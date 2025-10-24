
# imports
import re
import os
import string
import numpy as np
import pandas as pd
import spacy
from nltk.corpus import stopwords
import nltk
from pathlib import Path
from nltk.stem.snowball import GermanStemmer
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing
from spacy.cli import download as spacy_download
from pandas import concat


def ensure_required_nlp_resources():
    """
    Ensures all required NLP resources for German-language processing using NLTK and spaCy
    are downloaded and available *before* (parallel) processing begins. This avoids runtime
    download errors in subprocesses by ensuring all dependencies are present upfront.

    :dependency: nltk: punkt (tokenizer), stopwords (corpora)
    :dependency: spacy: de_core_news_sm (German language model)

    :param: None

    :return: None

    :raises: None (all missing resources are downloaded silently)
    """

    print("[Setup] Checking required NLTK and spaCy resources...")

    # Define NLTK resources and paths
    nltk_resources = {
        "tokenizers/punkt": "punkt",
        "tokenizers/punkt_tab": "punkt_tab",
        "corpora/stopwords": "stopwords"
    }

    for resource_path, resource_name in nltk_resources.items():
        try:
            nltk.data.find(resource_path)
            print(f"[NLTK] Resource '{resource_name}' already available.")
        except LookupError:
            print(f"[NLTK] Resource '{resource_name}' not found. Downloading...")
            nltk.download(resource_name, quiet=True)

    # Check and download spaCy German model
    try:
        _ = spacy.load("de_core_news_sm")
        print("[spaCy] Model 'de_core_news_sm' is already installed.")
    except OSError:
        print("[spaCy] Model 'de_core_news_sm' not found. Downloading...")
        spacy_download("de_core_news_sm")
        print("[spaCy] Model 'de_core_news_sm' downloaded successfully.")

    print("[Setup] All resources are available.")



def safe_nltk_download(resource):
    """
    Downloads an NLTK resource only if it is not already available. This function is
    designed to be safe in multi-threaded or multi-processed environments, such as when
    running preprocessing pipelines in parallel. It attempts to locate the specified
    resource in the local NLTK data directory, and only downloads it if it cannot be found.

    :dependency: nltk: Required for tokenization, stopword removal, and stemming.

    :param: resource (str): Resource path string, e.g. "tokenizers/punkt" or "corpora/stopwords".

    :return: None

    :raises: None (fails silently if download is not possible)
    """
    try:
        nltk.data.find(resource)
    except LookupError:
        nltk.download(resource.split('/')[-1], quiet=True)



def combine_two_datasets(input_path_a, input_path_b, output_path) -> None:
    """
    Combines two pickled pandas DataFrames into one and saves the result to the specified output path.

    :param: input_path_a (str or Path): File path to the first pickled dataset (e.g. term 19).
    :param: input_path_b (str or Path): File path to the second pickled dataset (e.g. term 20).
    :param: output_path (str or Path): File path to which the combined dataset should be saved.

    :return: None: The function saves the combined DataFrame as a pickle file and prints status messages.

    :raises: FileNotFoundError: If one of the input files does not exist.
    :raises: ValueError: If the loaded objects are not pandas DataFrames.
    :raises: Exception: If any unexpected error occurs during file loading, concatenation, or saving.
    """
    try:
        # Convert inputs to Path objects
        input_path_a = Path(input_path_a)
        input_path_b = Path(input_path_b)
        output_path = Path(output_path)

        # Check if input files exist
        if not os.path.isfile(input_path_a):
            raise FileNotFoundError(f"combine_two_datasets: [ERROR]: Input file A not found: {input_path_a}")
        if not os.path.isfile(input_path_b):
            raise FileNotFoundError(f"combine_two_datasets: [ERROR]: Input file B not found: {input_path_b}")

        # Validate output path extension
        if output_path.suffix != ".pkl":
            raise ValueError(f"combine_two_datasets: [ERROR]: Output path must end with '.pkl', got: {output_path.suffix}")

        # Load input data
        data_set_a = pd.read_pickle(input_path_a)
        data_set_b = pd.read_pickle(input_path_b)

        # Verify that both are DataFrames
        if not isinstance(data_set_a, pd.DataFrame) or not isinstance(data_set_b, pd.DataFrame):
            raise ValueError("combine_two_datasets: [ERROR]: One or both input files do not contain pandas DataFrames.")

        # Check column consistency
        if set(data_set_a.columns) != set(data_set_b.columns):
            raise ValueError("combine_two_datasets: [ERROR]: The two DataFrames do not have identical columns.")

        # Combine datasets
        data_set_a_b = concat([data_set_a, data_set_b], ignore_index=True)

        # Save combined dataset
        os.makedirs(os.path.dirname(output_path), exist_ok=True) # ensure output dir exists
        data_set_a_b.to_pickle(output_path)

        # Report statistics
        print(f"combine_two_datasets: Dataset A: {len(data_set_a)} rows")
        print(f"combine_two_datasets: Dataset B: {len(data_set_b)} rows")
        print(f"combine_two_datasets: Combined : {len(data_set_a_b)} rows")
        print(f"combine_two_datasets: Datasets successfully combined and saved to: {output_path}")

    except Exception as e:
        print(f"combine_two_datasets: [ERROR]: Failed to combine datasets: {e}")



# Wrapper-Function for parallel processing
def run_preprocessing(dataset, config):
    """
    Wrapper-Function for parallel processing
    Executes the speech preprocessing pipeline for a single dataset based on the provided configuration
    and validates the configuration and delegates all arguments to the `preprocess_speech_data` function.

    :param: dataset (str): A name identifier for the dataset (used for logging and status reporting).
    :param: config (dict): A dictionary containing all preprocessing options. Required keys are:
        Mandatory keys:
            - 'input_path' (Path): Path to the input .pkl file.
            - 'output_path_pickle' (Path): Path to save the cleaned .pkl file.
        Optional keys:
            Any keyword argument accepted by `preprocess_speech_data()` (e.g., stopword_mode, lemmatization, ...).

    :return: (str): A status message indicating the completion of the 'dataset' processing.

    :raises: TypeError: If the input types are invalid.
    :raises: ValueError: If required keys are missing or misconfigured.
    """
    # Input validation
    if not isinstance(dataset, str):
        raise TypeError(f"{dataset} config: Parameter 'dataset' must be a string.")

    if not isinstance(config, dict):
        raise TypeError(f"{dataset} config: Parameter 'config' must be a dictionary.")

    required_keys = ["input_path", "output_path_pickle"]
    for key in required_keys:
        if key not in config:
            raise ValueError(f"{dataset} config: Missing required config key: '{key}'")
        if not isinstance(config[key], Path):
            raise TypeError(f"{dataset} config: Config key '{key}' must be of type pathlib.Path")

    # keep going till every config has been looked at and skip faulty processes
    try:
        # Delegate to the preprocessing function
        preprocess_speech_data(
            input_path=config["input_path"],
            output_path_pickle=config["output_path_pickle"],
            output_path_excel=config.get("output_path_excel", None),
            position_short=["Presidium of Parliament", "Guest"],
            only_valid_faction_id=config.get("only_valid_faction_id", False),
            without_faction=config.get("without_faction", None),
            change_faction=config.get("change_faction", None),
            generate_contributions_data=config.get("generate_contributions_data", False),
            contributions=config.get("contributions", "REMOVE"),
            contributions_simplified_path=config.get("contributions_simplified_path", None),
            contributions_extended_path=config.get("contributions_extended_path", None),
            to_lower=config.get("to_lower", False),
            remove_digits=config.get("remove_digits", False),
            remove_punctuation=config.get("remove_punctuation", False),
            stopword_mode=config.get("stopword_mode", "NONE"),
            custom_stopwords=config.get("custom_stopwords", None),
            phrase_patterns=config.get("phrase_patterns", None),
            lemmatization=config.get("lemmatization", True),
            stemming=config.get("stemming", False),
            tokenization_method=config.get("tokenization_method", "NONE"),
            add_char_count=config.get("add_char_count", False),
            add_token_count=config.get("add_token_count", False),
            add_lemma_count=config.get("add_lemma_count", False),
            log_prefix = config.get("log_prefix", ""),
            parallel_processing = True
        )
        return f"{dataset} completed successfully."
    except Exception as e:
        return f"[{dataset}] not completed. Error occurred: {type(e).__name__}: {e}"



# parallel execution
def execute_parallel_preprocessing(dataset_configs):
    """
    Executes multiple preprocessing tasks in parallel using all available CPU cores.
    This function distributes independent dataset configurations across multiple processes
    using Python’s multiprocessing backend. Each dataset configuration will be handled
    by `run_preprocessing`, which wraps the `preprocess_speech_data()` call with proper
    configuration validation.

    :param: dataset_configs (dict):
            A dictionary where each key is a dataset name (str), and each value is a config dict for one dataset
            with arguments passed to `run_preprocessing`.
            The config dict must include at least a'input_path' (Path) and 'output_path_pickle' (Path)
        Additional keys may include preprocessing options (e.g. `to_lower`, `lemmatization`, ...).
        Example:
        dataset_configs = {
            "data_set_1": {
                "input_path": Path("input_1.pkl"),
                "output_path_pickle": Path("output_1.pkl"),
                "to_lower": True,
                ...
            },
            "data_set_2": {
                ...
            }
        }
    :return: None. Prints progress and result status messages to console.

    :raises: TypeError: If input is not a dict.
    :raises: ValueError: If the dictionary is empty.
    """
    # Input validation
    if not isinstance(dataset_configs, dict):
        raise TypeError(f"execute_parallel_preprocessing: Parameter 'dataset_configs' must be a dictionary.")

    if not dataset_configs:
        raise ValueError(f"execute_parallel_preprocessing: No dataset configurations provided.")

    # Determine the number of CPU cores to use
    n_cores = min(10, multiprocessing.cpu_count())
    print(f"[INFO] Using {n_cores} cores")

    # Create a process pool and submit preprocessing tasks
    with ProcessPoolExecutor(max_workers=n_cores) as executor:
        futures = [
            executor.submit(run_preprocessing, dataset, config)
            for dataset, config in dataset_configs.items()
        ]

        # Wait for all tasks to complete and print results
        for future in as_completed(futures):
            try:
                result = future.result()
                print(f"[RESULT] {result}")
            except Exception as e:
                print(f"[ERROR] Unexpected error during parallel execution: {type(e).__name__}: {e}")



def preprocess_speech_data(
    input_path: Path,                   # mandatory: cannot be empty
    output_path_pickle: Path,           # mandatory: cannot be empty
    output_path_excel: Path = None,     # optional: can be empty
    position_short: list[str] = None,   # All lines with position_shorts that match any of those strings will be deleted before the preprocessing process starts
    only_valid_faction_id: bool = False,# All lines with invalid faction_id (-1) will be deleted before the preprocessing process starts
    without_faction: str = None,        # All lines matching this faction_id will be deleted before the preprocessing process starts
    change_faction: list[str] = None,   # change_faction must be a list of two strings: [old_faction_id, new_faction_id]
                                        # All matching old_faction_ids will be replaced by new_faction_id
    generate_contributions_data: bool = False,
    contributions: str = "NONE",  # "REMOVE" or "INSERT" or "NONE"
    contributions_simplified_path: Path = None, # path to contributions_simplified file
    contributions_extended_path: Path = None, # path to contributions_extended file
    to_lower: bool = False,             # turns every character to lower case
    remove_digits: bool = False,        # removes all digits from speech_content
    remove_punctuation: bool = False,   # removes !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    stopword_mode: str = "NONE",  # "NLTK" or "SPACY" or "NONE"
    custom_stopwords: set = None,       # allows users to add custom stopword sets to nltk's or spacy's standard lists
    phrase_patterns: list[str] = None,  # allows users to give a list of regex based patterns which will be removed
    lemmatization: bool = False,        # lemmatizes cleaned speeches
    stemming: bool = False,             # stems every word in cleaned speeches
    tokenization_method: str = "NONE", # "NLTK" or "SPACY" or "NONE"
    add_char_count: bool = False,       # adds a column with the character count of each speech to the output
    add_token_count: bool = False,      # adds a column with the token count of each speech to the output
    add_lemma_count: bool = False,      # adds a column with the lemma count of each speech to the output
    log_prefix: str = "",               # adds a custom message before every log
    parallel_processing: bool = False         # shifts the log messages to multiline while parallel processing for better readability
):
    """
    This function applies a configurable and modular preprocessing pipeline to Bundestag speech
    data (column: 'speech_content'), supporting advanced filtering, text normalization, contribution handling,
    stopword removal, linguistic normalization (lemmatization, stemming, tokenization), and speech length statistics.
    The function can also extract and store related contribution data for the filtered subset of speeches.

    Capabilities:
    1. Loads the speech content from a .pkl file and verifies required columns.
    2. Optionally filters rows by speaker role (position_short), faction validity, or faction ID substitution.
    3. Optionally generates and stores matching simplified and extended contributions data for the remaining speeches.
    4. Applies contribution logic: either removes or reinserts contribution placeholders based on provided metadata.
    5. Cleans the speech text according to defined parameters (lowercasing, digits, punctuation, regex phrase removal).
    6. Optionally removes stopwords using either NLTK or spaCy stopword lists, optionally extended with custom terms.
    7. Optionally applies lemmatization and/or stemming to the cleaned text.
    8. Optionally tokenizes the cleaned text into lists of tokens.
    9. Optionally adds columns measuring character length, token count, or lemma count.
    10. Saves the resulting DataFrame to a .pkl file and optionally to .xlsx.
    11. Logs summary statistics for inspection.

    :param:
    | Parameter                      | Type                               | Standard | Description                                                                                                                                     |
    |--------------------------------|------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------|
    | `input_path`                   | `Path`                             |          | Mandatory: Path to the input `.pkl` file containing the speeches                                                                                |
    | `output_path_pickle`           | `Path`                             |          | Mandatory: Path where the cleaned `.pkl` file shall be saved                                                                                    |
    | `output_path_excel`            | `Path`                             | `None`   | Enables Excel export of the results to the given path                                                                                           |
    | `position_short`               | `list[str]`                        | `None`   | Filters out rows where position_short matches one mentioned in the given list (e.g., "Guest") (Case sensitive!)                                 |
    | `only_valid_faction_id`        | `bool`                             | `False`  | If Enabled: Removes all speeches with `faction_id == -1`                                                                                        |
    | `without_faction`              | `str`                              | `None`   | Removes all speeches with this specific faction ID                                                                                              |
    | `change_faction`               | `list[str]`                        | `None`   | change_faction must be a list of two strings: [old_faction_id, new_faction_id]. All matching old_faction_ids will be replaced by new_faction_id |
    | `generate_contributions_data`  | `bool`                             | `False`  | If Enabled: Saves reduced contributions data matching speech_ids in dataset                                                                     |
    | `contributions`                | `"REMOVE"` / `"INSERT"` / `"NONE"` | `"NONE"` | Controls how contribution position markers (e.g., ({2}) ) are handled                                                                           |
    | `contributions_simplified_path`| `Path`                             | `None`   | Optional path to the simplified contributions `.pkl` file. Used for reinsertion (if `contributions="INSERT"`) and for generating filtered contributions (if `generate_contributions_data=True`) |
    | `contributions_extended_path`  | `Path`                             | `None`   | Optional path to the extended contributions `.pkl` file. Only used for generating filtered contributions (if `generate_contributions_data=True`)|
    | `to_lower`                     | `bool`                             | `False`  | If Enabled: Converts all text to lowercase                                                                                                      |
    | `remove_digits`                | `bool`                             | `False`  | If Enabled: Removes all numeric digits                                                                                                          |
    | `remove_punctuation`           | `bool`                             | `False`  | If Enabled: Removes punctuation characters                                                                                                      |
    | `stopword_mode`                | `"NLTK"` / `"SPACY"` / `"NONE"`    | `"NONE"` | Enables stopword removal and selects stopword removal method                                                                                    |
    | `custom_stopwords`             | `set`                              | `None`   | Input for a set of domain-specific stopwords to extend base lists                                                                               |
    | `phrase_patterns`              | `list[str]`                        | `None`   | Input for a list of regexes for regex-phrase-based text removal                                                                                 |
    | `lemmatization`                | `bool`                             | `False`  | If Enabled: Applies lemmatization using spaCy                                                                                                   |
    | `stemming`                     | `bool`                             | `False`  | If Enabled: Applies stemming using NLTK                                                                                                         |
    | `tokenization_method`          | `"NLTK"` / `"SPACY"` / `"NONE"`    | `"NONE"` | Enables tokenization and defines which Tokenizer is used                                                                                        |
    | `add_char_count`               | `bool`                             | `False`  | If Enabled: Adds a column with character count (counts characters after latest preprocessing step)                                              |
    | `add_token_count`              | `bool`                             | `False`  | If Enabled: Adds a column with token count (if tokenization is also enabled)                                                                    |
    | `add_lemma_count`              | `bool`                             | `False`  | If Enabled: Adds a column with lemma count (if lemmatization is also enabled)                                                                   |

    :return:
    - No value is returned (in-place saving only).
    - The preprocessed speech DataFrame is saved to:
        - `output_path_pickle` (.pkl, always)
        - `output_path_excel` (.xlsx, optional)
    - If `generate_contributions_data=True`, two additional files are saved in the same directory:
        - `contributions_simplified.pkl`
        - `contributions_extended.pkl`

    Output DataFrame Columns:
    The output DataFrame retains all original columns from the input (such as `id`, `speech_content`, `faction_id`, etc.) and adds the following **preprocessing columns**:
    | Column                      | Description                                                                                                                     |
    |-----------------------------|---------------------------------------------------------------------------------------------------------------------------------|
    | `speech_content_cleaned`    | Cleaned version of original text (case/digit/punctuation/phrase normalized)                                                     |
    | `speech_content_stopword`   | Cleaned text after stopword removal if stopword removal enabled, else: ""                                                       |
    | `speech_content_lemmatized` | List of SPACY lemmas if lemmatization enabled, else: []                                                                         |
    | `speech_content_stemmed`    | Stemmed text if stemming enabled, else: ""                                                                                      |
    | `speech_content_tokenized`  | List of SPACY tokens if tokenization enabled, else: []                                                                          |
    | `speech_length_chars`       | Number of characters in stemmed text (if stemming disabled: stop word removed text, if stopword removal disabled: cleaned text) |
    | `speech_length_lemmas`      | Number of lemmas if 'add_lemma_count' flag is enabled and text has been lemmatized, else -1                                     |
    | `speech_length_tokens`      | Number of tokens if 'add_token_count' flag is enabled and text has been tokenized, else -1                                      |
    """

    # set up variables
    spacy_instance = None
    all_sw = set()
    stemmer = GermanStemmer()
    contributions_simplified_df = None
    contributions_extended_df = None


    def initial_data_filter(data: pd.DataFrame) -> pd.DataFrame:
        """
        Filters, transforms or updates the input DataFrame based on optional criteria such as
        unwanted positions, invalid or missing faction IDs, and faction replacements.
        Also generates contribution files limited to the remaining relevant speeches if configured.
        Logs the number of rows affected by each filtering operation in stdout.

        Filtering Steps:
        - Removes rows where `position_short` matches an excluded role (e.g., "Presidium of Parliament")
        - Removes rows with invalid `faction_id` (value -1)
        - Removes rows with a specific `faction_id` (e.g., "9")
        - Replaces specific `faction_id` values using [old, new] list
        - Optionally creates contribution files limited to remaining speech IDs

        :dependency: `contributions_simplified_19_20.pkl` must exist at fixed path

        :param: data (pd.DataFrame): Input DataFrame with speech content and metadata.
            Required columns: 'faction_id', 'position_short', 'speech_content', 'id'

        :return: filtered_data (pd.DataFrame): Filtered and/or updated DataFrame.

        :raises: ValueError: If required columns are missing or `change_faction` is misconfigured.
        """
        # validate input df
        required_columns = {"faction_id", "position_short", "speech_content"}
        missing_columns = required_columns - set(data.columns)
        if missing_columns:
            raise ValueError(f"{log_prefix}: Input file is missing required columns: {missing_columns}")
        original_len = len(data)

        # Remove rows where 'position_short' is in the provided exclusion list
        if position_short:
            before = len(data)
            data = data[
                (~data["position_short"].isin(position_short))
            ]
            print(f"{log_prefix}: [position_short Filter] Removed {before - len(data)} rows with excluded 'position_short' values.")

        # Keep only rows where faction_id is valid (not -1)
        if only_valid_faction_id:
            before = len(data)
            data = data[
                (data["faction_id"].astype(str) != "-1")
            ]
            print(f"{log_prefix}: [only_valid_faction_id Filter] Removed {before - len(data)} rows with invalid faction_id (-1).")

        # Remove rows with a specific faction_id (string match)
        if without_faction:
            before = len(data)
            data = data[
                (data["faction_id"].astype(str) != without_faction)
            ]
            print(f"{log_prefix}: [faction_id Filter] Removed {before - len(data)} rows with faction_id == '{without_faction}'.")

        # Replace all faction_id values matching change_faction[0] with change_faction[1]
        if change_faction:
            if not isinstance(change_faction, list) or len(change_faction) != 2:
                raise ValueError("change_faction must be a list of two strings [old_id, new_id]")
            old_id, new_id = change_faction
            matches = data["faction_id"].astype(str) == str(old_id)
            replacements = matches.sum()
            data.loc[matches, "faction_id"] = int(new_id)
            print(f"{log_prefix}: [change_faction Transform] Replaced faction_id '{old_id}' with '{new_id}' in {replacements} rows.")

        # Generates one file for contributions_simplified and one for contributions_extended only containing the relevant data
        if generate_contributions_data:
            if contributions_simplified_df is None:
                print(f"{log_prefix}: [ERROR] Could not load contributions simplified and will not generate file: {e}")
                return data
            if contributions_extended_df is None:
                print(f"{log_prefix}: [ERROR] Could not load contributions extended and will not generate file: {e}")
                return data
            # setup data
            contrib_ext_df  = contributions_extended_df.copy()
            contrib_simpl_df = contributions_simplified_df.copy()
            # filterlogic contributions
            valid_ids = set(data["id"])
            contrib_ext_filtered = contrib_ext_df[contrib_ext_df["speech_id"].isin(valid_ids)]
            contrib_simpl_filtered = contrib_simpl_df[contrib_simpl_df["speech_id"].isin(valid_ids)]
            # prepare output path
            output_path_pickle.parent.mkdir(parents=True, exist_ok=True)
            # save filtered contributions
            contrib_simpl_filtered.to_pickle(output_path_pickle.parent / f"contributions_simplified.pkl")
            contrib_ext_filtered.to_pickle(output_path_pickle.parent / f"contributions_extended.pkl")
            print(f"{log_prefix}: [generate_contribution_data Transform] Saved {len(contrib_simpl_filtered)} rows for simplified and {len(contrib_ext_filtered)} for extended.")

        print(f"{log_prefix}: [initial_data_filter Summary] Total rows after filtering: {len(data)} (from {original_len})")

        return data


    def handle_contributions(text: str, speech_id: int, contributions_simplified: pd.DataFrame):
        """
        Either removes or reinserts contributions into speech_content, based on simplified contribution data.

        :param: text (str): The speech text with contribution position markers.
        :param: speech_id (int): The ID of the speech.

        :return: str: The updated text (either without contribution position markers or with inserted contribution descriptions).
        """
        # remove contribution text postion markers
        if contributions.upper() == "REMOVE":
            text = re.sub(r'\[.*?\]', ' ', text, flags=re.IGNORECASE | re.MULTILINE)   # Remove "[Beifall]" and brackets like "[...]"
            text = re.sub(r'\(\{\d+\}\)', ' ', text, flags=re.IGNORECASE | re.MULTILINE)  # Remove "({<NUM>})" (placeholders for contributions)

        # insert old contributions
        elif contributions.upper() == "INSERT":
            # failsafe
            if contributions_simplified.empty:
                print(f"{log_prefix}: [WARNING] contribution_simplified df empty for speech {speech_id}. Skipping insertion.")
                return text

            # helperfunction to find the right contributions for the text position marker and speech id
            def handle_match(match):
                try:
                    pos = int(match.group().strip("{}()"))
                    speech_contribution = contributions_simplified[
                        (contributions_simplified["speech_id"].astype(int) == speech_id) &
                        (contributions_simplified["text_position"].astype(int) == pos)
                        ]
                    if not speech_contribution.empty:
                        return " ".join(speech_contribution["content"].astype(str))
                except Exception:
                    print(f"{log_prefix}: [WARNING] Insertion did not work in speech {speech_id}. Skipping insertion.")
                    pass
                return ""

            # replace every text position contribution marker step by step
            text = re.sub(r'\(\{\d+\}\)', handle_match, text)

        return text


    def clean(text):
        """
        Normalizes and cleans a speech string by applying several optional steps:
        lowercasing, digit removal, punctuation removal, phrase-based regex cleaning,
        and whitespace normalization.

        :param: text (str): The raw speech tet.

        :return: cleaned_text (str): Speech in various states of cleanliness.
        """
        if to_lower:
            text = text.lower()

        if remove_digits:
            text = re.sub(r"\d+", " ", text)  # Remove digits

        if remove_punctuation:
            text = re.sub(rf"[{re.escape(string.punctuation)}]", " ", text) # Remove punctuation

        # phrase-based removal if patterns were passed
        text = phrase_based_removal(text, phrase_patterns or [])

        # collapse white space as standard
        text = re.sub(r"\s+", " ", text)

        return text.strip()


    def phrase_based_removal(text: str, patterns: list[str]) -> str:
        """
        Removes phrases from the input text that match any of the provided regex patterns.
        If the list is empty, the text is returned unchanged.

        :param text (str): The raw or partially cleaned speech text to be processed.
        :param patterns (list[str]): A list of regex patterns. Each pattern will be applied independently to the text and replaced with a space.

        :return: cleaned_text (str): The input string with all matched patterns removed.
        """
        if not patterns:
            return text

        for pattern in patterns:
            text = re.sub(pattern, ' ', text, flags=re.IGNORECASE | re.MULTILINE)

        return text


    def remove_stopwords(text):
        """
        Removes stopwords from the input text based on the configured method ("NLTK" or "SPACY").

        :param text (str): Typically cleaned speech text.

        :return: filtered_text (str): The input string without stopwords, or original if stopword_mode is "NONE".
        """
        if stopword_mode.upper() == "NLTK":
            return " ".join([w for w in text.split() if w not in all_sw])

        elif stopword_mode.upper() == "SPACY":
            doc = spacy_instance(text)
            return " ".join(t.text for t in doc if not t.is_stop and not t.is_space and not t.is_punct)

        return ""


    def lemmatize_text(text: str) -> list[str]:
        """
        Lemmatizes the given text using spaCy's German language model.

        :dependency: spaCy – requires `de_core_news_sm` and a valid `spacy_instance`

        :param: text (str): The input text string (usually pre-cleaned and stopword-processed).

        :return: lemmas (list[str]): List of lemmatized word forms, skipping whitespace tokens.
                                 Returns empty list on error or if lemmatization is disabled.

        :raises: TypeError: If input is not a string.
        """
        # typecheck input
        if not isinstance(text, str):
            raise TypeError(f"Lemmatization expects string input, got {type(text)}")

        if lemmatization:
            try:
                doc = spacy_instance(text)
                return [t.lemma_ for t in doc if not t.is_space]
            except Exception as e:
                print(f"{log_prefix}: WARNING: spaCy lemmatization failed: {e}")
                return []

        return []


    def stem_text(text: str) -> str:
        """
        Applies stemming to the given German text using NLTK's SnowballStemmer.
        Tokenizes the input text and stems each word if alphabetic. Falls back to downloading
        the Punkt tokenizer if not available.

        :dependency: nltk: punkt tokenizer and SnowballStemmer for German
        :dependency: stemmer: pre-initialized GermanStemmer object

        :param: text (str): Preprocessed input text (ideally cleaned and stopword-processed).

        :return: stemmed_text (str): Stemmed version of the input string (words joined by spaces).
                                 Returns empty string if stemming is disabled or fails.

        :raises: TypeError: If input is not a string.
        """
        # typecheck input
        if not isinstance(text, str):
            raise TypeError(f"{log_prefix}: WARNING: Stemming expects string input, got {type(text)}")

        if stemming:
            try:
                tokens = nltk.word_tokenize(text, language="german")
                return " ".join(stemmer.stem(token) for token in tokens if token.isalpha())
            except LookupError:
                try:
                    nltk.download('punkt_tab', quiet=True)
                    tokens = nltk.word_tokenize(text, language="german")
                    return " ".join(stemmer.stem(token) for token in tokens if token.isalpha())
                except:
                    print(f"{log_prefix}: WARNING: punkt tokenizer not available, skipping stemming.")
                    return ""

        return ""


    def tokenize_text(text: str) -> list[str]:
        """
        Tokenizes the input text using the selected method: "SPACY" or "NLTK".
        Returns a list of string tokens. Falls back to downloading resources if required.

        :dependency: spaCy: for linguistically-informed tokenization (`de_core_news_sm`)
        :dependency: nltk: for simple word-based tokenization (`punkt`)

        :param: text (str): The input string to tokenize. Raw or preprocessed text.

        :return: tokens (list[str]): A list of tokens
                                     Or an empty list if tokenization fails or is disabled (method = "NONE").

        :raises: TypeError: If input is not a string.
        """
        # typecheck input
        if not isinstance(text, str):
            raise TypeError(f"Tokenization expects string input, got {type(text)}")

        if tokenization_method.upper() == "SPACY":
            try:
                doc = spacy_instance(text)
                return [t.text for t in doc if not t.is_space]
            except Exception as e:
                print(f"{log_prefix}: WARNING: spaCy tokenization failed: {e}")
                return []

        elif tokenization_method.upper() == "NLTK":
            try:
                return nltk.word_tokenize(text, language="german")
            except LookupError:
                try:
                    nltk.download("punkt", quiet=True)
                    return nltk.word_tokenize(text, language="german")
                except:
                    print(f"{log_prefix}: WARNING: punkt tokenizer not available, skipping tokenization.")
                    return []

        return []


    def char_count(text: str) -> int:
        """
        Returns the number of characters in the input text if character count
        tracking is enabled via the 'add_char_count' flag. Otherwise, returns -1.

        :param: text (str): The preprocessed text string whose character length is to be evaluated.

        :return: count (int): Number of characters in the text, or -1 if 'add_char_count' flag is False.

        :raises: TypeError: If input is not a string.
        """
        # typecheck input
        if not isinstance(text, str):
            raise TypeError(f"{log_prefix}: WARNING: char_count expects string input, got {type(text)}")

        if add_char_count:
            return len(text)
        return -1


    def lemma_count(text: list[str]) -> int:
        """
        Returns the number of lemmas (assumed to be whitespace-separated tokens)
        in the input text if lemma count tracking is enabled via the
        'add_lemma_count' flag and text has been lemmatized. Otherwise, returns -1.

        :param: text (list[str]): List of lemmatized tokens to be counted

        :return: count (int): Number of lemmas, or -1 if 'add_lemma_count' is False or lemmatization is disabled.

        :raises TypeError: If input is not a list.
        """
        # typecheck input
        if not isinstance(text, list):
            raise TypeError(f"{log_prefix}: WARNING: lemma_count expects string list input, got {type(text)}")

        if add_lemma_count and lemmatization:
            return len(text)
        return -1


    def token_count(text: list[str]) -> int:
        """
        Returns the number of tokens in the input list if token count tracking
        is enabled via the 'add_token_count' flag and text has been tokenized. Otherwise, returns -1.

        :param: text (list[str]): A list of tokens (e.g., words or subwords).

        :return: count (int): Number of tokens,  or -1 if 'add_token_count' is False or tokenization is disabled.

        :raises TypeError: If input is not a list.
        """
        # typecheck input
        if not isinstance(text, list):
            raise TypeError(f"{log_prefix}: WARNING: token_count expects string list input, got {type(text)}")

        if add_token_count and (tokenization_method.upper() != "NONE"):
            return len(text)
        return -1




    # check input path value
    if not input_path or not input_path.exists():
        raise ValueError(f"{log_prefix}: You must provide a valid input_path pointing to an existing .pkl file")
    # load data and check for speech_content column
    df = pd.read_pickle(input_path)
    assert "speech_content" in df.columns, "Input file must contain 'speech_content' column."
    print(f"{log_prefix}: Input path <{input_path}> is correct.")

    # setup spacy instance
    needs_spacy = (
            stopword_mode.upper() == "SPACY"
            or tokenization_method.upper() == "SPACY"
            or lemmatization
    )
    if needs_spacy and spacy_instance is None:
        print(f"{log_prefix}: Setting up spacy instance ... ", end="", flush= not parallel_processing)
        try:
            spacy_instance = spacy.load("de_core_news_sm")
        except OSError:
            print(f"{log_prefix}: spaCy model not found. Downloading ...")
            from spacy.cli import download
            download("de_core_news_sm")
            spacy_instance = spacy.load("de_core_news_sm")
        print(f"{log_prefix}: Done.")

    # setup nltk
    if stemming or tokenization_method.upper() == "NLTK":
        safe_nltk_download("tokenizers/punkt")  #  punkt
        safe_nltk_download("tokenizers/punkt_tab")
        safe_nltk_download("corpora/stopwords")

    # setup contributions dfs
    if contributions.upper() == "INSERT" or generate_contributions_data:
        # load contribution data if necessary
        if contributions_simplified_df is None:
            simplified_path = contributions_simplified_path or Path(
                "../../Data/DataFinalStage/contributionsSimplified/contributions_simplified_19_20.pkl")  #
            if not os.path.exists(simplified_path):
                print(f"{log_prefix}: [WARNING] Missing contribution_simplified file: {simplified_path}.")
            try:
                print(f"{log_prefix}: Loading contributions simplified Pickle ...")
                contributions_simplified_df = pd.read_pickle(simplified_path)
                print(f"{log_prefix}: Contributions loaded.")
            except (EOFError, FileNotFoundError) as e:
                contributions_simplified_df = pd.DataFrame()  # empty
                print(f"{log_prefix}: [ERROR] Could not load the provided contributions simplified file. Contribution Mode now is REMOVE and no contributions data will be generated: {e}")
                contributions = "REMOVE"
                generate_contributions_data = False
        # check for matching ids
        if not contributions_simplified_df.empty:
            speech_ids_in_df = set(df["id"].unique())
            speech_ids_in_contributions = set(contributions_simplified_df["speech_id"].unique())
            missing_speech_ids = speech_ids_in_df - speech_ids_in_contributions
            if missing_speech_ids:
                print(f"{log_prefix}: [ERROR] {len(missing_speech_ids)} speeches in input dir have no matching contributions in the provided contributions simplified file. Contribution Mode now is REMOVE and no contributions data will be generated!")
                contributions = "REMOVE"
                generate_contributions_data = False
    if generate_contributions_data:
        if contributions_extended_df is None:
            contrib_ext_path = contributions_extended_path or Path(
                "../../Data/dataFinalStage/contributionsExtendedFinalStage/contributions_extended_19_20.pkl")
            if not os.path.exists(contrib_ext_path):
                print(f"{log_prefix}: [WARNING] Missing contribution extended file: {contrib_ext_path}.")
            try:
                print(f"{log_prefix}: Loading contributions extended Pickle ...")
                contributions_extended_df = pd.read_pickle(contrib_ext_path)
                print(f"{log_prefix}: Contributions loaded.")
            except (EOFError, FileNotFoundError) as e:
                contributions_extended_df = pd.DataFrame()  # empty
                print(f"{log_prefix}: [ERROR] Could not load the provided contributions extended file. No contributions data will be generated: {e}")
                generate_contributions_data = False
        # check for matching ids
        if not contributions_extended_df.empty:
            speech_ids_in_df = set(df["id"].unique())
            speech_ids_in_contributions = set(contributions_extended_df["speech_id"].unique())
            missing_speech_ids = speech_ids_in_df - speech_ids_in_contributions
            if missing_speech_ids:
                print(f"{log_prefix}: [ERROR] {len(missing_speech_ids)} speeches in input dir have no matching contributions in the provided contributions extended file. No contributions data will be generated!")
                generate_contributions_data = False

    # filter for relevant rows (deletes all irrelevant rows)
    print(f"{log_prefix}: Filter data frame ... ", end="", flush= not parallel_processing)
    df = initial_data_filter(df)
    print(f"{log_prefix}: Done.")

    # Apply contributions logic in DataFrame row-wise
    if contributions.upper() != "NONE": print(f"{log_prefix}: Handle contributions ... ", end="", flush= not parallel_processing)
    df["speech_content"] = df.apply(
        lambda row: handle_contributions(row["speech_content"], row["id"], contributions_simplified_df),
        axis=1
    )
    if contributions.upper() != "NONE": print(f"{log_prefix}: Done.")

    # clean speech_content as to the defined specifications
    print(f"{log_prefix}: Clean speech content ...", end="", flush= not parallel_processing)
    df["speech_content_cleaned"] = df["speech_content"].astype(str).apply(clean) # only collapses whitespace as standard
    print(f"{log_prefix}: Done.")

    # setup NLTK stopwords
    if stopword_mode == "NLTK":
        print(f"{log_prefix}: Setting up NLTK for stopword removal ... ", end="", flush= not parallel_processing)
        # download stopwords once
        safe_nltk_download("corpora/stopwords")
        nltk_sw = set(stopwords.words("german"))
        # additional domain-specific stopwords
        custom_sw = custom_stopwords or set()
        # combine all stopwords
        all_sw = nltk_sw.union(custom_sw)
        print(f"{log_prefix}: Done.")

    # setup SPACY stopwords
    if stopword_mode == "SPACY":
        print(f"{log_prefix}: Setting up SPACY for stopword removal ... ", end="", flush= not parallel_processing)
        # download stopwords once
        safe_nltk_download("corpora/stopwords")
        nltk_sw = set(stopwords.words("german"))
        # spacy_instance = spacy.load("de_core_news_sm")
        # additional domain-specific stopwords
        custom_sw = custom_stopwords or set()
        # combine all stopwords
        all_sw = nltk_sw.union(custom_sw)
        for word in all_sw:
            spacy_instance.Defaults.stop_words.add(word)
            spacy_instance.vocab[word].is_stop = True
        print(f"{log_prefix}: Done.")

    # remove stopwords if not (stopword_mode == "NONE")
    if stopword_mode.upper() != "NONE": print(f"{log_prefix}: Removing stopwords ... ", end="", flush= not parallel_processing)
    df["speech_content_stopword"] = df["speech_content_cleaned"].apply(remove_stopwords)
    if stopword_mode.upper() != "NONE": print(f"{log_prefix}: Done.")

    # lemmatize speeches after stopwords have been removed
    if lemmatization: print(f"{log_prefix}: Lemmatizing speeches ... ", end="", flush= not parallel_processing)
    if stopword_mode.upper() != "NONE":
        df["speech_content_lemmatized"] = df["speech_content_stopword"].apply(lemmatize_text)
    else:
        df["speech_content_lemmatized"] = df["speech_content_cleaned"].apply(lemmatize_text)
    if lemmatization: print(f"{log_prefix}: Done.")

    # stem speeches after stopwords have been removed
    if stemming: print(f"{log_prefix}: Stemming speeches ... ", end="", flush= not parallel_processing)
    if stopword_mode.upper() != "NONE":
        df["speech_content_stemmed"] = df["speech_content_stopword"].apply(stem_text)
    else:
        df["speech_content_stemmed"] = df["speech_content_cleaned"].apply(stem_text)
    if stemming: print(f"{log_prefix}: Done.")

    # tokenize speeches after stopwords have been removed
    if tokenization_method.upper() != "NONE": print(f"{log_prefix}: Tokenizing speeches ... ", end="", flush= not parallel_processing)
    if stopword_mode.upper() != "NONE":
        df["speech_content_tokenized"] = df["speech_content_stopword"].apply(lambda t: tokenize_text(t))
    else:
        df["speech_content_tokenized"] = df["speech_content_cleaned"].apply(lambda t: tokenize_text(t))
    if tokenization_method.upper() != "NONE":print(f"{log_prefix}: Done.")

    # add speech_length_char column for next step
    if add_char_count: print(f"{log_prefix}: Counting chars ... ", end="", flush= not parallel_processing)
    if stemming: # use stemmed speech content
        df["speech_length_chars"] = df["speech_content_stemmed"].apply(char_count)
    elif stopword_mode.upper() != "NONE": # use stop-word-cleaned speech content
        df["speech_length_chars"] = df["speech_content_stopword"].apply(char_count)
    else:
        df["speech_length_chars"] = df["speech_content_cleaned"].apply(char_count)
    if add_char_count: print(f"{log_prefix}: Done.")

    # add speech_length_lemmas column for next step
    if add_lemma_count: print(f"{log_prefix}: Counting chars ... ", end="", flush= not parallel_processing)
    df["speech_length_lemmas"] = df["speech_content_lemmatized"].apply(lemma_count)
    if add_lemma_count: print(f"{log_prefix}: Done.")

    # add speech_length_tokens column for next step
    if add_token_count: print(f"{log_prefix}: Counting chars ... ", end="", flush= not parallel_processing)
    df["speech_length_tokens"] = df["speech_content_tokenized"].apply(token_count)
    if add_token_count: print(f"{log_prefix}: Done.")

    # save cleaned data
    print(f"{log_prefix}: Save cleaned data ... ", end="", flush= not parallel_processing)
    if output_path_pickle:
        output_path_pickle.parent.mkdir(parents=True, exist_ok=True)
        df.to_pickle(output_path_pickle)
    if output_path_excel:
        output_path_excel.parent.mkdir(parents=True, exist_ok=True)
        try:
            df.to_excel(output_path_excel, index=False)
        except ModuleNotFoundError as e:
            print(f"{log_prefix}: [WARNING] Skipping Excel export because of EXCEPTION: {e}")
    print(f"{log_prefix}: Done.")


    # give short overview of overall data loss
    print(f"{log_prefix}: Avg char length before cleaning:", df["speech_content"].str.len().mean())
    print(f"{log_prefix}: Avg char length after cleaning:", df["speech_content_stopword"].str.len().mean())
    print(f"{log_prefix}: Avg token count:", df["speech_length_tokens"].mean())



# Example Usage in Jupyter Notebook (EDIT PATHS BEFORE USING!!):
"""
# imports
from pathlib import Path
from Preprocessing_Pipeline import execute_parallel_preprocessing
from Preprocessing_Pipeline import ensure_required_nlp_resources

# spaCy-Ressourcen laden (in der Shell oder im Jupyter-Notebook via "!") 
!python -m spacy download de_core_news_sm

# regex pattern for phrase-based removal
PHRASE_PATTERNS_CLASSIFICATION_3 = [
    r"^sehr geehrte[r]? (herr|frau)?( präsident(in)?| vizepräsident(in)?).*?(kolleg(inn)?en)?", # Erweitert um optionale Begriffe wie "Kolleginnen und Kollegen"
    r"^meine (sehr geehrten )?damen und herren(,)?",                                            # Erweiterung um optionales "sehr geehrten" und Komma
    r"^(werte|liebe) kolleginnen und kollegen",                                                 # Erweiterung um "liebe" als Alternativformulierung
    r"^ich (möchte|will|werde|darf) mich.*?(bedanken|ausführen|äußern|anschließen)",            # Erweitert um typische Formulierungen wie "äußern" oder "anschließen"
    r"(zum|abschließend zum|abschließend möchte ich).*?schluss.*",                              # Erweiterung um häufige Formulierung "abschließend möchte ich"
    r"ich danke (ihnen|für ihre aufmerksamkeit|für ihre geduld).*?$",                           # Sicherstellung, dass Danksagungen am Ende exakt getroffen werden
    r"(vielen|herzlichen) dank für.*?$",                                                        # Ergänzung um häufige Dankes-Varianten am Redeende
    r"^(danke|besten dank|vielen dank).*?$",                                                    # Direkte Danksagungen am Anfang oder Ende der Rede
    r"^(herr|frau) (präsident|präsidentin|vizepräsident|vizepräsidentin),?$",                   # Einfache und sehr häufige Begrüßung des Präsidiums
]

# additional domain-specific stopwords
DOMAIN_SPECIFIC_STOPWORDS_CLASSIFICATION_1 = {
    # formelhafte Anrede & Begrüßung
    "liebe", "sehr", "geehrte", "geehrter", "damen", "herren", "werte",
    "kolleginnen", "kollegen", "kollege", "kollegin",
    "abgeordnete", "abgeordneter", "abgeordneten",
    # moderative Phrasen
    "frau", "herr", "präsident", "präsidentin", "vizepräsident", "vizepräsidentin",
    "schriftführer", "schriftführerin",
    # Redebeginn/-ende Floskeln
    "ich", "möchte", "mich", "nochmals", "danken", "bedanken", "danke",
    "zum", "schluss", "abschließend", "kommen", "kurz", "anmerken",
    # häufige höfliche, aber neutrale Füllwörter
    "bitte", "vielen", "herzlichen", "willkommen", "entschuldigung", "antrag",
    # häufige metakommunikative Floskeln
    "reden", "rede", "gesagt", "sagen", "sprechen", "beitrag",
    "anrede", "ausführungen", "feststellen", "meinen", "anmerken",
    # redundante Strukturwörter (keine grammatikalischen Stopwörter)
    "herrn", "frau", "wort", "genommen", "zurück", "vorweg"
}

# terms: numeric + kombi
terms = [19, 20, "19_20"]

dataset_configs = {}

for term in terms:
    dataset_configs_curr_term = {
        # data set 12: full cleaning, domain specific spacy stopword removal, phrase pattern removal
        f"data_set_12, term: {term}": {
            "input_path":Path(f"dataFinalStage/speechContentFinalStage/speech_content_{term}.pkl"),
            "output_path_pickle": Path(f"dataPreprocessedStage/dataClassification/speechContentCleaned/data_set_12_{term}.pkl"),
            #"output_path":_excel=Path(f"dataPreprocessedStage/dataClassification/speechContentCleaned/data_set_12_{term}.pkl"),

            # Optional filters (deactivated here)
            "position_short": ["Presidium of Parliament", "Guest"],  # removes presidium/neutral moderation
            "only_valid_faction_id": True,
            "without_faction": None,
            # "change_faction": ["3", "7"], # swap BSW to Die Linke
            "generate_contributions_data": False,

            # Core text normalization
            "contributions": "INSERT",
            "to_lower": True,
            "remove_digits": True,
            "remove_punctuation": True,
            "stopword_mode": "SPACY",
            "custom_stopwords": DOMAIN_SPECIFIC_STOPWORDS_CLASSIFICATION_1,
            "phrase_patterns": PHRASE_PATTERNS_CLASSIFICATION_3,

            # Optional NLP metrics
            "lemmatization": True,
            "stemming": True,
            "tokenization_method": "SPACY",
            "add_char_count": True,
            "add_token_count": True,
            "add_lemma_count": True,

            "log_prefix": f"[data_set_1, Term {term}]"
        }
        # Additional configs can be added as needed...
    }
    dataset_configs.update(dataset_configs_curr_term)


# parallel execution
if __name__ == "__main__":
    ensure_required_nlp_resources()
    execute_parallel_preprocessing(dataset_configs)
"""
