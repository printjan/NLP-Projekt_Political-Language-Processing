

# Fundstelle

Liefert im Vorgangsablauf das zu einem Vorgangsschritt gehörende Dokument (Drucksache oder Protokoll).   Beispiel: „BT-Drucksache 19/1 (Antrag Fraktion der CDU/CSU)“ oder beim Vorgangsschritt Beratung „BT-Plenarprotokoll 19/1, S. 4C-12A“. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | ID einer Drucksache oder eines Plenarprotokolls |  |
|**dokumentart** | [**DokumentartEnum**](#DokumentartEnum) |  |  |
|**pdfUrl** | **String** |  |  [optional] |
|**dokumentnummer** | **String** |  |  |
|**datum** | **LocalDate** |  |  |
|**drucksachetyp** | **String** |  |  [optional] |
|**herausgeber** | **Zuordnung** |  |  |
|**urheber** | **List&lt;String&gt;** |  |  |
|**verteildatum** | **LocalDate** |  |  [optional] |
|**seite** | **String** |  |  [optional] |
|**anfangsseite** | **Integer** |  |  [optional] |
|**endseite** | **Integer** |  |  [optional] |
|**anfangsquadrant** | **Quadrant** |  |  [optional] |
|**endquadrant** | **Quadrant** |  |  [optional] |
|**frageNummer** | **String** |  |  [optional] |
|**anlagen** | **String** |  |  [optional] |
|**top** | **Integer** |  |  [optional] |
|**topZusatz** | **String** |  |  [optional] |



## Enum: DokumentartEnum

| Name | Value |
|---- | -----|
| DRUCKSACHE | &quot;Drucksache&quot; |
| PLENARPROTOKOLL | &quot;Plenarprotokoll&quot; |



