

# PlenarprotokollText


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**dokumentart** | [**DokumentartEnum**](#DokumentartEnum) |  |  |
|**typ** | [**TypEnum**](#TypEnum) |  |  |
|**dokumentnummer** | **String** |  |  |
|**wahlperiode** | **Integer** |  |  [optional] |
|**herausgeber** | **Zuordnung** |  |  |
|**datum** | **LocalDate** |  |  |
|**aktualisiert** | **OffsetDateTime** | Letzte Aktualisierung der Entität |  |
|**titel** | **String** |  |  |
|**fundstelle** | [**Fundstelle**](Fundstelle.md) |  |  |
|**pdfHash** | **String** | MD5-Prüfsumme der PDF-Datei |  [optional] |
|**vorgangsbezug** | [**List&lt;Vorgangsbezug&gt;**](Vorgangsbezug.md) | Zusammenfassung der ersten 4 zugehörigen Vorgänge |  [optional] |
|**vorgangsbezugAnzahl** | **Integer** | Gesamtzahl der zugehörigen Vorgänge |  |
|**sitzungsbemerkung** | **String** |  |  [optional] |
|**text** | **String** | Volltext des Dokuments  Das Beispiel enthält einen gekürzten Auszug einer Drucksache.  |  [optional] |



## Enum: DokumentartEnum

| Name | Value |
|---- | -----|
| PLENARPROTOKOLL | &quot;Plenarprotokoll&quot; |



## Enum: TypEnum

| Name | Value |
|---- | -----|
| DOKUMENT | &quot;Dokument&quot; |



