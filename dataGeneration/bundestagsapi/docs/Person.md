

# Person

Liefert Personenstammdaten zu einer Person

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**nachname** | **String** |  |  |
|**vorname** | **String** |  |  |
|**namenszusatz** | **String** |  |  [optional] |
|**typ** | **String** |  |  |
|**wahlperiode** | **Integer** | Wahlperiode des ersten zugehörigen Dokuments |  [optional] |
|**basisdatum** | **LocalDate** | Datum des ersten zugehörigen Dokuments |  [optional] |
|**datum** | **LocalDate** | Datum des letzten zugehörigen Dokuments |  [optional] |
|**aktualisiert** | **OffsetDateTime** | Letzte Aktualisierung der Entität |  |
|**titel** | **String** |  |  |
|**personRoles** | [**List&lt;PersonRole&gt;**](PersonRole.md) | Nebeneinträge mit bspw. abweichenden Funktionen oder Namensänderungen |  [optional] |



