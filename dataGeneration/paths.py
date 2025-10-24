"""
Centralized path configuration for the Data Generation Pipeline.

This module defines all major input and output paths in a structured form,
organized by processing stage and data type. Can be imported wherever file
access is needed in the project.
"""

from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_GENERATION_DIR = DATA_DIR / "dataGeneration"
DATA_FINAL_STAGE_DIR = DATA_DIR / "dataFinalStage"
DATA_EXCEL_DIR = DATA_DIR / "dataExcel"

# === Raw Data ===
RAW_DIR = DATA_GENERATION_DIR / "rawData"
RAW_ELECTORAL_TERMS = RAW_DIR / "electoralTerms" / "electoralTerms.csv"
RAW_POLITICIANS = RAW_DIR / "politiciansRawData"
RAW_JSON_19 = RAW_DIR / "rawData19json"
RAW_JSON_20 = RAW_DIR / "rawData20json"
RAW_PDF_19 = RAW_DIR / "rawData19pdf"
RAW_PDF_20 = RAW_DIR / "rawData20pdf"
RAW_XML_19 = RAW_DIR / "rawData19xml"
RAW_XML_20 = RAW_DIR / "rawData20xml"

# === Stage 02 ===
STAGE02 = DATA_GENERATION_DIR / "dataStage02"
XML_SPLIT_19 = STAGE02 / "data19xmlSplit"
XML_SPLIT_20 = STAGE02 / "data20xmlSplit"
FACTIONS_STAGE02 = STAGE02 / "dataFactionsStage02" / "factions.pkl"
POLITICIANS_STAGE02 = STAGE02 / "dataPoliticiansStage02" / "mps.pkl"

# === Stage 03 ===
STAGE03 = DATA_GENERATION_DIR / "dataStage03"
FACTIONS_ABBR_STAGE03 = STAGE03 / "dataFactionsStage03" / "factionsAbbreviations.pkl"
MPS_FACTIONS_STAGE03 = STAGE03 / "dataPoliticiansStage03" / "mpsFactions.pkl"
SPEAKER_LOOKUP_STAGE03 = STAGE03 / "dataPoliticiansStage03" / "speaker_faction_lookup.csv"

# === Stage 04 ===
STAGE04 = DATA_GENERATION_DIR / "dataStage04"
SPEECH_CONTENT_STAGE04 = STAGE04 / "speechContent"
CONTRIB_EXT_19 = STAGE04 / "contributionsExtended" / "electoral_term_19"
CONTRIB_EXT_20 = STAGE04 / "contributionsExtended" / "electoral_term_20"
CONTRIB_SIMPLIFIED = STAGE04 / "contributionsSimplified"
SPEECH_CONTENT_04_19 = SPEECH_CONTENT_STAGE04 / "electoral_term_19"
SPEECH_CONTENT_04_20 = SPEECH_CONTENT_STAGE04 / "electoral_term_20"

# === Stage 05 & 06 ===
STAGE05 = DATA_GENERATION_DIR / "dataStage05"
STAGE06 = DATA_GENERATION_DIR / "dataStage06"
CONTRIBUTIONS_EXTENDED_STAGE06 = STAGE06 / "contributionsExtendedStage06"

# === Final Stage ===
FINAL_STAGE = DATA_FINAL_STAGE_DIR
FINAL_CONTRIB_SIM = FINAL_STAGE / "contributionsSimplifiedFinalStage"
FINAL_CONTRIB_EXT = FINAL_STAGE / "contributionsExtendedFinalStage"
FINAL_SPEECH_CONTENT = FINAL_STAGE / "speechContentFinalStage"
FINAL_FACTIONS_ABBREVIATIONS = DATA_FINAL_STAGE_DIR / "factionsAbbreviations.pkl"

# === Excel Exports ===
EXCEL_FINAL_STAGE = DATA_EXCEL_DIR / "finalStage"
DATA_EXCEL_GENERATOR_DIR = DATA_EXCEL_DIR / "dataGeneration"
EXCEL_MGS = DATA_EXCEL_GENERATOR_DIR / "mgs_wiki_rawData.xlsx"
EXCEL_MPS_STAGE02 = DATA_EXCEL_GENERATOR_DIR / "mps_stage02.xlsx"
EXCEL_MPS_STAGE03 = DATA_EXCEL_GENERATOR_DIR / "mpsFactions_stage03.xlsx"
EXCEL_POLITICIANS_STAGE03 = DATA_EXCEL_GENERATOR_DIR / "politicians_stage03.xlsx"
EXCEL_SPEECH_STAGE04_19 = DATA_EXCEL_GENERATOR_DIR / "speech_content_19_stage04.xlsx"
EXCEL_SPEECH_STAGE04_20 = DATA_EXCEL_GENERATOR_DIR / "speech_content_20_stage04.xlsx"
EXCEL_FACTIONS_STAGE02 = DATA_EXCEL_GENERATOR_DIR / "factions_stage02.xlsx"
EXCEL_FACTIONS_ABBR_STAGE03 = EXCEL_FINAL_STAGE/ "factionsAbbreviations.xlsx"
EXCEL_CONTRIB_SIMPLIFIED_STAGE04 = DATA_EXCEL_GENERATOR_DIR / "contributionsSimplified_stage04.xlsx"

