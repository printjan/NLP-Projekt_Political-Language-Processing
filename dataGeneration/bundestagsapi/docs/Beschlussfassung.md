

# Beschlussfassung

Liefert die Beschlussfassung (z. B. Annahme, Ablehnung, Kenntnisnahme) zu einer Drucksache mit Fundstelle im Plenarprotokoll sowie Angaben zu ggf. erforderlichen qualifizierten Mehrheiten (`mehrheit`) bzw. der besonderen Abstimmungsverfahren (`abstimmungsart`).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**beschlusstenor** | **String** |  |  |
|**seite** | **String** |  |  [optional] |
|**abstimmungsart** | [**AbstimmungsartEnum**](#AbstimmungsartEnum) |  |  [optional] |
|**abstimmErgebnisBemerkung** | **String** |  |  [optional] |
|**grundlage** | **String** |  |  [optional] |
|**dokumentnummer** | **String** |  |  [optional] |
|**mehrheit** | [**MehrheitEnum**](#MehrheitEnum) |  |  [optional] |



## Enum: AbstimmungsartEnum

| Name | Value |
|---- | -----|
| ABSTIMMUNG_DURCH_AUFRUF_DER_L_NDER | &quot;Abstimmung durch Aufruf der Länder&quot; |
| GEHEIME_WAHL | &quot;Geheime Wahl&quot; |
| HAMMELSPRUNG | &quot;Hammelsprung&quot; |
| NAMENTLICHE_ABSTIMMUNG | &quot;Namentliche Abstimmung&quot; |
| VERH_LTNISWAHL | &quot;Verhältniswahl&quot; |



## Enum: MehrheitEnum

| Name | Value |
|---- | -----|
| ABSOLUTE_MEHRHEIT | &quot;Absolute Mehrheit&quot; |
| ZWEIDRITTELMEHRHEIT | &quot;Zweidrittelmehrheit&quot; |



