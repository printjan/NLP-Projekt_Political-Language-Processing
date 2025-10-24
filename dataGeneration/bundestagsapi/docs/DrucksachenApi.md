# DrucksachenApi

All URIs are relative to *https://search.dip.bundestag.de/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDrucksache**](DrucksachenApi.md#getDrucksache) | **GET** /drucksache/{id} | Liefert Metadaten zu einer Drucksache |
| [**getDrucksacheList**](DrucksachenApi.md#getDrucksacheList) | **GET** /drucksache | Liefert eine Liste von Metadaten zu Drucksachen |
| [**getDrucksacheText**](DrucksachenApi.md#getDrucksacheText) | **GET** /drucksache-text/{id} | Liefert Volltext und Metadaten zu einer Drucksache |
| [**getDrucksacheTextList**](DrucksachenApi.md#getDrucksacheTextList) | **GET** /drucksache-text | Liefert eine Liste von Volltexten und Metadaten zu Drucksachen |


<a id="getDrucksache"></a>
# **getDrucksache**
> Drucksache getDrucksache(id, format)

Liefert Metadaten zu einer Drucksache

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DrucksachenApi;

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

    DrucksachenApi apiInstance = new DrucksachenApi(defaultClient);
    Integer id = 1; // Integer | 
    String format = "json"; // String | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML.
    try {
      Drucksache result = apiInstance.getDrucksache(id, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DrucksachenApi#getDrucksache");
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

[**Drucksache**](Drucksache.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metadaten einer Drucksache |  -  |
| **401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |
| **404** | Die angefragte Entität wurde nicht gefunden |  -  |

<a id="getDrucksacheList"></a>
# **getDrucksacheList**
> DrucksacheListResponse getDrucksacheList(fAktualisiertStart, fAktualisiertEnd, fDatumStart, fDatumEnd, fDokumentnummer, fDrucksachetyp, fId, fRessortFdf, fTitel, fUrheber, fVorgangstyp, fVorgangstypNotation, fWahlperiode, fZuordnung, cursor, format)

Liefert eine Liste von Metadaten zu Drucksachen

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DrucksachenApi;

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

    DrucksachenApi apiInstance = new DrucksachenApi(defaultClient);
    OffsetDateTime fAktualisiertStart = OffsetDateTime.parse(""); // OffsetDateTime | Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum. 
    OffsetDateTime fAktualisiertEnd = OffsetDateTime.parse(""); // OffsetDateTime | Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum. 
    LocalDate fDatumStart = LocalDate.parse(""); // LocalDate | Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen. 
    LocalDate fDatumEnd = LocalDate.parse(""); // LocalDate | Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen. 
    List<String> fDokumentnummer = Arrays.asList(); // List<String> | Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren. Hinterlegt ist eine ODER-Suche. 
    String fDrucksachetyp = ""; // String | Typ der Drucksache  Selektiert alle Entitäten, die mit dem angegebenen Drucksachetyp verknüpft sind. 
    List<Integer> fId = Arrays.asList(); // List<Integer> | ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren. 
    List<String> fRessortFdf = Arrays.asList(); // List<String> | Ressort (federführend)  Selektiert alle Entitäten, die mit dem angegebenen federführenden Ressort in einer Drucksache verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Ressorts zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere federführende Ressorts ist mit einer einzigen Abfrage nicht möglich. Die federführenden Ressorts müssen dazu einzeln abgefragt werden. 
    List<String> fTitel = Arrays.asList(); // List<String> | Titel  Selektiert alle Entitäten, die den angegebenen Suchbegriff im Titel enthalten. Kann wiederholt werden, um mehrere Titel zu selektieren. Hinterlegt ist eine ODER-Suche. Eine Einzelwortsuche ist möglich. Mehrere Suchbegriffe hintereinander werden als Phrase gesucht. 
    List<String> fUrheber = Arrays.asList(); // List<String> | Urheber  Selektiert alle Entitäten, die mit dem angegebenen Urheber in einer Drucksache verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Urheber zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere Urheber ist mit einer einzigen Abfrage nicht möglich. Die Urheber müssen dazu einzeln abgefragt werden. 
    List<String> fVorgangstyp = Arrays.asList(); // List<String> | Vorgangstyp  Selektiert alle Entitäten, die dem angegebenen Vorgangstyp zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche. 
    List<Integer> fVorgangstypNotation = Arrays.asList(); // List<Integer> | Vorgangstyp-Notation  Selektiert alle Entitäten, die der angegebenen Vorgangstyp-Notation zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche. 
    List<Integer> fWahlperiode = Arrays.asList(); // List<Integer> | Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren. Hinterlegt ist eine ODER-Suche. 
    Zuordnung fZuordnung = Zuordnung.fromValue("BT"); // Zuordnung | Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer
    String cursor = "cursor_example"; // String | Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden. 
    String format = "json"; // String | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML.
    try {
      DrucksacheListResponse result = apiInstance.getDrucksacheList(fAktualisiertStart, fAktualisiertEnd, fDatumStart, fDatumEnd, fDokumentnummer, fDrucksachetyp, fId, fRessortFdf, fTitel, fUrheber, fVorgangstyp, fVorgangstypNotation, fWahlperiode, fZuordnung, cursor, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DrucksachenApi#getDrucksacheList");
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
| **fAktualisiertStart** | **OffsetDateTime**| Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  | [optional] |
| **fAktualisiertEnd** | **OffsetDateTime**| Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  | [optional] |
| **fDatumStart** | **LocalDate**| Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  | [optional] |
| **fDatumEnd** | **LocalDate**| Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  | [optional] |
| **fDokumentnummer** | [**List&lt;String&gt;**](String.md)| Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fDrucksachetyp** | **String**| Typ der Drucksache  Selektiert alle Entitäten, die mit dem angegebenen Drucksachetyp verknüpft sind.  | [optional] |
| **fId** | [**List&lt;Integer&gt;**](Integer.md)| ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren.  | [optional] |
| **fRessortFdf** | [**List&lt;String&gt;**](String.md)| Ressort (federführend)  Selektiert alle Entitäten, die mit dem angegebenen federführenden Ressort in einer Drucksache verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Ressorts zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere federführende Ressorts ist mit einer einzigen Abfrage nicht möglich. Die federführenden Ressorts müssen dazu einzeln abgefragt werden.  | [optional] |
| **fTitel** | [**List&lt;String&gt;**](String.md)| Titel  Selektiert alle Entitäten, die den angegebenen Suchbegriff im Titel enthalten. Kann wiederholt werden, um mehrere Titel zu selektieren. Hinterlegt ist eine ODER-Suche. Eine Einzelwortsuche ist möglich. Mehrere Suchbegriffe hintereinander werden als Phrase gesucht.  | [optional] |
| **fUrheber** | [**List&lt;String&gt;**](String.md)| Urheber  Selektiert alle Entitäten, die mit dem angegebenen Urheber in einer Drucksache verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Urheber zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere Urheber ist mit einer einzigen Abfrage nicht möglich. Die Urheber müssen dazu einzeln abgefragt werden.  | [optional] |
| **fVorgangstyp** | [**List&lt;String&gt;**](String.md)| Vorgangstyp  Selektiert alle Entitäten, die dem angegebenen Vorgangstyp zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fVorgangstypNotation** | [**List&lt;Integer&gt;**](Integer.md)| Vorgangstyp-Notation  Selektiert alle Entitäten, die der angegebenen Vorgangstyp-Notation zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fWahlperiode** | [**List&lt;Integer&gt;**](Integer.md)| Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fZuordnung** | [**Zuordnung**](.md)| Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer | [optional] [enum: BT, BR, BV, EK] |
| **cursor** | **String**| Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden.  | [optional] |
| **format** | **String**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] [default to json] [enum: json, xml] |

### Return type

[**DrucksacheListResponse**](DrucksacheListResponse.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metadaten zu Drucksachen |  -  |
| **400** | Syntaxfehler in einem der Anfrageparameter |  -  |
| **401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |

<a id="getDrucksacheText"></a>
# **getDrucksacheText**
> DrucksacheText getDrucksacheText(id, format)

Liefert Volltext und Metadaten zu einer Drucksache

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DrucksachenApi;

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

    DrucksachenApi apiInstance = new DrucksachenApi(defaultClient);
    Integer id = 1; // Integer | 
    String format = "json"; // String | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML.
    try {
      DrucksacheText result = apiInstance.getDrucksacheText(id, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DrucksachenApi#getDrucksacheText");
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

[**DrucksacheText**](DrucksacheText.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Volltext und Metadaten einer Drucksache |  -  |
| **401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |
| **404** | Die angefragte Entität wurde nicht gefunden |  -  |

<a id="getDrucksacheTextList"></a>
# **getDrucksacheTextList**
> DrucksacheTextListResponse getDrucksacheTextList(fAktualisiertStart, fAktualisiertEnd, fDatumStart, fDatumEnd, fDokumentnummer, fDrucksachetyp, fId, fRessortFdf, fTitel, fUrheber, fVorgangstyp, fVorgangstypNotation, fWahlperiode, fZuordnung, cursor, format)

Liefert eine Liste von Volltexten und Metadaten zu Drucksachen

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DrucksachenApi;

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

    DrucksachenApi apiInstance = new DrucksachenApi(defaultClient);
    OffsetDateTime fAktualisiertStart = OffsetDateTime.parse(""); // OffsetDateTime | Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum. 
    OffsetDateTime fAktualisiertEnd = OffsetDateTime.parse(""); // OffsetDateTime | Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum. 
    LocalDate fDatumStart = LocalDate.parse(""); // LocalDate | Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen. 
    LocalDate fDatumEnd = LocalDate.parse(""); // LocalDate | Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen. 
    List<String> fDokumentnummer = Arrays.asList(); // List<String> | Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren. Hinterlegt ist eine ODER-Suche. 
    String fDrucksachetyp = ""; // String | Typ der Drucksache  Selektiert alle Entitäten, die mit dem angegebenen Drucksachetyp verknüpft sind. 
    List<Integer> fId = Arrays.asList(); // List<Integer> | ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren. 
    List<String> fRessortFdf = Arrays.asList(); // List<String> | Ressort (federführend)  Selektiert alle Entitäten, die mit dem angegebenen federführenden Ressort in einer Drucksache verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Ressorts zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere federführende Ressorts ist mit einer einzigen Abfrage nicht möglich. Die federführenden Ressorts müssen dazu einzeln abgefragt werden. 
    List<String> fTitel = Arrays.asList(); // List<String> | Titel  Selektiert alle Entitäten, die den angegebenen Suchbegriff im Titel enthalten. Kann wiederholt werden, um mehrere Titel zu selektieren. Hinterlegt ist eine ODER-Suche. Eine Einzelwortsuche ist möglich. Mehrere Suchbegriffe hintereinander werden als Phrase gesucht. 
    List<String> fUrheber = Arrays.asList(); // List<String> | Urheber  Selektiert alle Entitäten, die mit dem angegebenen Urheber in einer Drucksache verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Urheber zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere Urheber ist mit einer einzigen Abfrage nicht möglich. Die Urheber müssen dazu einzeln abgefragt werden. 
    List<String> fVorgangstyp = Arrays.asList(); // List<String> | Vorgangstyp  Selektiert alle Entitäten, die dem angegebenen Vorgangstyp zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche. 
    List<Integer> fVorgangstypNotation = Arrays.asList(); // List<Integer> | Vorgangstyp-Notation  Selektiert alle Entitäten, die der angegebenen Vorgangstyp-Notation zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche. 
    List<Integer> fWahlperiode = Arrays.asList(); // List<Integer> | Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren. Hinterlegt ist eine ODER-Suche. 
    Zuordnung fZuordnung = Zuordnung.fromValue("BT"); // Zuordnung | Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer
    String cursor = "cursor_example"; // String | Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden. 
    String format = "json"; // String | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML.
    try {
      DrucksacheTextListResponse result = apiInstance.getDrucksacheTextList(fAktualisiertStart, fAktualisiertEnd, fDatumStart, fDatumEnd, fDokumentnummer, fDrucksachetyp, fId, fRessortFdf, fTitel, fUrheber, fVorgangstyp, fVorgangstypNotation, fWahlperiode, fZuordnung, cursor, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DrucksachenApi#getDrucksacheTextList");
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
| **fAktualisiertStart** | **OffsetDateTime**| Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  | [optional] |
| **fAktualisiertEnd** | **OffsetDateTime**| Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  | [optional] |
| **fDatumStart** | **LocalDate**| Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  | [optional] |
| **fDatumEnd** | **LocalDate**| Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  | [optional] |
| **fDokumentnummer** | [**List&lt;String&gt;**](String.md)| Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fDrucksachetyp** | **String**| Typ der Drucksache  Selektiert alle Entitäten, die mit dem angegebenen Drucksachetyp verknüpft sind.  | [optional] |
| **fId** | [**List&lt;Integer&gt;**](Integer.md)| ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren.  | [optional] |
| **fRessortFdf** | [**List&lt;String&gt;**](String.md)| Ressort (federführend)  Selektiert alle Entitäten, die mit dem angegebenen federführenden Ressort in einer Drucksache verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Ressorts zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere federführende Ressorts ist mit einer einzigen Abfrage nicht möglich. Die federführenden Ressorts müssen dazu einzeln abgefragt werden.  | [optional] |
| **fTitel** | [**List&lt;String&gt;**](String.md)| Titel  Selektiert alle Entitäten, die den angegebenen Suchbegriff im Titel enthalten. Kann wiederholt werden, um mehrere Titel zu selektieren. Hinterlegt ist eine ODER-Suche. Eine Einzelwortsuche ist möglich. Mehrere Suchbegriffe hintereinander werden als Phrase gesucht.  | [optional] |
| **fUrheber** | [**List&lt;String&gt;**](String.md)| Urheber  Selektiert alle Entitäten, die mit dem angegebenen Urheber in einer Drucksache verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Urheber zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere Urheber ist mit einer einzigen Abfrage nicht möglich. Die Urheber müssen dazu einzeln abgefragt werden.  | [optional] |
| **fVorgangstyp** | [**List&lt;String&gt;**](String.md)| Vorgangstyp  Selektiert alle Entitäten, die dem angegebenen Vorgangstyp zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fVorgangstypNotation** | [**List&lt;Integer&gt;**](Integer.md)| Vorgangstyp-Notation  Selektiert alle Entitäten, die der angegebenen Vorgangstyp-Notation zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fWahlperiode** | [**List&lt;Integer&gt;**](Integer.md)| Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fZuordnung** | [**Zuordnung**](.md)| Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer | [optional] [enum: BT, BR, BV, EK] |
| **cursor** | **String**| Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden.  | [optional] |
| **format** | **String**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] [default to json] [enum: json, xml] |

### Return type

[**DrucksacheTextListResponse**](DrucksacheTextListResponse.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Volltext und Metadaten zu Drucksachen |  -  |
| **400** | Syntaxfehler in einem der Anfrageparameter |  -  |
| **401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |

