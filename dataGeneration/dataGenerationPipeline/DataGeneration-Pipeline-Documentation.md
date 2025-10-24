# **Data Generation Pipeline**

This notebook executes the full data generation pipeline that builds a structured, speaker-linked dataset from raw plenary session documents of the German Bundestag. It downloads, parses, normalizes, and enriches metadata from various sources including XML, JSON, and official politician registries. The pipeline extracts both speeches and audience contributions, links them to politicians and parties, and outputs clean, well-structured Pickle and Excel datasets. These outputs form the foundation for all subsequent NLP and machine learning tasks in this project.
The pipeline logic and structure are based on the [open-discourse project](https://github.com/open-discourse/open-discourse/tree/main), which we discovered during initial research for the project.


---


## **Resulting File Structure:**

```
team-16/
├── dataGeneration/
│   ├── dataGeneratorPipeline.ipynb  # YOU ARE HERE!
│   ├── paths.py
│   ├── dataGenerator_Clean_Text.py
│   ├── dataGenerator_Extract_Contributions.py
│   ├── dataGenerator_Match_Names.py
│   └── bundestagsapi/
data/
├── dataGeneration/
│   ├── rawData/
│   │   ├── electoralTerms/
│   │   │   └── electoralTerms.csv
│   │   ├── politiciansRawData/
│   │   │   ├── MDB_STAMMDATEN.XML
│   │   │   ├── MDB_STAMMDATEN.DTD
│   │   │   └── mgs.pkl
│   │   ├── rawData19json/
│   │   │   ├── protokoll_<Nr.>.json
│   │   │   └── …
│   │   ├── rawData20json/
│   │   │   ├── protokoll_<Nr.>.json
│   │   │   └── …
│   │   ├── rawData19pdf/
│   │   ├── rawData20pdf/
│   │   ├── rawData19xml/
│   │   │   ├── 19001.xml
│   │   │   └── …
│   │   ├── rawData20xml/
│   │   │   ├── 20001.xml
│   │   │   └── …
│   │   │
│   │   dataStage02/
│   │   ├── data19xmlSplit/
│   │   │   ├── 19001/
│   │   │   │   ├── appendix.xml
│   │   │   │   ├── meta_data.xml
│   │   │   │   ├── toc.xml
│   │   │   │   └── session_content.xml
│   │   │   ├── 19002/ …
│   │   │   └── …
│   │   ├── data20xmlSplit/
│   │   │   ├── 20001/
│   │   │   │   ├── appendix.xml
│   │   │   │   ├── meta_data.xml
│   │   │   │   ├── toc.xml
│   │   │   │   └── session_content.xml
│   │   │   ├── 20002/ …
│   │   │   └── …
│   │   ├── dataFactionsStage02/
│   │   │   └── factions.pkl
│   │   ├── dataPoliticiansStage02/
│   │   │   └── mps.pkl
│   │   │
│   │   dataStage03/
│   │   ├── dataFactionsStage03/
│   │   │   └── factionsAbbreviations.pkl
│   │   ├── dataPoliticiansStage03/
│   │   │   ├── mpsFactions.pkl
│   │   │   ├── politicians.csv
│   │   │   └── speaker_faction_lookup.csv
│   │   │
│   │   dataStage04/
│   │   ├── contributionsExtended/
│   │   │   ├── electoral_term_19/
│   │   │   │   ├── 19001.pkl
│   │   │   │   └── …
│   │   │   ├── electoral_term_20/
│   │   │   │   ├── 20001.pkl
│   │   │   │   └── …
│   │   ├── contributionsSimplified/
│   │   │   ├── contributions_simplified_19.pkl
│   │   │   ├── contributions_simplified_20.pkl
│   │   │   └── contributions_simplified_19_20.pkl
│   │   ├── speechContent/
│   │   │   ├── electoral_term_19/
│   │   │   │   └── speech_content.pkl
│   │   │   ├── electoral_term_20/
│   │   │   │   └── speech_content.pkl
│   │   │
│   │   dataStage05/
│   │   ├── contributionsExtendedStage05/
│   │   │   ├── electoral_term_19/
│   │   │   │   ├── 19001.pkl
│   │   │   │   └── …
│   │   │   ├── electoral_term_20/
│   │   │   │   ├── 20001.pkl
│   │   │   │   └── …
│   │   │
│   │   dataStage06/
│   │   ├── contributionsExtendedStage06/
│   │   │   ├── electoral_term_19/
│   │   │   │   ├── 19001.pkl
│   │   │   │   └── …
│   │   │   ├── electoral_term_20/
│   │   │   │   ├── 20001.pkl
│   │   │   │   └── …
│   │
├── dataFinalStage/
│   ├── contributionsExtendedFinalStage/
│   │   ├── contributions_extended_19_20.pkl
│   │   ├── contributions_extended_19.pkl
│   │   └── contributions_extended_20.pkl
│   ├── contributionsSimplifiedFinalStage/
│   │   ├── contributions_simplified_19.pkl
│   │   ├── contributions_simplified_20.pkl
│   │   └── contributions_simplified_19_20.pkl
│   ├── speechContentFinalStage/
│   │   ├── speech_content_19_20.pkl
│   │   ├── speech_content_19.pkl
│   │   └── speech_content_20.pkl
│   └── factionsAbbreviations.pkl
├── dataExcel/
│   ├── finalStage/
│   │   ├── contributions_extended_19_20_finalStage.xlsx
│   │   ├── contributions_extended_19_finalStage.xlsx
│   │   ├── contributions_extended_20_finalStage.xlsx
│   │   ├── contributions_simplified_19_20_finalStage.xlsx
│   │   ├── contributions_simplified_19_finalStage.xlsx
│   │   ├── contributions_simplified_20_finalStage.xlsx
│   │   ├── speech_content_19_20_finalStage.xlsx
│   │   ├── speech_content_19_finalStage.xlsx
│   │   ├── speech_content_20_finalStage.xlsx
│   │   └── factionsAbbreviations.xlsx
│   ├── dataGeneration/
│   │   ├── mgs_wiki_rawData.xlsx
│   │   ├── mps_stage02.xlsx
│   │   ├── mpsFactions_stage03.xlsx
│   │   ├── politicians_stage03.xlsx
│   │   ├── speech_content_19_stage04.xlsx
│   │   ├── speech_content_20_stage04.xlsx
│   │   └── factions_stage02.xlsx
```

# **0 Data Generation Pipeline Setup**

## **0.1 Setup Environment for Project**

## **0.2 Imports**

Import via requirements.txt.

## **0.3 Read Json Files from API into Python Process**

**The following datastructure needs to exist in the enclosing folder of this notebook for the pipeline to work:**
```
rawData/
├── rawData19json/
│   ├── protokoll_<Nr.>.json
│   └── …
├── rawData20json/
│   ├── protokoll_<Nr.>.json
│   └── …
```
It can be generated via [LoadProtocols.java](dataGeneration/bundestagsapi/src/main/java/LoadProtocols.java) in the bundestagsapi.

# **1 Download raw data**

## **1.1 Download Plenary Protocols (.pdf & .xml) for Electoral Terms 19 and 20**
- Fetches the PDF and XML files of all plenary protocols for the 19th and 20th electoral periods.
- The files are retrieved by reading the corresponding .json files (which were previously downloaded via the bundestagsapi) and following the pdf_url and xml_url links contained in each.
- Downloaded files are stored separately by format and electoral period.
- This module ensures that all raw protocol documents are available locally in structured form. These files serve as the primary source for downstream parsing and processing steps.

### **Input:**
```
rawData/
├── rawData19json/
│   ├── protokoll_<Nr.>.json
│   └── …
├── rawData20json/
│   ├── protokoll_<Nr.>.json
│   └── …
```

### **Output:**
```
rawData/
├── rawData19pdf/
├── rawData20pdf/
├── rawData19xml/
│   ├── 19001.xml
│   └── …
├── rawData20xml/
│   ├── 20001.xml
│   └── …
```

## **1.2 Download Metadata of All Members of the Bundestag (MdB)**
Downloads and extracts a ZIP archive containing structured information (as a XML file) for all members of the German Bundestag from the 1st to the 20th electoral period. The files are provided by the Bundestag via the following URL:
    https://www.bundestag.de/resource/blob/472878/7d4d417dbb7f7bd44508b3dc5de08ae2/MdB-Stammdaten-data.zip

### **Input:**
```
None.
```

### **Output:**
```
rawData/
├── politiciansRawData/
│   ├── MDB_STAMMDATEN.XML
│   └── MDB_STAMMDATEN.DTD
```

## **1.3 Split Plenary Protocol XML Files into Structural Components**

This script processes raw plenary protocol XML files and splits each file into 4 logically separated XML documents:
- toc.xml: Table of contents (XML-tag: vorspann)
- session_content.xml: Speech content (XML-tag: sitzungsverlauf)
- appendix.xml: Appendices such as voting results or exhibits (XML-tag: anlagen)
- meta_data.xml: Metadata on speakers (XML-tag: rednerliste)

### **Input:**
```
rawData/
├── rawData19xml/*.xml
│   ├── 19001.xml
│   └── …
├── rawData20xml/*.xml
│   ├── 20001.xml
│   └── …
```

### **Ouput:**
```
dataStage02/
├── data19xmlSplit/
│   ├── 19001/
│   │   ├── appendix.xml
│   │   ├── meta_data.xml
│   │   ├── toc.xml
│   │   └── session_content.xml
│   ├── 19002/ …
│   └── …
├── data20xmlSplit/
│   ├── 20001/
│   │   ├── appendix.xml
│   │   ├── meta_data.xml
│   │   ├── toc.xml
│   │   └── session_content.xml
│   ├── 20002/ …
│   └── …
```

## **1.4 Extract MP Metadata from MP-Base-Data**

Extracts biographical and institutional metadata for all members of the Bundestag from MDB_STAMMDATEN.xml.

- **Each MP may get multiple entries depending on:**
    - Name changes over time
    - Multiple institutional affiliations (e.g., Bundestag and government office)
    - Participation across multiple electoral terms
- **The extracted data includes:**
    - Biographical information: name, gender, profession, birth/death details
    - Metadata: academic titles, aristocratic prefixes
    - Electoral data: constituency, institution type (e.g. “Regierungsmitglied”)


### **Input:**
```
rawData/
├── politiciansRawData/
│   └── MDB_STAMMDATEN.XML
```

### **Ouput:**
```
dataStage02/
├── dataPoliticiansStage02/
│   └── mps.pkl
dataExcel/
└── mps_stage02.xlsx
```


**Columns (mps.pkl):**
| Column name       | Description                                                   |
|------------------|---------------------------------------------------------------|
| `ui`              | Unique politician identifier                                  |
| `electoral_term`  | Electoral term in which the entry applies                     |
| `first_name`      | First name(s) of the MP                                        |
| `last_name`       | Last name of the MP                                           |
| `birth_place`     | Place of birth                                                |
| `birth_country`   | Country of birth                                              |
| `birth_date`      | Date of birth                                                 |
| `death_date`      | Date of death (or -1 if not applicable)                       |
| `gender`          | Gender                                                        |
| `profession`      | Profession                                                    |
| `constituency`    | Electoral district (constituency)                             |
| `aristocracy`     | Aristocratic title (e.g., Freiherr)                           |
| `academic_title`  | Academic title (e.g., Dr., Prof.)                             |
| `institution_type`| Type of institution (e.g., Fraktion/Gruppe, Regierungsmitglied)|
| `institution_name`| Full name of the institution affiliation                      |

## **1.5 Generate Electoral Terms Reference Table**

Creates a CSV reference table listing all electoral terms from 1949 (1st term) to the current term (20th) and assigns each term:
- a unique ID (1-based),
- a start and end date (in seconds since the Unix epoch).

The table can later be used to match speech or politician timestamps to the correct legislative period.


### **Input:**
```
None.
```

### **Ouput:**
```
rawData/
├── electoralTerms/
│   └── electoralTerms.csv
```


**Columns (electoralTerms.csv):**
| Column name | Description                              |
|-------------|------------------------------------------|
| `start_date`| Start of the electoral term (in seconds) |
| `end_date`  | End of the electoral term (in seconds)   |
| `id`        | Unique ID for the electoral term         |

# **2 Factions:**

## **2.1 Extract & Normalize Factions from MP Metadata**

- Extracts a unique list of factions from the structured MP dataset (mps.pkl), which are officially listed as institutional affiliations for MPs in the Bundestag.
- Since some faction names appear in speech data but not in the structured MP data (e.g. historical or special cases), this script manually appends missing entries to the list of known factions to ensure consistency in downstream data processing.



### **Input:**
```
dataStage02/
├── dataPoliticiansStage02/
│   └── mps.pkl
```

### **Ouput:**
```
dataStage02
├── dataFactionsStage02/
│   └── factions.pkl
dataExcel/
└── factions_stage02.xlsx
```


**Columns (factions.pkl):**
| Column name    | Description                                     |
|----------------|-------------------------------------------------|
| `faction_name` | Full name of the faction or parliamentary group |

## **2.2 Add abbreviations to factions**

Augments the previously extracted list of faction names by
- assigning standardized abbreviations to each entry
- and then assigning a unique integer id to each abbreviation
- before outputting as a structured table.


### **Input:**
```
dataStage02
├── dataFactionsStage02/
│   └── factions.pkl
```

### **Ouput:**
```
dataStage03/
├── dataFactionsStage03/
│   └── factionsAbbreviations.pkl
dataExcel/
└── factionsAbbreviations_stage03.xlsx
```


**Columns (factionsAbbreviations.pkl):**
| Column name     | Description                                        |
|-----------------|----------------------------------------------------|
| `id`            | Unique numeric identifier for each faction         |
| `abbreviation`  | Shortened, normalized faction label (e.g., "SPD")  |
| `faction_name`  | Original full name of the faction                  |

# **3 Politicians**

## **3.1 Add unique Faction IDs to MPs**

Assigns a normalized faction ID to each member of parliament (MP) based on their associated faction name. The normalized mapping was created in the previous step (2.2). The result is a consistent representation of faction membership for every politician across all electoral terms.

The script:
- Loads the list of MPs (mps.pkl) and normalized faction data (factionsAbbreviations.pkl)
- Adds a new column faction_id to the MP DataFrame
- Assigns the appropriate ID by matching the original institution_name with the normalized faction_name
- Outputs the enriched MP data with faction references


### **Input:**
```
dataStage02/
├── dataPoliticiansStage02/
│   └── mps.pkl
dataStage03/
├── dataFactionsStage03/
│   └── factionsAbbreviations.pkl
```

### **Ouput:**
```
dataStage03
├── dataPoliticiansStage03/
│   ├── mpsFactions.pkl
dataExcel/
└── mpsFactions_stage03.xlsx
```


**Columns (mpsFactions.pkl):**
| Column name       | Description                                                      |
|-------------------|------------------------------------------------------------------|
| `ui`              | Unique ID for the politician                                     |
| `electoral_term`  | Electoral term number                                            |
| `faction_id`      | Integer ID of matched faction (from `factionsAbbreviations.pkl`) |
| `first_name`      | First name(s) of the MP                                          |
| `last_name`       | Last name of the MP                                              |
| `birth_place`     | Place of birth                                                   |
| `birth_country`   | Country of birth                                                 |
| `birth_date`      | Date of birth (as string)                                        |
| `death_date`      | Date of death (or -1 if unknown)                                 |
| `gender`          | Gender                                                           |
| `profession`      | Profession                                                       |
| `constituency`    | Additional location info                                         |
| `aristocracy`     | Nobility title (if any)                                          |
| `academic_title`  | Academic title (e.g. Dr., Prof.)                                 |
| `institution_type`| Type of institution (e.g. "Fraktion/Gruppe")                     |
| `institution_name`| Name of the institution (used for faction matching)              |

## **3.2 Scrape Government Membership Data from Wikipedia**


- Extracts structured data on German government members for all cabinets since 1949 from Wikipedia: https://de.wikipedia.org/wiki/Liste_der_deutschen_Regierungsmitglieder_seit_1949.
- This dataset complements the MP data by adding government-specific roles such as Ministers and Secretaries of State.


### **Input:**
```
None.
```

### **Ouput:**
```
rawData/
├── politiciansRawData/
│   └── mgs.pkl
dataExcel/
└── mgs_wiki_rawData.xlsx
```


**Columns (mgs.pkl):**
| Column name        | Description                                                   |
|--------------------|---------------------------------------------------------------|
| `ui`               | Unique ID assigned by the script (e.g. "gov_123")             |
| `last_name`        | Last name of the politician                                   |
| `first_name`       | First name(s) (stored as list)                                |
| `position`         | Government position held (e.g., "Bundeskanzler")              |
| `position_from`    | Year the office began                                         |
| `position_until`   | Year the office ended (or -1 if open-ended)                   |
| `birth_date`       | Year of birth                                                 |
| `death_date`       | Year of death or -1 if still alive                            |
| `faction`          | Main political affiliation (e.g., "CDU", "SPD", "parteilos")  |
| `additional_faction` | Additional party affiliation (e.g., coalition)              |

## **3.3 Merge Parliament and Government Members**

Merges the dataset of MPs mpsFactions.pkl with the dataset of MGs mgs.pkl into a unified dataframe politicians.csv that includes all individuals with legislative or executive roles in the Bundestag:
- **For each government member:**
    - The algorithm attempts to match by last name, first name, and birth date.
    - If a match is found in the MP dataset, the government position (e.g. Minister, Chancellor) is appended to that MP across all electoral terms the position covers.
    - If no match is found, a new entry with a generated ui (unique identifier) is created manually.
    - The electoral term(s) are inferred from the time period of the government position using a mapping table of legislative periods.
- **The output:**
    - Contains full biographical and role-specific information
    - Covers all electoral periods from 1 to 20


### **Input:**
```
rawData/
├── politiciansRawData/
│   └── mgs.pkl
dataStage03/
├── dataPoliticiansStage03/
│   ├── mpsFactions.pkl
├── dataFactionsStage03/
│   └── factionsAbbreviations.pkl
```

### **Ouput:**
```
dataStage03/
├── dataPoliticiansStage03/
│   └── politicians.csv
dataExcel/
└── politicians_stage03.xlsx
```


**Columns (politicians.csv):**
| Column name       | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `ui`              | Unique identifier (integer)                                                 |
| `electoral_term`  | Electoral period (1-based index from 1949)                                  |
| `faction_id`      | Normalized integer ID of party affiliation (linked to faction lookup table) |
| `first_name`      | First name of the person (as string or joined from list)                    |
| `last_name`       | Last name of the person                                                     |
| `birth_place`     | Place of birth (may be empty)                                               |
| `birth_country`   | Country of birth (default: "Deutschland")                                   |
| `birth_date`      | Year of birth (as string)                                                   |
| `death_date`      | Year of death (or "-1" if still alive)                                      |
| `gender`          | Gender ("m" / "w")                                                           |
| `profession`      | Stated profession                                                           |
| `constituency`    | Place of political representation                                           |
| `aristocracy`     | Aristocratic prefix (e.g., "von", "Freiherr")                               |
| `academic_title`  | Academic title (e.g., "Dr.")                                                |
| `institution_type`| Type of institution (e.g., "Fraktion/Gruppe", "Regierungsmitglied")         |
| `institution_name`| Name of institution or office held

## **3.4 Create Speaker-to-Faction Lookup Table**


Creates a lookup table mapping each speaker (by speaker_id) and electoral term to their most recent valid faction (faction_id). This is necessary for resolving speaker affiliations in cases where the original speech data does not contain accurate or complete faction information.
- **Process overview:**
    - Iterates over all combinations of speaker_id (ui) and electoral_term.
    - For each group, scans the politician records in reverse order to find the last valid (≠ -1) faction ID.
    - If a valid faction is found, adds a row to the lookup table with: speaker_id, electoral_term, faction_id
- **This lookup table can later be used to:**
    - Fill in missing faction IDs in speech datasets
    - Support faction-based analyses when direct affiliation is missing or ambiguous


### **Input:**
```
dataStage03/
├── dataPoliticiansStage03/
│   └── politicians.csv
```

### **Ouput:**
```
dataStage03/
├── dataPoliticiansStage03/
│   └── speaker_faction_lookup.csv
```


**Columns (speaker_faction_lookup.csv):**
| Column name      | Description                                             |
|------------------|---------------------------------------------------------|
| `speaker_id`     | Unique ID of the speaker (`ui` from `politicians.csv`) |
| `electoral_term` | Electoral period ID (integer)                          |
| `faction_id`     | Final party ID assigned in that term                   |

# **4 Spoken Content**

## **4.1 Extract structured Speeches and Contributions from XML (Term 19 and 20)**

**1. Speech Extraction:** Each session_content.xml file is parsed to extract speeches (rede), including speaker metadata such as:
- first_name, last_name
- position (e.g., Minister, MP, Guest)
- politician_id (from MDB data or speaker_faction_lookup)
- faction_id (determined from fraktion tag or fallback lookup)

**2. Contribution Extraction:** Embedded commentary tags (kommentar) in the speech content are parsed using a regex-based extraction function:
- Contributions are isolated, tokenized, and classified.
- Here an external extraction function extract(…) is used: it can be found in [extract_contributions.py](dataGeneration/extract_contributions.py).
- They are replaced in the speech content with a placeholder.
- Metadata for each contribution is stored separately.

This parser-step is central to transforming raw XML session data into:
- Clean structured speech datasets suitable for NLP tasks
- Detailed speaker-level contributions with speaker and faction alignment

Internal Highlights:
- Position Handling: Robust mapping of fraktion and rolle tags to standard position categories.
- Speaker Disambiguation: Matching via speaker_id or fuzzy name search using first_name and last_name.
- Date Handling: Converts sitzung-datum to Unix time.
- Failsafes: Manual correction for broken XML dates (e.g., session 19158).


### **Input:**
```
dataStage02/
├── data19xmlSplit/
│   ├── 19001/
│   │   ├── appendix.xml
│   │   ├── meta_data.xml
│   │   ├── toc.xml
│   │   └── session_content.xml
│   ├── 19002/ …
│   └── …
├── data20xmlSplit/
│   ├── 20001/
│   │   ├── appendix.xml
│   │   ├── meta_data.xml
│   │   ├── toc.xml
│   │   └── session_content.xml
│   ├── 20002/ …
│   └── …
dataStage03/
├── dataPoliticiansStage03/
│   ├── politicians.csv
├── dataFactionsStage03/
│   ├── factionsAbbreviations.pkl
│   └── speaker_faction_lookup.csv
```

### **Ouput:**
```
dataStage04/
├── contributionsExtended/
│   ├── electoral_term_19/
│   │   ├── 19001.pkl
│   │   └── …
│   ├── electoral_term_20/
│   │   ├── 20001.pkl
│   │   └── …
├── contributionsSimplified/
│   ├── electoral_term_19/
│   │   └── contributions_simplified.pkl
├── speechContent/
│   ├── electoral_term_19/
│   │   └── speech_content.pkl
│   ├── electoral_term_20/
│   │   └── speech_content.pkl
dataExcel/
│   ├── speech_content_19_stage04.xlsx
│   └── speech_content_20_stage04.xlsx
```


**Columns (speech_content_--)**:
| Column name      | Description                                                  |
|------------------|--------------------------------------------------------------|
| `id`             | Unique ID of the speech                                      |
| `session`        | Session number (e.g. "001")                                  |
| `first_name`     | First name(s) of the speaker                                 |
| `last_name`      | Last name of the speaker                                     |
| `faction_id`     | Integer ID of the faction                                    |
| `position_short` | Role class (e.g. "MP", "Minister", "Presidium")              |
| `position_long`  | Full title (e.g. "Parliamentary Secretary of State")         |
| `politician_id`  | Foreign key to matched person (or -1 if unknown)             |
| `speech_content` | Full plain text of the speech and `text_position` of contributions e.g. ({1}) |
| `date`           | Date of the session in Unix timestamp format (seconds since 1970) |

**Columns (contributions_simplified_--)**:
| Column name      | Description                                 |
|------------------|---------------------------------------------|
| `text_position`  | Character index in the speech text          |
| `content`        | Extracted contribution (e.g. "[Applause]")  |
| `speech_id`      | Foreign key to the speech this belongs to   |

# **5 Contributions**

## **5.1 Extended contributions - Normalize Speaker Names and Assign Party Affiliation**

Processes the contributions_extended files from stage 4 and prepares them for further use by:
- **Name Cleaning and Splitting:**
    - The name_raw field (raw PDF name extractions) is cleaned from unwanted characters.
    - Academic titles and nobility prefixes (e.g., Dr., von, Freiherr) are removed.
    - Names are then split into first_name and last_name.
- **Faction Matching:**
    - Party names are normalized using regex patterns.
    - The faction field is mapped to a canonical abbreviation.
    - Corresponding faction_id values are assigned from a precompiled faction lookup table.
- **Output Generation:**
    - At this point the fields first_name, last_name, acad_title, faction, and faction_id are properly cleaned and normalized.


### **Input:**
```
dataStage04/
├── contributionsExtended/
│   ├── electoral_term_19/
│   │   ├── 19001.pkl
│   │   └── …
│   ├── electoral_term_20/
│   │   ├── 20001.pkl
│   │   └── …
dataStage03/
├── dataFactionsStage03/
│   └── factionsAbbreviations.pkl
```

### **Ouput:**
```
dataStage05/
├── contributionsExtendedStage05/
│   ├── electoral_term_19/
│   │   ├── 19001.pkl
│   │   └── …
│   ├── electoral_term_20/
│   │   ├── 20001.pkl
│   │   └── …
```

## **5.2 Assign Speaker Identity to extended Contributions**

Assigns a unique politician ID (ui) to each contribution entry by matching cleaned name components and metadata to the politician registry:
- Loads the cleaned contributions from dataStage05.
- Loads the complete list of politicians (including government and parliament members) from stage 3.
- Cleans and normalizes name columns in the politician database to facilitate accurate matching.
- Filters politicians per electoral term for performance and accuracy.
- For each file:
    - Matches speaker identity via first_name and last_name against the politician list.
    - Assigns the corresponding ui (unique ID) to the contribution.
    - This matching logic is encapsulated in insert_politician_id_into_contributions_extended() which can be found in [exctract_contributions.py](exctract_contributions.py)



### **Input:**
```
dataStage03/
├── dataPoliticiansStage03/
│   └── politicians.csv
dataStage05/
├── contributionsExtendedStage05/
│   ├── electoral_term_19/
│   │   ├── 19001.pkl
│   │   └── …
│   ├── electoral_term_20/
│   │   ├── 20001.pkl
│   │   └── …
```

### **Ouput:**
```
dataStage06/
├── contributionsExtendedStage06/
│   ├── electoral_term_19/
│   │   ├── 19001.pkl
│   │   └── …
│   ├── electoral_term_20/
│   │   ├── 20001.pkl
│   │   └── …
```

# **6 Merge and Structure Speech & Contribution Data**


Merges all speech and contribution data from the 19th and 20th electoral periods into unified datasets. It also ensures consistency in structure, adds helpful metadata and saves all outputs both as .pkl and .xlsx files for downstream processing or analysis.

**Speech Content (Redebeiträge)**:
- Loads pickled DataFrames containing speech data per term.
- Adds the electoral_term and document_url fields for each speech.
- Ensures correct data types and column structure.
- Merges the 19th and 20th terms into one speech_content DataFrame.
- Saves:
    - Combined dataset (speech_content_19_20.pkl)
    - Per-period datasets (speech_content_19.pkl, speech_content_20.pkl)
    - Excel copies for all three.

**Extended Contributions (Einwürfe, Zwischenrufe)**:
- Iterates over all .pkl contribution files for each term.
- Renames and reorders relevant columns.
- Adds a unique contribution id.
- Ensures unified data types.
- Saves:
    - Per-period contribution data as .pkl and .xlsx.
    - A merged dataset contributions_extended_19_20.pkl.


### **Input:**
```
rawData/
├── rawData19xml/*.xml
│   ├── 19001.xml
│   └── …
├── rawData20xml/*.xml
│   ├── 20001.xml
│   └── …
dataStage04/
├── speechContent/
│   ├── electoral_term_19/
│   │   └── speech_content.pkl
│   ├── electoral_term_20/
│   │   └── speech_content.pkl
dataStage06/
├── contributionsExtendedStage06/
│   ├── electoral_term_19/
│   │   ├── 19001.pkl
│   │   └── …
│   ├── electoral_term_20/
│   │   ├── 20001.pkl
│   │   └── …
```

### **Ouput:**
```
dataFinalStage/
├── contributionsExtendedFinalStage/
│   ├── contributions_extended_19_20.pkl
│   ├── contributions_extended_19.pkl
│   └── contributions_extended_20.pkl
├── speechContentFinalStage/
│   ├── speech_content_19_20.pkl
│   ├── speech_content_19.pkl
│   └── speech_content_20.pkl
dataExcel/
├── finalStage
│   ├── contributions_extended_19_20_finalStage.xlsx
│   ├── contributions_extended_19_finalStage.xlsx
│   ├── contributions_extended_20_finalStage.xlsx
│   ├── speech_content_19_20_finalStage.xlsx
│   ├── speech_content_19_finalStage.xlsx
│   └── speech_content_20_finalStage.xlsx
```


**Columns (speech_content_*.pkl):**
| Column            | Description                                          |
|-------------------|------------------------------------------------------|
| `id`              | Unique ID for each speech block                     |
| `electoral_term`  | Electoral period (e.g., 19, 20)                     |
| `session`         | Session number within the term                      |
| `first_name`      | First name of the speaker                           |
| `last_name`       | Last name of the speaker                            |
| `faction_id`      | Faction ID assigned to the speaker                  |
| `position_short`  | Speaker's role (e.g., MP, Minister)                 |
| `position_long`   | Full position title (e.g., "Bundesminister für...") |
| `politician_id`   | Unique politician ID (ui)                           |
| `speech_content`  | Full speech text                                    |
| `date`            | Session date (in Unix time format)                  |
| `document_url`    | Link to original PDF of session                     |

**Columns (contributions_extended_*.pkl):**
| Column          | Description                                   |
|------------------|-----------------------------------------------|
| `id`            | Unique ID for the contribution                |
| `type`          | Contribution type (e.g., "Einwurf", "Beifall") |
| `first_name`    | First name of the contributor                 |
| `last_name`     | Last name of the contributor                  |
| `faction_id`    | Faction ID of the contributor                 |
| `speech_id`     | Refers to the speech this contribution belongs to |
| `text_position` | Position within the speech text               |
| `politician_id` | ID of the contributor (if identifiable)       |
| `content`       | Extracted contribution text                   |