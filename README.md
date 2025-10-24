# **Political Language Processing**


## **Team:**

* Julian Dreykorn: dreykornju96245@th-nuernberg.de
* Simon Zeitler: zeitlersi95865@th-nuernberg.de
* Jan Tischner: tischnerja95752@th-nuernberg.de

If you use this repository, please consider citing as:

```
Tischner Jan, Julian Dreykorn, Simon Zeitler (2025): Political Language Processing: A analysis of German Bundestag Speeches covering 19th & 20th Legislative Periods.
```
---


## **Political Language Processing**

In our project “Political Language Processing”, we analyze political speeches in the German Bundestag using Natural Language Processing. The aim is to gain insights into the dynamics and structure of political communication. Our motivation is to reveal and critically question hidden patterns and relationships in political discourse.

The scenario focuses on a comprehensive analysis of the plenary protocols of the German Bundestag. As a hypothetical client, we consider, for example, political research institutes, media houses, or parties that are interested in detailed analyses and comprehensible visualizations of political communication.

Specifically, we aim to answer the following questions:
* Which party speaks how much, and how fair is the allocation of speaking time?
* Is it possible to automatically identify the party affiliation or even the identity of a speaker based solely on the speech transcript?
* Which main topics dominate the political discourse, and how do the parties differ in this regard?


---


## **data**


### **For our project, the data was fetched from the open data service provided by the Bundestag:**


* The data from the 19th electural term could simply be downloaded using the API.
* Note: For the 20th period, a small number of protocols were missing.
* For downloading, an API client was created and used, it is checked in under the bundestagsapi folder. However since the data only ahas to be downloaded once, this is not included in any notebook and just kept for reference.
* After crawling, the data was stored in a Pandas dataframe, preprocessed through several stages, and stored in Pickle (*.pkl) files. Below is a OneDrive link, containing the raw data and the preprocessing stages



## **Project Structure Overview:**

```
data/
├── dataGeneration/ … # created by the Data Generation Pipeline
│   │
├── dataFinalStage/ # final result of the Data Generation Pipeline
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
├── dataStatistics/…
├── dataClassification/…
├── dataTopicModeling/…
│
team-16/
├── dataGeneration/
│   ├── dataGeneratorPipeline.ipynb
│   ├── paths.py
│   ├── dataGenerator_Clean_Text.py
│   ├── dataGenerator_Extract_Contributions.py
│   ├── dataGenerator_Match_Names.py
│   └── bundestagsapi/
├── dataPreprocessingHelpers/
│   ├── preprocessing_pipeline.py
│   ├── phrase_patterns.py
│   └── domain_stopwords.py
├── statisticTask/
├── ML-Task-1_Classification/
│   ├── ML-Task-1_Classification.ipynb
│   ├── classification_experiments.ipynb
│   └── preprocessing_ML-Task-1.py
├── ML-Task-2_Topic-Modeling/
├── README.md
├── ProjectSheet.md
├── requirements.txt
├── nlp_project_env_setup.yml
└── pitch_slides.pdf
```

---


