## **Preprocessing & Daten bereinigen (ML-Task 1: Klassifikation)**

### **1. Initiale Datenbereinigung**
- **Ziel:** Datensatz von nicht-klassifikationsrelevanten Inhalten befreien.  
→ diese initiale Verkleinerung des Datensatzes verhindert unnötigen Aufwand und Verzerrungen in den nächsten Schritten  
  - **Entfernen moderativer Redebeiträge** (`position_short == "Presidium of Parliament"`)  
    → diese Beiträge liefern keine parteispezifischen Informationen, sind also irrelevant für die Klassifikation  
  - **Entfernen von nicht klassifizierbaren Redebeiträgen** (`faction_id == -1`)  
    → diese Beiträge sind ohne klare Zuordnung zu Parteien und somit nicht für die 1.ML-Task verwendbar

---

### **2. Text-Cleaning und Normalisierung**
- **Ziel:** Robuste und einheitliche Textbasis schaffen, die gut interpretierbar für das Klassifikationsmodell ist.
- Achtung: Diese Schritte beeinflussen maßgeblich Länge und Verteilung der Texte
- Essenzieller Schritt für textbasierte Modelle wie TF-IDF-basierte Klassifikatoren, Naive Bayes, SVM, logistische Regression oder neuronale Modelle (z.B. BERT).
  - **Umwandlung aller Buchstaben in Kleinbuchstaben**
  - **Umgang mit Contributions Positionen im speech_content: Entfernen:**
    - Durch Entfernung dieser Beiträge geht zwar Kontext verloren, aber Beiträge wie "Beifall" könnten besonders für reine Text-Klassifikations-Aufgaben redundanten noise erzeugen
  - **Umgang mit Zahlen: Entfernen:** (Hier könnte man später nochmal überprüfen, ob das Modell mit Zahlen besser wird!)
    - Zahlen treten typischerweise auf als: Jahreszahlen („im Jahr 2023“), Haushaltszahlen („30 Milliarden Euro“), Statistische Angaben („60 % der Bevölkerung“), Paragrafenverweise („nach § 42 BGB“), Datumsangaben, Sitzungsnummern, Artikelnummern etc.
    - Zahlen sind meist nicht parteispezifisch, sondern inhaltlich neutral bzw. aus Sicht des Modells inhaltsleerer numerischer Noise, durch dessen Entfernung wir besser generalisieren können. Auch minimieren wir das Risiko, dass das Modell Zusammenhänge wie SPD->30 lernt
  - **Umgang mit Sonderzeichen: Entfernen**
  - **Stopwörter: Entfernen**
    - Diese Wörter treten häufig auf, tragen aber keine Parteispezifische Bedeutung. Entfernung erhöht die Trennschärfe der Partei-typischen Begriffe
    - Standard-Stopwortlisten für Deutsch (z.B. von NLTK, spaCy)
    - Ergänzung der Standard Listen um domänenspezifische Stopwörterlisten (mit ChatGPT erstellt)
  - **Umgang mit hochfrequenten Textteilen (z.B. Anredeformeln wie "Sehr geehrte Damen und Herren"): Entfernen um Modellgüte und generalisierbarkeit zu erhöhen**
    - Diese Formulierungen sind rein protokollarisch oder höflich und nicht parteipolitisch motiviert
    - Sie dienen nur dem sozialen Rahmen und nicht dem inhaltlichen Diskurs
    - Modelle könnten ggf. rein statistische Korrelationen ("Frau Präsidentin" -> SPD) lernen, die semantisch nicht gerechtfertigt sind 
    - Entfernung mittels einer von ChatGPT erstellten Liste
  - **Tokenisierung und Lemmatization durchführen:** 
    - Verwendung von spaCy oder NLTK für eine effektive deutsche Lemmatization

---

### **Für Schritte 1 und 2 wird eine zentralisierte Funktion [preprocess_speech_data()](dataPreprocessingHelpers/preprocessing_pipeline.py)**

Es werden folgende Datensätze erstellt:

| dataset number | preprocessing steps                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------|
| 1              | full cleaning, domain specific spacy stopword removal, phrase pattern removal                          |
| 2              | full cleaning, spacy stopword removal, phrase pattern removal                                          |
| 3              | full cleaning, spacy stopword removal                                                                  |
| 4              | full cleaning, phrase pattern removal                                                                  |
| 5              | full cleaning                                                                                          |
| 6              | no cleaning, spacy stop word removal                                                                   |
| 7              | cleaning (lowercase), domain specific spacy stopword removal                                           |
| 8              | no cleaning, phrase pattern removal                                                                    |
| 9              | cleaning (lowercase), domain specific spacy stopword removal, phrase pattern removal                   |
| 10             | cleaning (lowercase), domain specific spacy stopword removal, phrae based removal, contribution insert |


| Dataset name | Details               | Lowercase | Remove digits | Remove punctuation | Stopword removal | Domain specific stopword removal | Phrase pattern removal | Contribution Mode |
|--------------|-----------------------|-----------|---------------|--------------------|------------------|----------------------------------|------------------------|-------------------|
| data_set_1   | Extreme normalization | Yes       | Yes           | Yes                | Yes              | Yes                              | Yes                    | REMOVE            |
| data_set_2   | Middle ground         | Yes       | Yes           | Yes                | Yes              | No                               | No                     | REMOVE            |
| data_set_3   | Minimal normalization | Yes       | No            | No                 | No               | No                               | No                     | INSERT            |
| data_set_4   | BERT                  | No        | Yes           | Yes                | Yes              | Yes                              | Yes                    | REMOVE            |
| data_set_1   | LSTM                  | Yes       | Yes           | Yes                | Yes              | Yes                              | Yes                    | REMOVE            |
| data_set_5   | BERT                  | No        | No            | No                 | Yes              | No                               | No                     | INSERT            |
| data_set_6   | LSTM                  | Yes       | No            | No                 | Yes              | No                               | No                     | INSERT            |
| data_set_7   | BERT                  | No        | No            | No                 | No               | No                               | No                     | INSERT            |
| data_set_8   | LSTM                  | Yes       | No            | No                 | No               | No                               | Yes                    | REMOVE            |
| data_set_9   | BERT                  | No        | No            | No                 | No               | No                               | Yes                    | REMOVE            |
| data_set_3   | LSTM                  | Yes       | No            | No                 | No               | No                               | No                     | INSERT            |


---

### **3. Analyse der Redelängenan und Klassenverteilung**
- **Ziel:** Sicherstellen, dass extreme Redelängen das Modell nicht verzerren und die Klassenverteilung stabil ist
- Die Textlänge ist ein wichtiger Einflussfaktor für fast alle NLP-Modelle. Nach Textnormalisierung (Schritt 2) ist es ideal, die Länge final zu bewerten und Ausreißer zu bereinigen.
- Sehr wichtig besonders bei klassischen Vektorisierungen wie TF-IDF oder Naive Bayes, da diese stark auf Textlänge und Wortverteilung reagieren.
  - **Statistische Analyse der Redelänge durchführen:**
    - Durchschnittliche Redelänge, Median, Minimum, Maximum
    - Verteilung der Redelängen visualisieren (Histogramme, Boxplots)
  - **Ausreißer-Erkennung und Behandlung:**
    - Sehr kurze Reden (z.B. unter 50–100 Zeichen) entfernen (typischerweise kaum informative Inhalte)
    - Extrem lange Reden prüfen (z.B. Reden mit mehr als 2 Standardabweichungen über dem Mittelwert)  
      → Diese nicht zwingend entfernen, sofern sie nicht das Modell verzerren. Oft genügt es, sie zu kürzen/splitten
  - **Prüfen der Klassenverteilung:**
    - Verteilung der Klassen (Parteien) berechnen, nachdem Extremwerte entfernt wurden (Dabei muss sowohl Verteilung Redezeit bzw. Redelängen auf die Parteien sowie Anzahl der Reden pro Partei beachtet werden. Auch die ANzahl der verschiedenen Redner pro Partei ist hier interessant.)
    - Klassen mit zu wenigen Reden (z.B. weniger als 50) entfernen, da diese kaum valide Modellierung ermöglichen

---

### **4. Feature Engineering**
- **Ziel:** Daten in eine numerische und für das spezifische Modell optimal interpretierbare Form bringen
- Dieser Schritt folgt logischerweise nach den grundlegenden Bereinigungen und Analysen, da erst hier relevante Features sinnvoll erzeugt werden können
- **Feature Engineering variiert je nach Modelltyp:**
  - **Klassische NLP-Modelle** (Logistische Regression, Naive Bayes, SVM, Random Forest):
    - TF-IDF-Vektorisierung
    - Berücksichtige n-Gramme (1 bis 3-Gramme), um Kontext besser einzufangen.
  - **Für Deep-Learning-basierte Ansätze bzw. neuronale Modelle** (z.B. BERT):
    - Direkt Nutzung von Embeddings (TF-IDF entfällt)
- **Optionale Feature-Erweiterungen** (Durchläufe mit und ohne die Erweiterungen um deren Einfluss festzustellen):
  - Redelänge als zusätzliches numerisches Feature
  - Metainformationen:
    - Redezeitpunkt (als zeitliches Feature)
    - Position des Sprechers (Minister, einfacher Abgeordneter)
    - Geschlecht (falls für Fairnessanalyse relevant)
    - Themencluster aus Topic Modeling (wenn bereits vorhanden)
- **Grundlegende Überlegung zur Datensatz Erstellung:**
  - TF-IDF (z.B. SVM):
    - Hohe Relevanz von exaktem Wording und sparsamer, klarer Sprache.
    - Stemming und Lemmatization sind hilfreich.
    - Stopword-Removal und Phrase-Patterns reduzieren Noise und helfen der TF-IDF-Methode, sich auf parteispezifische Begriffe zu konzentrieren.
    - Sinnvoll: starke Normalisierung (kleinschreiben, Zahlen und Interpunktion entfernen).
  - Embeddings & Deep-Learning (z.B. BERT) 
    - Modelle profitieren stark von Kontext und Syntax.
    - Zu starke Entfernung grammatikalischer und struktureller Information (wie Interpunktion oder Zahlen) kann kontraproduktiv sein.
    - Stopword-Removal nur moderat sinnvoll; kontextuelle Bedeutung der Sprache sollte erhalten bleiben.
    - Lemmatization hilfreich, um semantische Zusammenhänge deutlicher zu machen, Stemming eher schädlich (kann Embeddings verfälschen).

---

### **5. Umgang mit Klassenungleichgewicht**
- **Ziel:** Ausgewogene Datengrundlage schaffen, um Modelle nicht durch dominante Klassen zu verzerren
- Dieser Schritt erfolgt direkt vor dem Data-Split, da er auf dem finalen Datensatz durchgeführt werden sollte und vor dem Split das Klassengleichgewicht sichergestellt werden sollte, um eine repräsentative Aufteilung der Daten zu gewährleisten
- Vergleichende Evaluation verschiedener Techniken wie (MOTE, Oversampling, Undersampling oder Klassengewichte

### **6. Data-Split und Umgang mit Klassenungleichgewicht**
- **Ziel:** Realistische und robuste Einschätzung der Generalisierungsfähigkeit und Performance der Modelle
- Finaler Schritt vor der Modellierung, da man erst auf dem endgültigen, bereinigten, feature-engineertem und klassenausgeglichenem Datensatz die finale Modellbewertung durchführen kann
  - **Standard:** Zufallsbasierte, stratifizierte Train-Test-Aufteilung
  - Erweiterungen:
    - **Rednerbasierte Splits:** Falls bestimmte Redner dominieren, Cross-Validation mit gruppierten Rednern durchführen, um sicherzustellen, dass Modelle nicht rednerspezifische Muster, sondern parteispezifische Muster lernen  
      → Wenn du viele Reden derselben Person hast, könnten Redner-spezifische Muster das Modell stärker beeinflussen als Parteimuster.
    - **Zeitbasierte Splits:** Wenn thematische Perioden dominieren (z.B. Corona, Ukraine Krieg)  
      → um zu prüfen, ob das Modell generalisiert


---

## **`preprocess_speech_data()`: Modular Preprocessing-Pipeline for Bundestagsreden**

This function applies a configurable and modular preprocessing pipeline to Bundestag speech
data (column: 'speech_content'), supporting advanced filtering, text normalization, contribution handling,
stopword removal, linguistic normalization (lemmatization, stemming, tokenization), and speech length statistics. 
It transforms raw speech texts into structured and clean textual input for machine learning models.
The function can also extract and store related contribution data for the filtered subset of speeches.

This function applies a configurable and modular preprocessing pipeline to Bundestag speech
    data (column: 'speech_content'), supporting advanced filtering, text normalization, contribution handling,
    stopword removal, linguistic normalization (lemmatization, stemming, tokenization), and speech length statistics.
    The function can also extract and store related contribution data for the filtered subset of speeches.

---

### **Capabilities and main steps:**
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

- Datenpunkte entfernen, deren Redner eine gewisse position_short belegen
- Datenpunkte entfernen, deren faction_id ungültig (-1) ist
- Datenpunkte entfernen, die eine bestimmte faction_id haben
- Die faction id von Datenpunkten mit bestimmter faction_id zu einer anderen faction_id ändern
- Contribution Position Marker (bspw. ({1}) ) aus dem Text entfernen oder die Contributions_Simplified wieder an ihre Stelle einfügen
- Den speech_content aller Datenpunkte zu lowecase convertieren
- Alle Zahlen aus dem speech_content aller Datenpunkte entfernen
- Alle Punkte etc. aus dem speech_content aller Datenpunkte entfernen
- SPACY oder NLTK oder gar kein Stopword Removal auf dem speech_content aller Datenpunkte
- Wenn Stopword Removal durchgeführt wird: Stopword Liste um eine custom Liste erweitern
- Phrase Pattern Entfernung auf dem speech_content aller Datenpunkte (basierend auf einer Regex Liste)
- lemmatisierung mit SPACY
- Stemming mit NLTK
- Tokenization mit SPACY, NLTK oder gar nicht
- Token, Lemmas oder / und Buchstaben Anzahl für jeden speech_content aller Datenpunkte

---

### **Input Parameters of `preprocess_speech_data()`**

| Parameter                       | Type                               | Standard | Description                                                                                                                                                                                     |
|---------------------------------|------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `input_path`                    | `Path`                             |          | Mandatory: Path to the input `.pkl` file containing the speeches                                                                                                                                |
| `output_path_pickle`            | `Path`                             |          | Mandatory: Path where the cleaned `.pkl` file shall be saved                                                                                                                                    |
| `output_path_excel`             | `Path`                             | `None`   | Enables Excel export of the results to the given path                                                                                                                                           |
| `position_short`                | `list[str]`                        | `None`   | Filters out rows where position_short matches one mentioned in the given list (e.g., "Guest") (Case sensitive!)                                                                                 |
| `only_valid_faction_id`         | `bool`                             | `False`  | If Enabled: Removes all speeches with `faction_id == -1`                                                                                                                                        |
| `without_faction`               | `str`                              | `None`   | Removes all speeches with this specific faction ID                                                                                                                                              |
| `change_faction`                | `list[str]`                        | `None`   | change_faction must be a list of two strings: [old_faction_id, new_faction_id]. All matching old_faction_ids will be replaced by new_faction_id                                                 |
| `generate_contributions_data`   | `bool`                             | `False`  | If Enabled: Saves reduced contributions data matching speech_ids in dataset                                                                                                                     |
| `contributions`                 | `"REMOVE"` / `"INSERT"` / `"NONE"` | `"NONE"` | Controls how contribution position markers (e.g., ({2}) ) are handled                                                                                                                           |
| `contributions_simplified_path` | `Path`                             | `None`   | Optional path to the simplified contributions `.pkl` file. Used for reinsertion (if `contributions="INSERT"`) and for generating filtered contributions (if `generate_contributions_data=True`) |
| `contributions_extended_path`   | `Path`                             | `None`   | Optional path to the extended contributions `.pkl` file. Only used for generating filtered contributions (if `generate_contributions_data=True`)                                                |
| `to_lower`                      | `bool`                             | `False`  | If Enabled: Converts all text to lowercase                                                                                                                                                      |
| `remove_digits`                 | `bool`                             | `False`  | If Enabled: Removes all numeric digits                                                                                                                                                          |
| `remove_punctuation`            | `bool`                             | `False`  | If Enabled: Removes punctuation characters                                                                                                                                                      |
| `stopword_mode`                 | `"NLTK"` / `"SPACY"` / `"NONE"`    | `"NONE"` | Enables stopword removal and selects stopword removal method                                                                                                                                    |
| `custom_stopwords`              | `set`                              | `None`   | Input for a set of domain-specific stopwords to extend base lists                                                                                                                               |
| `phrase_patterns`               | `list[str]`                        | `None`   | Input for a list of regexes for regex-phrase-based text removal                                                                                                                                 |
| `lemmatization`                 | `bool`                             | `False`  | If Enabled: Applies lemmatization using spaCy                                                                                                                                                   |
| `stemming`                      | `bool`                             | `False`  | If Enabled: Applies stemming using NLTK                                                                                                                                                         |
| `tokenization_method`           | `"NLTK"` / `"SPACY"` / `"NONE"`    | `"NONE"` | Enables tokenization and defines which Tokenizer is used                                                                                                                                        |
| `add_char_count`                | `bool`                             | `False`  | If Enabled: Adds a column with character count (counts characters after latest preprocessing step)                                                                                              |
| `add_token_count`               | `bool`                             | `False`  | If Enabled: Adds a column with token count (if tokenization is also enabled)                                                                                                                    |
| `add_lemma_count`               | `bool`                             | `False`  | If Enabled: Adds a column with lemma count (if lemmatization is also enabled)                                                                                                                   |


---

### **Output**
- The preprocessed speech DataFrame is saved to:
  - `output_path_pickle` (`.pkl`, always)
  - `output_path_excel` (`.xlsx`, optional: can be enabled by adding a `output_path_excel` in the function call)
- If `generate_contributions_data = True`, two additional files are saved to `output_path_pickle`:
  - `contributions_simplified.pkl`: Filtered simplified contributions
  - `contributions_extended.pkl`: Filtered extended contributions
- No value is returned (in-place saving only).


---

### **Output Columns**

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

---

### **Example Use in Jupyter Notebook (EDIT PATHS BEFORE USING!!):**

```python
# imports
from pathlib import Path
from dataPreprocessingHelpers.preprocessing_pipeline import execute_parallel_preprocessing
from dataPreprocessingHelpers.preprocessing_pipeline import ensure_required_nlp_resources

# spaCy-Ressourcen laden (in der Shell oder im Jupyter-Notebook via "!") 
!python - m
spacy
download
de_core_news_sm

# regex pattern for phrase-based removal
PHRASE_PATTERNS_CLASSIFICATION_3 = [
  r"^sehr geehrte[r]? (herr|frau)?( präsident(in)?| vizepräsident(in)?).*?(kolleg(inn)?en)?",
  # Erweitert um optionale Begriffe wie "Kolleginnen und Kollegen"
  r"^meine (sehr geehrten )?damen und herren(,)?",  # Erweiterung um optionales "sehr geehrten" und Komma
  r"^(werte|liebe) kolleginnen und kollegen",  # Erweiterung um "liebe" als Alternativformulierung
  r"^ich (möchte|will|werde|darf) mich.*?(bedanken|ausführen|äußern|anschließen)",
  # Erweitert um typische Formulierungen wie "äußern" oder "anschließen"
  r"(zum|abschließend zum|abschließend möchte ich).*?schluss.*",
  # Erweiterung um häufige Formulierung "abschließend möchte ich"
  r"ich danke (ihnen|für ihre aufmerksamkeit|für ihre geduld).*?$",
  # Sicherstellung, dass Danksagungen am Ende exakt getroffen werden
  r"(vielen|herzlichen) dank für.*?$",  # Ergänzung um häufige Dankes-Varianten am Redeende
  r"^(danke|besten dank|vielen dank).*?$",  # Direkte Danksagungen am Anfang oder Ende der Rede
  r"^(herr|frau) (präsident|präsidentin|vizepräsident|vizepräsidentin),?$",
  # Einfache und sehr häufige Begrüßung des Präsidiums
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
      "input_path": Path(f".../speech_content_{term}.pkl"),
      "output_path_pickle": Path(f".../data_set_12_{term}.pkl"),
      "output_path_excel": Path(f".../data_set_12_{term}.pkl"),

      # Optional filters (deactivated here)
      "position_short": ["Presidium of Parliament", "Guest"],  # removes presidium/neutral moderation
      "only_valid_faction_id": True,
      "without_faction": None,
      "change_faction": ["3", "7"],  # swap BSW to Die Linke
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
```

