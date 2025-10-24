

# DrucksacheText


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**typ** | [**TypEnum**](#TypEnum) |  |  |
|**dokumentart** | [**DokumentartEnum**](#DokumentartEnum) |  |  |
|**drucksachetyp** | **String** |  |  |
|**dokumentnummer** | **String** |  |  |
|**wahlperiode** | **Integer** |  |  [optional] |
|**herausgeber** | [**HerausgeberEnum**](#HerausgeberEnum) |  |  |
|**datum** | **LocalDate** |  |  |
|**aktualisiert** | **OffsetDateTime** | Letzte Aktualisierung der Entität |  |
|**titel** | **String** |  |  |
|**autorenAnzeige** | [**List&lt;DrucksacheAutorenAnzeigeInner&gt;**](DrucksacheAutorenAnzeigeInner.md) | Zusammenfassung der ersten 4 zur Anzeige markierten Autor:innen |  [optional] |
|**autorenAnzahl** | **Integer** | Gesamtzahl der Autor:innen |  |
|**fundstelle** | [**Fundstelle**](Fundstelle.md) |  |  |
|**pdfHash** | **String** | MD5-Prüfsumme der PDF-Datei |  [optional] |
|**urheber** | [**List&lt;Urheber&gt;**](Urheber.md) |  |  [optional] |
|**vorgangsbezug** | [**List&lt;Vorgangsbezug&gt;**](Vorgangsbezug.md) | Zusammenfassung der ersten 4 zugehörigen Vorgänge |  [optional] |
|**vorgangsbezugAnzahl** | **Integer** | Gesamtzahl der zugehörigen Vorgänge |  |
|**ressort** | [**List&lt;Ressort&gt;**](Ressort.md) |  |  [optional] |
|**anlagen** | **String** |  |  [optional] |
|**text** | **String** | Volltext des Dokuments  Das Beispiel enthält einen gekürzten Auszug einer Drucksache.  |  [optional] |



## Enum: TypEnum

| Name | Value |
|---- | -----|
| DOKUMENT | &quot;Dokument&quot; |



## Enum: DokumentartEnum

| Name | Value |
|---- | -----|
| DRUCKSACHE | &quot;Drucksache&quot; |



## Enum: HerausgeberEnum

| Name | Value |
|---- | -----|
| BT | &quot;BT&quot; |
| BR | &quot;BR&quot; |



