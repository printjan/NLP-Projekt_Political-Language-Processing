# PlenarprotokolleApi

All URIs are relative to *https://search.dip.bundestag.de/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPlenarprotokoll**](PlenarprotokolleApi.md#getPlenarprotokoll) | **GET** /plenarprotokoll/{id} | Liefert Metadaten zu einem Plenarprotokoll |
| [**getPlenarprotokollList**](PlenarprotokolleApi.md#getPlenarprotokollList) | **GET** /plenarprotokoll | Liefert eine Liste von Metadaten zu Plenarprotokollen |
| [**getPlenarprotokollText**](PlenarprotokolleApi.md#getPlenarprotokollText) | **GET** /plenarprotokoll-text/{id} | Liefert Volltext und Metadaten zu einem Plenarprotokoll |
| [**getPlenarprotokollTextList**](PlenarprotokolleApi.md#getPlenarprotokollTextList) | **GET** /plenarprotokoll-text | Liefert eine Liste von Volltexten und Metadaten zu Plenarprotokollen |


<a id="getPlenarprotokoll"></a>
# **getPlenarprotokoll**
> Plenarprotokoll getPlenarprotokoll(id, format)

Liefert Metadaten zu einem Plenarprotokoll

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlenarprotokolleApi;

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

    PlenarprotokolleApi apiInstance = new PlenarprotokolleApi(defaultClient);
    Integer id = 1; // Integer | 
    String format = "json"; // String | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML.
    try {
      Plenarprotokoll result = apiInstance.getPlenarprotokoll(id, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlenarprotokolleApi#getPlenarprotokoll");
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

[**Plenarprotokoll**](Plenarprotokoll.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metadaten eines Plenarprotokolls |  -  |
| **401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |
| **404** | Die angefragte Entität wurde nicht gefunden |  -  |

<a id="getPlenarprotokollList"></a>
# **getPlenarprotokollList**
> PlenarprotokollListResponse getPlenarprotokollList(fAktualisiertStart, fAktualisiertEnd, fDatumStart, fDatumEnd, fDokumentnummer, fId, fVorgangstyp, fVorgangstypNotation, fWahlperiode, fZuordnung, cursor, format)

Liefert eine Liste von Metadaten zu Plenarprotokollen

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlenarprotokolleApi;

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

    PlenarprotokolleApi apiInstance = new PlenarprotokolleApi(defaultClient);
    OffsetDateTime fAktualisiertStart = OffsetDateTime.parse(""); // OffsetDateTime | Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum. 
    OffsetDateTime fAktualisiertEnd = OffsetDateTime.parse(""); // OffsetDateTime | Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum. 
    LocalDate fDatumStart = LocalDate.parse(""); // LocalDate | Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen. 
    LocalDate fDatumEnd = LocalDate.parse(""); // LocalDate | Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen. 
    List<String> fDokumentnummer = Arrays.asList(); // List<String> | Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren. Hinterlegt ist eine ODER-Suche. 
    List<Integer> fId = Arrays.asList(); // List<Integer> | ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren. 
    List<String> fVorgangstyp = Arrays.asList(); // List<String> | Vorgangstyp  Selektiert alle Entitäten, die dem angegebenen Vorgangstyp zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche. 
    List<Integer> fVorgangstypNotation = Arrays.asList(); // List<Integer> | Vorgangstyp-Notation  Selektiert alle Entitäten, die der angegebenen Vorgangstyp-Notation zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche. 
    List<Integer> fWahlperiode = Arrays.asList(); // List<Integer> | Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren. Hinterlegt ist eine ODER-Suche. 
    Zuordnung fZuordnung = Zuordnung.fromValue("BT"); // Zuordnung | Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer
    String cursor = "cursor_example"; // String | Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden. 
    String format = "json"; // String | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML.
    try {
      PlenarprotokollListResponse result = apiInstance.getPlenarprotokollList(fAktualisiertStart, fAktualisiertEnd, fDatumStart, fDatumEnd, fDokumentnummer, fId, fVorgangstyp, fVorgangstypNotation, fWahlperiode, fZuordnung, cursor, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlenarprotokolleApi#getPlenarprotokollList");
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
| **fId** | [**List&lt;Integer&gt;**](Integer.md)| ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren.  | [optional] |
| **fVorgangstyp** | [**List&lt;String&gt;**](String.md)| Vorgangstyp  Selektiert alle Entitäten, die dem angegebenen Vorgangstyp zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fVorgangstypNotation** | [**List&lt;Integer&gt;**](Integer.md)| Vorgangstyp-Notation  Selektiert alle Entitäten, die der angegebenen Vorgangstyp-Notation zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fWahlperiode** | [**List&lt;Integer&gt;**](Integer.md)| Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fZuordnung** | [**Zuordnung**](.md)| Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer | [optional] [enum: BT, BR, BV, EK] |
| **cursor** | **String**| Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden.  | [optional] |
| **format** | **String**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] [default to json] [enum: json, xml] |

### Return type

[**PlenarprotokollListResponse**](PlenarprotokollListResponse.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metadaten zu Plenarprotokollen |  -  |
| **400** | Syntaxfehler in einem der Anfrageparameter |  -  |
| **401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |

<a id="getPlenarprotokollText"></a>
# **getPlenarprotokollText**
> PlenarprotokollText getPlenarprotokollText(id, format)

Liefert Volltext und Metadaten zu einem Plenarprotokoll

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlenarprotokolleApi;

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

    PlenarprotokolleApi apiInstance = new PlenarprotokolleApi(defaultClient);
    Integer id = 1; // Integer | 
    String format = "json"; // String | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML.
    try {
      PlenarprotokollText result = apiInstance.getPlenarprotokollText(id, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlenarprotokolleApi#getPlenarprotokollText");
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

[**PlenarprotokollText**](PlenarprotokollText.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Volltext und Metadaten eines Plenarprotokolls |  -  |
| **401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |
| **404** | Die angefragte Entität wurde nicht gefunden |  -  |

<a id="getPlenarprotokollTextList"></a>
# **getPlenarprotokollTextList**
> PlenarprotokollTextListResponse getPlenarprotokollTextList(fAktualisiertStart, fAktualisiertEnd, fDatumStart, fDatumEnd, fDokumentnummer, fId, fVorgangstyp, fVorgangstypNotation, fWahlperiode, fZuordnung, cursor, format)

Liefert eine Liste von Volltexten und Metadaten zu Plenarprotokollen

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlenarprotokolleApi;

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

    PlenarprotokolleApi apiInstance = new PlenarprotokolleApi(defaultClient);
    OffsetDateTime fAktualisiertStart = OffsetDateTime.parse(""); // OffsetDateTime | Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum. 
    OffsetDateTime fAktualisiertEnd = OffsetDateTime.parse(""); // OffsetDateTime | Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum. 
    LocalDate fDatumStart = LocalDate.parse(""); // LocalDate | Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen. 
    LocalDate fDatumEnd = LocalDate.parse(""); // LocalDate | Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen. 
    List<String> fDokumentnummer = Arrays.asList(); // List<String> | Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren. Hinterlegt ist eine ODER-Suche. 
    List<Integer> fId = Arrays.asList(); // List<Integer> | ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren. 
    List<String> fVorgangstyp = Arrays.asList(); // List<String> | Vorgangstyp  Selektiert alle Entitäten, die dem angegebenen Vorgangstyp zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche. 
    List<Integer> fVorgangstypNotation = Arrays.asList(); // List<Integer> | Vorgangstyp-Notation  Selektiert alle Entitäten, die der angegebenen Vorgangstyp-Notation zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche. 
    List<Integer> fWahlperiode = Arrays.asList(); // List<Integer> | Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren. Hinterlegt ist eine ODER-Suche. 
    Zuordnung fZuordnung = Zuordnung.fromValue("BT"); // Zuordnung | Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer
    String cursor = "cursor_example"; // String | Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden. 
    String format = "json"; // String | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML.
    try {
      PlenarprotokollTextListResponse result = apiInstance.getPlenarprotokollTextList(fAktualisiertStart, fAktualisiertEnd, fDatumStart, fDatumEnd, fDokumentnummer, fId, fVorgangstyp, fVorgangstypNotation, fWahlperiode, fZuordnung, cursor, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlenarprotokolleApi#getPlenarprotokollTextList");
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
| **fId** | [**List&lt;Integer&gt;**](Integer.md)| ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren.  | [optional] |
| **fVorgangstyp** | [**List&lt;String&gt;**](String.md)| Vorgangstyp  Selektiert alle Entitäten, die dem angegebenen Vorgangstyp zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fVorgangstypNotation** | [**List&lt;Integer&gt;**](Integer.md)| Vorgangstyp-Notation  Selektiert alle Entitäten, die der angegebenen Vorgangstyp-Notation zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fWahlperiode** | [**List&lt;Integer&gt;**](Integer.md)| Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fZuordnung** | [**Zuordnung**](.md)| Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer | [optional] [enum: BT, BR, BV, EK] |
| **cursor** | **String**| Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden.  | [optional] |
| **format** | **String**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] [default to json] [enum: json, xml] |

### Return type

[**PlenarprotokollTextListResponse**](PlenarprotokollTextListResponse.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Volltext und Metadaten zu Plenarprotokollen |  -  |
| **400** | Syntaxfehler in einem der Anfrageparameter |  -  |
| **401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |

