# imports
from dataPreprocessingHelpers.phrase_patterns import PHRASE_PATTERNS_CLASSIFICATION_3
from dataPreprocessingHelpers.domain_stopwords import DOMAIN_SPECIFIC_STOPWORDS_CLASSIFICATION_1
from pathlib import Path
from dataPreprocessingHelpers.preprocessing_pipeline import execute_parallel_preprocessing
from dataPreprocessingHelpers.preprocessing_pipeline import ensure_required_nlp_resources
from dataPreprocessingHelpers.preprocessing_pipeline import combine_two_datasets

"""
Dataset configuration for ML-Task 1 (Party Classification) using parallel processing.
This script defines various preprocessing configurations which are than used to generate 
multiple slightly different datasets with the execute_parallel_preprocessing function of preprocessing_pipeline.py:

| Dataset name | Details               | Lowercase | Remove digits | Remove punctuation | Stopword removal | Domain specific stopword removal | Phrase pattern removal | Contribution Mode |
|--------------|-----------------------|-----------|---------------|--------------------|------------------|----------------------------------|------------------------|-------------------|
| data_set_1   | Extreme normalization | Yes       | Yes           | Yes                | Yes              | Yes                              | Yes                    | REMOVE            |
| data_set_2   | Middle ground         | Yes       | Yes           | Yes                | Yes              | No                               | No                     | REMOVE            |
| data_set_3   | Minimal normalization | Yes       | No            | No                 | No               | No                               | No                     | INSERT            |
| data_set_4   | BERT                  | No        | Yes           | Yes                | Yes              | Yes                              | Yes                    | REMOVE            |
| data_set_5   | BERT                  | No        | No            | No                 | Yes              | No                               | No                     | INSERT            |
| data_set_6   | LSTM                  | Yes       | No            | No                 | Yes              | No                               | No                     | INSERT            |
| data_set_7   | BERT                  | No        | No            | No                 | No               | No                               | No                     | INSERT            |
| data_set_8   | LSTM                  | Yes       | No            | No                 | No               | No                               | Yes                    | REMOVE            |
| data_set_9   | BERT                  | No        | No            | No                 | No               | No                               | Yes                    | REMOVE            |

Every Dataset will be generated for electoral term 19, 20 and 19_20 combined.

:dependencies: preprocessing_pipeline.py (functions: combine_two_datasets, execute_parallel_preprocessing, ensure_required_nlp_resources)
:dependencies: domain_stopwords.py (e.g., DOMAIN_SPECIFIC_STOPWORDS_CLASSIFICATION_1)
:dependencies: phrase_patterns.py (e.g., PHRASE_PATTERNS_CLASSIFICATION_3)

:raises: look in preprocessing_pipeline.py

:params: input:
    dataFinalStage/
    ├── speechContentFinalStage/
    │   ├── speech_content_19.pkl
    │   └── speech_content_20.pkl

:return: output:
    dataPreprocessedStage/
    ├── dataClassification/
    │   ├── dataSets/
    │   │   ├── data_set_<1-9>_19_20.xlsx
    │   │   ├── data_set_<1-9>_19.xlsx
    │   │   ├── data_set_<1-9>_20.xlsx
    │   │   ├── data_set_<1-9>_19_20.pkl
    │   │   ├── data_set_<1-9>_19.pkl
    │   │   └── data_set_<1-9>_20.pkl

columns (data_set_X_Y.pkl):
    | Column name                 | Description                                                      |
    | --------------------------- | ---------------------------------------------------------------- |
    | `id`                        | Speech ID                                                        |
    | `speech_content`            | Original full speech text                                        |
    | `speech_content_cleaned`    | Normalized text (case, digits, punctuation, phrases)             |
    | `speech_content_stopword`   | After stopword removal (if enabled)                              |
    | `speech_content_lemmatized` | After lemmatization (if enabled)                                 |
    | `speech_content_stemmed`    | After stemming (if enabled)                                      |
    | `speech_content_tokenized`  | List of tokens (if tokenization enabled)                         |
    | `speech_length_chars`       | Character count of cleaned text                                  |
    | `speech_length_lemmas`      | Lemma count                                                      |
    | `speech_length_tokens`      | Token count                                                      |
    | …                           | Original columns like `faction_id`, `politician_id`, etc. remain |
"""

# terms to process
terms = [19, 20]

# configuration dictionary for each dataset
dataset_configs = {}

# generate dataset configs
for term in terms:
    dataset_configs_curr_term = {
        # data set 1: full cleaning, domain specific spacy stopword removal, phrase pattern removal, contribution removal
        f"data_set_1, term: {term}": {
            "input_path":Path(f"dataFinalStage/speechContentFinalStage/speech_content_{term}.pkl"),
            "output_path_pickle": Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_1_{term}.pkl"),
            "output_path_excel":Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_1_{term}.xlsx"),

            # Optional filters (deactivated here)
            "position_short": ["Presidium of Parliament", "Guest"],  # removes presidium/neutral moderation
            "only_valid_faction_id": True,
            "without_faction": None,
            # "change_faction": ["3", "7"], # swap BSW to Die Linke
            "generate_contributions_data": False,

            # Core text normalization
            "contributions": "REMOVE",
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
        },

        # data set 2: full cleaning, spacy stopword removal, phrase pattern removal, contribution removal
        f"data_set_2, term: {term}": {
            "input_path":Path(f"dataFinalStage/speechContentFinalStage/speech_content_{term}.pkl"),
            "output_path_pickle": Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_2_{term}.pkl"),
            "output_path_excel":Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_2_{term}.xlsx"),

            # Optional filters (deactivated here)
            "position_short": ["Presidium of Parliament", "Guest"],  # removes presidium/neutral moderation
            "only_valid_faction_id": True,
            "without_faction": None,
            # "change_faction": ["3", "7"], # swap BSW to Die Linke
            "generate_contributions_data": False,

            # Core text normalization
            "contributions": "REMOVE",
            "to_lower": True,
            "remove_digits": True,
            "remove_punctuation": True,
            "stopword_mode": "SPACY",
            # "custom_stopwords": DOMAIN_SPECIFIC_STOPWORDS_CLASSIFICATION_1,
            "phrase_patterns": PHRASE_PATTERNS_CLASSIFICATION_3,

            # Optional NLP metrics
            "lemmatization": True,
            "stemming": True,
            "tokenization_method": "SPACY",
            "add_char_count": True,
            "add_token_count": True,
            "add_lemma_count": True,

            "log_prefix": f"[data_set_2, Term {term}]"
        },

        # data set 3: cleaning (lowercase), contributions insert
        f"data_set_3, term: {term}": {
            "input_path":Path(f"dataFinalStage/speechContentFinalStage/speech_content_{term}.pkl"),
            "output_path_pickle": Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_3_{term}.pkl"),
            "output_path_excel":Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_3_{term}.xlsx"),

            # Optional filters (deactivated here)
            "position_short": ["Presidium of Parliament", "Guest"],  # removes presidium/neutral moderation
            "only_valid_faction_id": True,
            "without_faction": None,
            # "change_faction": ["3", "7"], # swap BSW to Die Linke
            "generate_contributions_data": False,

            # Core text normalization
            "contributions": "INSERT",
            "to_lower": True,
            #"remove_digits": True,
            #"remove_punctuation": True,
            #"stopword_mode": "SPACY",
            # "custom_stopwords": DOMAIN_SPECIFIC_STOPWORDS_CLASSIFICATION_1,
            # "phrase_patterns": PHRASE_PATTERNS_CLASSIFICATION_3,

            # Optional NLP metrics
            "lemmatization": True,
            "stemming": True,
            "tokenization_method": "SPACY",
            "add_char_count": True,
            "add_token_count": True,
            "add_lemma_count": True,

            "log_prefix": f"[data_set_3, Term {term}]"
        },

        # data set 4: cleaning (remove numbers, remove punctuation), domain specific spacy stopword removal, phrase pattern removal, contribution removal
        f"data_set_4, term: {term}": {
            "input_path":Path(f"dataFinalStage/speechContentFinalStage/speech_content_{term}.pkl"),
            "output_path_pickle": Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_4_{term}.pkl"),
            "output_path_excel":Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_4_{term}.xlsx"),

            # Optional filters (deactivated here)
            "position_short": ["Presidium of Parliament", "Guest"],  # removes presidium/neutral moderation
            "only_valid_faction_id": True,
            "without_faction": None,
            # "change_faction": ["3", "7"], # swap BSW to Die Linke
            "generate_contributions_data": False,

            # Core text normalization
            "contributions": "REMOVE",
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

            "log_prefix": f"[data_set_4, Term {term}]"
        },

        # data set 5: no cleaning, Spacy stopword removal, insert contributions
        f"data_set_5, term: {term}": {
            "input_path":Path(f"dataFinalStage/speechContentFinalStage/speech_content_{term}.pkl"),
            "output_path_pickle":Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_5_{term}.pkl"),
            "output_path_excel":Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_5_{term}.xlsx"),

            # Optional filters (deactivated here)
            "position_short": ["Presidium of Parliament", "Guest"],  # removes presidium/neutral moderation
            "only_valid_faction_id": True,
            "without_faction": None,
            # "change_faction": ["3", "7"], # swap BSW to Die Linke
            "generate_contributions_data": False,

            # Core text normalization
            "contributions": "INSERT",
            #"to_lower": True,
            #"remove_digits": True,
            #"remove_punctuation": True,
            "stopword_mode": "SPACY",
            # "custom_stopwords": DOMAIN_SPECIFIC_STOPWORDS_CLASSIFICATION_1,
            # "phrase_patterns": PHRASE_PATTERNS_CLASSIFICATION_3,

            # Optional NLP metrics
            "lemmatization": True,
            "stemming": True,
            "tokenization_method": "SPACY",
            "add_char_count": True,
            "add_token_count": True,
            "add_lemma_count": True,

            "log_prefix": f"[data_set_5, Term {term}]"
        },

        # data set 6: cleaning (lower case), spacy stop word removal, insert contributions
        f"data_set_6, term: {term}": {
            "input_path":Path(f"dataFinalStage/speechContentFinalStage/speech_content_{term}.pkl"),
            "output_path_pickle":Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_6_{term}.pkl"),
            "output_path_excel":Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_6_{term}.xlsx"),

            # Optional filters (deactivated here)
            "position_short": ["Presidium of Parliament", "Guest"],  # removes presidium/neutral moderation
            "only_valid_faction_id": True,
            "without_faction": None,
            # "change_faction": ["3", "7"], # swap BSW to Die Linke
            "generate_contributions_data": False,

            # Core text normalization
            "contributions": "INSERT",
            "to_lower": True,
            # "remove_digits": True,
            # "remove_punctuation": True,
            "stopword_mode": "SPACY",
            # "custom_stopwords": DOMAIN_SPECIFIC_STOPWORDS_CLASSIFICATION_1,
            # "phrase_patterns": PHRASE_PATTERNS_CLASSIFICATION_3,

            # Optional NLP metrics
            "lemmatization": True,
            "stemming": True,
            "tokenization_method": "SPACY",
            "add_char_count": True,
            "add_token_count": True,
            "add_lemma_count": True,

            "log_prefix": f"[data_set_6, Term {term}]"
        },

        # data set 7: no cleaning, insert contributions
        f"data_set_7, term: {term}": {
            "input_path":Path(f"dataFinalStage/speechContentFinalStage/speech_content_{term}.pkl"),
            "output_path_pickle":Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_7_{term}.pkl"),
            "output_path_excel":Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_7_{term}.xlsx"),

            # Optional filters (deactivated here)
            "position_short": ["Presidium of Parliament", "Guest"],  # removes presidium/neutral moderation
            "only_valid_faction_id": True,
            "without_faction": None,
            # "change_faction": ["3", "7"], # swap BSW to Die Linke
            "generate_contributions_data": False,

            # Core text normalization
            "contributions": "INSERT",
            # "to_lower": True,
            # "remove_digits": True,
            # "remove_punctuation": True,
            # "stopword_mode": "SPACY",
            # "custom_stopwords": DOMAIN_SPECIFIC_STOPWORDS_CLASSIFICATION_1,
            # "phrase_patterns": PHRASE_PATTERNS_CLASSIFICATION_3,

            # Optional NLP metrics
            "lemmatization": True,
            "stemming": True,
            "tokenization_method": "SPACY",
            "add_char_count": True,
            "add_token_count": True,
            "add_lemma_count": True,

            "log_prefix": f"[data_set_7, Term {term}]"
        },

        # data set 8: cleaning (lowercase), phrase based removal, remove contributions
        f"data_set_8, term: {term}": {
            "input_path": Path(f"dataFinalStage/speechContentFinalStage/speech_content_{term}.pkl"),
            "output_path_pickle": Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_8_{term}.pkl"),
            "output_path_excel": Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_8_{term}.xlsx"),

            # Optional filters (deactivated here)
            "position_short": ["Presidium of Parliament", "Guest"],  # removes presidium/neutral moderation
            "only_valid_faction_id": True,
            "without_faction": None,
            # "change_faction": ["3", "7"],  # swap BSW to Die Linke
            "generate_contributions_data": False,

            # Core text normalization
            "contributions": "REMOVE",
            "to_lower": True,
            # "remove_digits": True,
            # "remove_punctuation": True,
            # "stopword_mode": "SPACY",
            # "custom_stopwords": DOMAIN_SPECIFIC_STOPWORDS_CLASSIFICATION_1,
            "phrase_patterns": PHRASE_PATTERNS_CLASSIFICATION_3,

            # Optional NLP metrics
            "lemmatization": True,
            "stemming": True,
            "tokenization_method": "SPACY",
            "add_char_count": True,
            "add_token_count": True,
            "add_lemma_count": True,

            "log_prefix": f"[data_set_8, Term {term}]"
        },

        # data set 9: cleaning (lowercase), phrase based removal, remove contributions
        f"data_set_9, term: {term}": {
            "input_path": Path(f"dataFinalStage/speechContentFinalStage/speech_content_{term}.pkl"),
            "output_path_pickle": Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_9_{term}.pkl"),
            "output_path_excel": Path(f"dataPreprocessedStage/dataClassification/dataSets/data_set_9_{term}.xlsx"),

            # Optional filters (deactivated here)
            "position_short": ["Presidium of Parliament", "Guest"],  # removes presidium/neutral moderation
            "only_valid_faction_id": True,
            "without_faction": None,
            # "change_faction": ["3", "7"],  # swap BSW to Die Linke
            "generate_contributions_data": False,

            # Core text normalization
            "contributions": "REMOVE",
            # "to_lower": True,
            # "remove_digits": True,
            # "remove_punctuation": True,
            # "stopword_mode": "SPACY",
            # "custom_stopwords": DOMAIN_SPECIFIC_STOPWORDS_CLASSIFICATION_1,
            "phrase_patterns": PHRASE_PATTERNS_CLASSIFICATION_3,

            # Optional NLP metrics
            "lemmatization": True,
            "stemming": True,
            "tokenization_method": "SPACY",
            "add_char_count": True,
            "add_token_count": True,
            "add_lemma_count": True,

            "log_prefix": f"[data_set_9, Term {term}]"
        }

        # more datasets can be added as needed ...
    }

    dataset_configs.update(dataset_configs_curr_term)

# parallel execution
if __name__ == "__main__":
    ensure_required_nlp_resources()
    execute_parallel_preprocessing(dataset_configs)

    # datasets
    data_set_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]

    # combination processing loop
    for num in data_set_numbers:
        # setup input path variables
        input_path_19 = f"dataPreprocessedStage/dataClassification/dataSets/data_set_{num}_19.pkl"
        input_path_20 = f"dataPreprocessedStage/dataClassification/dataSets/data_set_{num}_20.pkl"

        # setup output path variable
        output_path_19_20 = f"dataPreprocessedStage/dataClassification/dataSets/data_set_{num}_19_20.pkl"

        # combine datasets
        combine_two_datasets(input_path_a=input_path_19, input_path_b=input_path_20, output_path=output_path_19_20)


