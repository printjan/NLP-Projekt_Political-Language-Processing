

# Aktivitaet

Liefert Metadaten zu einer Aktivität.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**aktivitaetsart** | **String** |  |  |
|**typ** | [**TypEnum**](#TypEnum) |  |  |
|**dokumentart** | [**DokumentartEnum**](#DokumentartEnum) |  |  |
|**wahlperiode** | **Integer** |  |  |
|**datum** | **LocalDate** |  |  |
|**aktualisiert** | **OffsetDateTime** | Letzte Aktualisierung der Entität oder des zugehörigen Dokuments |  |
|**titel** | **String** |  |  |
|**fundstelle** | [**Fundstelle**](Fundstelle.md) |  |  |
|**vorgangsbezug** | [**List&lt;Vorgangspositionbezug&gt;**](Vorgangspositionbezug.md) | Zusammenfassung der ersten 4 zugehörigen Vorgänge |  [optional] |
|**vorgangsbezugAnzahl** | **Integer** | Gesamtzahl der zugehörigen Vorgänge |  |
|**deskriptor** | [**List&lt;Deskriptor&gt;**](Deskriptor.md) |  |  [optional] |
|**_abstract** | **String** |  |  [optional] |



## Enum: TypEnum

| Name | Value |
|---- | -----|
| AKTIVIT_T | &quot;Aktivität&quot; |



## Enum: DokumentartEnum

| Name | Value |
|---- | -----|
| DRUCKSACHE | &quot;Drucksache&quot; |
| PLENARPROTOKOLL | &quot;Plenarprotokoll&quot; |



