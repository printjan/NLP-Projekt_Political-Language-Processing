

# Vorgang

Liefert Metadaten zu einem Vorgang.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**typ** | [**TypEnum**](#TypEnum) |  |  |
|**beratungsstand** | **String** |  |  [optional] |
|**vorgangstyp** | **String** |  |  |
|**wahlperiode** | **Integer** |  |  |
|**initiative** | **List&lt;String&gt;** |  |  [optional] |
|**datum** | **LocalDate** | Datierung des letzten zugehörigen Dokuments |  [optional] |
|**aktualisiert** | **OffsetDateTime** | Letzte Aktualisierung der Entität |  |
|**titel** | **String** |  |  |
|**_abstract** | **String** |  |  [optional] |
|**sachgebiet** | **List&lt;String&gt;** |  |  [optional] |
|**deskriptor** | [**List&lt;VorgangDeskriptor&gt;**](VorgangDeskriptor.md) |  |  [optional] |
|**gesta** | **String** | GESTA-Ordnungsnummer |  [optional] |
|**zustimmungsbeduerftigkeit** | **List&lt;String&gt;** |  |  [optional] |
|**kom** | **String** | KOM-Nr. |  [optional] |
|**ratsdok** | **String** | Ratsdok-Nr. |  [optional] |
|**verkuendung** | [**List&lt;Verkuendung&gt;**](Verkuendung.md) |  |  [optional] |
|**inkrafttreten** | [**List&lt;Inkrafttreten&gt;**](Inkrafttreten.md) |  |  [optional] |
|**archiv** | **String** | Archivsignatur |  [optional] |
|**mitteilung** | **String** |  |  [optional] |
|**vorgangVerlinkung** | [**List&lt;VorgangVerlinkung&gt;**](VorgangVerlinkung.md) |  |  [optional] |
|**sek** | **String** | SEK-Nr. |  [optional] |



## Enum: TypEnum

| Name | Value |
|---- | -----|
| VORGANG | &quot;Vorgang&quot; |



