

# Vorgangsposition

Liefert Metadaten zu einer Vorgangsposition (Vorgangsschritt).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**vorgangsposition** | **String** |  |  |
|**zuordnung** | **Zuordnung** |  |  |
|**gang** | **Boolean** | Alle Vorgangsschritte, die von besonderer Bedeutung für den Fortgang der Beratung sind, werden durch das Attribut &#x60;gang: true&#x60; gekennzeichnet.  Ist ein solcher Vorgangsschritt mit einer Drucksache verknüpft, werden im Frontend unter der Benennung \&quot;Wichtige Drucksachen\&quot; Herausgeber, Nummer und Typ sowie das Datum der entsprechenden Drucksachen ausgegeben (z.B. BT-Drs 18/13014 (Beschlussempfehlung), 28.06.2017).  Ist er mit einem Plenarprotokoll verknüpft, werden im Frontend unter der Benennung \&quot;Plenum\&quot; der Klartext der Vorgangsposition, Datum, Herausgeber und Nummer des Plenarprotokolls mit Anfangsseite/Quadrant und Endseite/Quadrant dargestellt (z.B. 2. Beratung: 29.06.2017, BT-PlPr 18/243, S. 24964C - 24973C).  |  |
|**fortsetzung** | **Boolean** | Erstreckt sich eine Beratung über mehrere Plenarprotokolle, so müssen entsprechend viele Vorgangsschritte mit je gleicher Vorgangsposition im Vorgangsablauf angelegt werden. Der zweite und jeder weitere dieser Schritte wird dann als \&quot;Fortsetzung\&quot; gekennzeichnet (Attribut &#x60;fortsetzung: true&#x60;).  Für die Beratung des Gesetzentwurfs für die Feststellung des Haushaltsplanes (Haushaltsberatungen) gelten abweichende Regelungen.  |  |
|**nachtrag** | **Boolean** | Eine Auswertungseinheit eines Plenarprotokolls kann nur an genau einen Vorgangsschritt angebunden werden.  Müssen aber mehrere Auswertungseinheiten für einen Vorgangsschritt gebildet werden (weil die Ergänzung einer Rede erst in einem späteren Protokoll erscheint oder weil sich z.B. bei einer Verbundenen Beratung (§ 24 GO-BT) nicht alle Schriftlichen Erklärungen nach § 31 GO-BT auf sämtliche Vorlagen beziehen),  dann müssen im Vorgangsablauf mehrere Vorgangsschritte mit der gleichen Vorgangsposition angelegt werden. Der zweite und jeder weitere dieser Schritte wird dann als \&quot;Nachtrag\&quot; gekennzeichnet (Attribut &#x60;nachtrag: true&#x60;)  |  |
|**vorgangstyp** | **String** | Vorgangstyp des zugehörigen Vorgangs |  |
|**typ** | [**TypEnum**](#TypEnum) |  |  |
|**titel** | **String** | Titel des zugehörigen Vorgangs |  |
|**dokumentart** | [**DokumentartEnum**](#DokumentartEnum) |  |  |
|**vorgangId** | **String** | ID des zugehörigen Vorgangs |  |
|**datum** | **LocalDate** | Datum des zugehörigen Dokuments |  |
|**aktualisiert** | **OffsetDateTime** | Letzte Aktualisierung der Entität oder des zugehörigen Dokuments |  |
|**fundstelle** | [**Fundstelle**](Fundstelle.md) |  |  |
|**urheber** | [**List&lt;Urheber&gt;**](Urheber.md) |  |  [optional] |
|**ueberweisung** | [**List&lt;Ueberweisung&gt;**](Ueberweisung.md) |  |  [optional] |
|**aktivitaetAnzeige** | [**List&lt;AktivitaetAnzeige&gt;**](AktivitaetAnzeige.md) | Zusammenfassung der ersten 4 zur Anzeige vorgesehenen Aktivitäten |  [optional] |
|**aktivitaetAnzahl** | **Integer** | Gesamtzahl der zugehörigen Aktivitäten |  |
|**ressort** | [**List&lt;Ressort&gt;**](Ressort.md) |  |  [optional] |
|**beschlussfassung** | [**List&lt;Beschlussfassung&gt;**](Beschlussfassung.md) |  |  [optional] |
|**ratsdok** | **String** | Ratsdok-Nr. |  [optional] |
|**kom** | **String** | KOM-Nr. |  [optional] |
|**sek** | **String** | SEK-Nr. |  [optional] |
|**mitberaten** | [**List&lt;Vorgangspositionbezug&gt;**](Vorgangspositionbezug.md) | Es ist eine häufig geübte Praxis, mehrere thematisch verwandte Vorlagen (z.B. konkurrierende Anträge der verschiedenen Fraktionen zum Thema Diesel-Fahrverbote) in einer Debatte gemeinsam zu beraten (\&quot;Zusammenberatung\&quot;).  &#x60;mitberaten&#x60; liefert, von einem Vorgang ausgehend, alle anderen Vorgänge, die Gegenstand der Zusammenberatung sind.  |  [optional] |
|**_abstract** | **String** |  |  [optional] |



## Enum: TypEnum

| Name | Value |
|---- | -----|
| VORGANGSPOSITION | &quot;Vorgangsposition&quot; |



## Enum: DokumentartEnum

| Name | Value |
|---- | -----|
| DRUCKSACHE | &quot;Drucksache&quot; |
| PLENARPROTOKOLL | &quot;Plenarprotokoll&quot; |



