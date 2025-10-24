# VorgangspositionenApi

All URIs are relative to *https://search.dip.bundestag.de/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVorgangsposition**](VorgangspositionenApi.md#getVorgangsposition) | **GET** /vorgangsposition/{id} | Liefert Metadaten zu einer Vorgangsposition |
| [**getVorgangspositionList**](VorgangspositionenApi.md#getVorgangspositionList) | **GET** /vorgangsposition | Liefert eine Liste von Metadaten zu Vorgangspositionen |


<a id="getVorgangsposition"></a>
# **getVorgangsposition**
> Vorgangsposition getVorgangsposition(id, format)

Liefert Metadaten zu einer Vorgangsposition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VorgangspositionenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://search.dip.bundestag.de/api/v1");
    
    // Configure API key authorization: ApiKeyHeader
    ApiKeyAuth ApiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyHeader");
    ApiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyHeader.setApiKeyPrefix("Token");

    // Configure API key authorization: ApiKeyQuery
    ApiKeyAuth ApiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyQuery");
    ApiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyQuery.setApiKeyPrefix("Token");

    VorgangspositionenApi apiInstance = new VorgangspositionenApi(defaultClient);
    Integer id = 1; // Integer | 
    String format = "json"; // String | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML.
    try {
      Vorgangsposition result = apiInstance.getVorgangsposition(id, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VorgangspositionenApi#getVorgangsposition");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **format** | **String**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] [default to json] [enum: json, xml] |

### Return type

[**Vorgangsposition**](Vorgangsposition.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metadaten einer Vorgangsposition |  -  |
| **401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |
| **404** | Die angefragte Entität wurde nicht gefunden |  -  |

<a id="getVorgangspositionList"></a>
# **getVorgangspositionList**
> VorgangspositionListResponse getVorgangspositionList(fAktivitaet, fAktualisiertStart, fAktualisiertEnd, fDatumStart, fDatumEnd, fDokumentart, fDokumentnummer, fDrucksache, fDrucksachetyp, fFrageNummer, fId, fPlenarprotokoll, fRessortFdf, fTitel, fUrheber, fVorgang, fVorgangstyp, fVorgangstypNotation, fWahlperiode, fZuordnung, cursor, format)

Liefert eine Liste von Metadaten zu Vorgangspositionen

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VorgangspositionenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://search.dip.bundestag.de/api/v1");
    
    // Configure API key authorization: ApiKeyHeader
    ApiKeyAuth ApiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyHeader");
    ApiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyHeader.setApiKeyPrefix("Token");

    // Configure API key authorization: ApiKeyQuery
    ApiKeyAuth ApiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyQuery");
    ApiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyQuery.setApiKeyPrefix("Token");

    VorgangspositionenApi apiInstance = new VorgangspositionenApi(defaultClient);
    Integer fAktivitaet = 56; // Integer | ID einer verknüpften Aktivität  Selektiert alle Entitäten, die mit der angegebenen Aktivität verknüpft sind. 
    OffsetDateTime fAktualisiertStart = OffsetDateTime.parse(""); // OffsetDateTime | Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum. 
    OffsetDateTime fAktualisiertEnd = OffsetDateTime.parse(""); // OffsetDateTime | Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum. 
    LocalDate fDatumStart = LocalDate.parse(""); // LocalDate | Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen. 
    LocalDate fDatumEnd = LocalDate.parse(""); // LocalDate | Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen. 
    String fDokumentart = "Drucksache"; // String | Drucksache oder Plenarprotokoll  Selektiert alle Entitäten, die mit der angegebenen Dokumentart verknüpft sind. 
    List<String> fDokumentnummer = Arrays.asList(); // List<String> | Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren. Hinterlegt ist eine ODER-Suche. 
    Integer fDrucksache = 56; // Integer | ID einer verknüpften Drucksache  Selektiert alle Entitäten, die mit der angegebenen Drucksache verknüpft sind. 
    String fDrucksachetyp = ""; // String | Typ der Drucksache  Selektiert alle Entitäten, die mit dem angegebenen Drucksachetyp verknüpft sind. 
    List<String> fFrageNummer = Arrays.asList(); // List<String> | Fragenummer/Listenziffer  Selektiert alle Entitäten, die mit der angegebenen Fragenummer in einer Drucksache verknüpft sind. Kann wiederholt werden, um mehrere Fragenummern zu selektieren. Hinterlegt ist eine ODER-Suche. 
    List<Integer> fId = Arrays.asList(); // List<Integer> | ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren. 
    Integer fPlenarprotokoll = 56; // Integer | ID eines verknüpften Plenarprotokolls  Selektiert alle Entitäten, die mit dem angegebenen Plenarprotokoll verknüpft sind. 
    List<String> fRessortFdf = Arrays.asList(); // List<String> | Ressort (federführend)  Selektiert alle Entitäten, die mit dem angegebenen federführenden Ressort in einer Drucksache verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Ressorts zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere federführende Ressorts ist mit einer einzigen Abfrage nicht möglich. Die federführenden Ressorts müssen dazu einzeln abgefragt werden. 
    List<String> fTitel = Arrays.asList(); // List<String> | Titel  Selektiert alle Entitäten, die den angegebenen Suchbegriff im Titel enthalten. Kann wiederholt werden, um mehrere Titel zu selektieren. Hinterlegt ist eine ODER-Suche. Eine Einzelwortsuche ist möglich. Mehrere Suchbegriffe hintereinander werden als Phrase gesucht. 
    List<String> fUrheber = Arrays.asList(); // List<String> | Urheber  Selektiert alle Entitäten, die mit dem angegebenen Urheber in einer Drucksache verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Urheber zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere Urheber ist mit einer einzigen Abfrage nicht möglich. Die Urheber müssen dazu einzeln abgefragt werden. 
    Integer fVorgang = 56; // Integer | ID eines verknüpften Vorgangs  Selektiert alle Entitäten, die mit dem angegebenen Vorgang verknüpft sind. 
    List<String> fVorgangstyp = Arrays.asList(); // List<String> | Vorgangstyp  Selektiert alle Entitäten, die dem angegebenen Vorgangstyp zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche. 
    List<Integer> fVorgangstypNotation = Arrays.asList(); // List<Integer> | Vorgangstyp-Notation  Selektiert alle Entitäten, die der angegebenen Vorgangstyp-Notation zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche. 
    List<Integer> fWahlperiode = Arrays.asList(); // List<Integer> | Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren. Hinterlegt ist eine ODER-Suche. 
    Zuordnung fZuordnung = Zuordnung.fromValue("BT"); // Zuordnung | Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer
    String cursor = "cursor_example"; // String | Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden. 
    String format = "json"; // String | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML.
    try {
      VorgangspositionListResponse result = apiInstance.getVorgangspositionList(fAktivitaet, fAktualisiertStart, fAktualisiertEnd, fDatumStart, fDatumEnd, fDokumentart, fDokumentnummer, fDrucksache, fDrucksachetyp, fFrageNummer, fId, fPlenarprotokoll, fRessortFdf, fTitel, fUrheber, fVorgang, fVorgangstyp, fVorgangstypNotation, fWahlperiode, fZuordnung, cursor, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VorgangspositionenApi#getVorgangspositionList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fAktivitaet** | **Integer**| ID einer verknüpften Aktivität  Selektiert alle Entitäten, die mit der angegebenen Aktivität verknüpft sind.  | [optional] |
| **fAktualisiertStart** | **OffsetDateTime**| Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  | [optional] |
| **fAktualisiertEnd** | **OffsetDateTime**| Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  | [optional] |
| **fDatumStart** | **LocalDate**| Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  | [optional] |
| **fDatumEnd** | **LocalDate**| Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  | [optional] |
| **fDokumentart** | **String**| Drucksache oder Plenarprotokoll  Selektiert alle Entitäten, die mit der angegebenen Dokumentart verknüpft sind.  | [optional] [enum: Drucksache, Plenarprotokoll] |
| **fDokumentnummer** | [**List&lt;String&gt;**](String.md)| Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fDrucksache** | **Integer**| ID einer verknüpften Drucksache  Selektiert alle Entitäten, die mit der angegebenen Drucksache verknüpft sind.  | [optional] |
| **fDrucksachetyp** | **String**| Typ der Drucksache  Selektiert alle Entitäten, die mit dem angegebenen Drucksachetyp verknüpft sind.  | [optional] |
| **fFrageNummer** | [**List&lt;String&gt;**](String.md)| Fragenummer/Listenziffer  Selektiert alle Entitäten, die mit der angegebenen Fragenummer in einer Drucksache verknüpft sind. Kann wiederholt werden, um mehrere Fragenummern zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fId** | [**List&lt;Integer&gt;**](Integer.md)| ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren.  | [optional] |
| **fPlenarprotokoll** | **Integer**| ID eines verknüpften Plenarprotokolls  Selektiert alle Entitäten, die mit dem angegebenen Plenarprotokoll verknüpft sind.  | [optional] |
| **fRessortFdf** | [**List&lt;String&gt;**](String.md)| Ressort (federführend)  Selektiert alle Entitäten, die mit dem angegebenen federführenden Ressort in einer Drucksache verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Ressorts zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere federführende Ressorts ist mit einer einzigen Abfrage nicht möglich. Die federführenden Ressorts müssen dazu einzeln abgefragt werden.  | [optional] |
| **fTitel** | [**List&lt;String&gt;**](String.md)| Titel  Selektiert alle Entitäten, die den angegebenen Suchbegriff im Titel enthalten. Kann wiederholt werden, um mehrere Titel zu selektieren. Hinterlegt ist eine ODER-Suche. Eine Einzelwortsuche ist möglich. Mehrere Suchbegriffe hintereinander werden als Phrase gesucht.  | [optional] |
| **fUrheber** | [**List&lt;String&gt;**](String.md)| Urheber  Selektiert alle Entitäten, die mit dem angegebenen Urheber in einer Drucksache verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Urheber zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere Urheber ist mit einer einzigen Abfrage nicht möglich. Die Urheber müssen dazu einzeln abgefragt werden.  | [optional] |
| **fVorgang** | **Integer**| ID eines verknüpften Vorgangs  Selektiert alle Entitäten, die mit dem angegebenen Vorgang verknüpft sind.  | [optional] |
| **fVorgangstyp** | [**List&lt;String&gt;**](String.md)| Vorgangstyp  Selektiert alle Entitäten, die dem angegebenen Vorgangstyp zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fVorgangstypNotation** | [**List&lt;Integer&gt;**](Integer.md)| Vorgangstyp-Notation  Selektiert alle Entitäten, die der angegebenen Vorgangstyp-Notation zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fWahlperiode** | [**List&lt;Integer&gt;**](Integer.md)| Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fZuordnung** | [**Zuordnung**](.md)| Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer | [optional] [enum: BT, BR, BV, EK] |
| **cursor** | **String**| Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden.  | [optional] |
| **format** | **String**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] [default to json] [enum: json, xml] |

### Return type

[**VorgangspositionListResponse**](VorgangspositionListResponse.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metadaten zu Vorgangspositionen |  -  |
| **400** | Syntaxfehler in einem der Anfrageparameter |  -  |
| **401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |

