# AktivittenApi

All URIs are relative to *https://search.dip.bundestag.de/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAktivitaet**](AktivittenApi.md#getAktivitaet) | **GET** /aktivitaet/{id} | Liefert Metadaten zu einer Aktivität |
| [**getAktivitaetList**](AktivittenApi.md#getAktivitaetList) | **GET** /aktivitaet | Liefert eine Liste von Metadaten zu Aktivitäten |


<a id="getAktivitaet"></a>
# **getAktivitaet**
> Aktivitaet getAktivitaet(id, format)

Liefert Metadaten zu einer Aktivität

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AktivittenApi;

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

    AktivittenApi apiInstance = new AktivittenApi(defaultClient);
    Integer id = 1; // Integer | 
    String format = "json"; // String | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML.
    try {
      Aktivitaet result = apiInstance.getAktivitaet(id, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AktivittenApi#getAktivitaet");
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

[**Aktivitaet**](Aktivitaet.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metadaten einer Aktivität |  -  |
| **401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |
| **404** | Die angefragte Entität wurde nicht gefunden |  -  |

<a id="getAktivitaetList"></a>
# **getAktivitaetList**
> AktivitaetListResponse getAktivitaetList(fAktualisiertStart, fAktualisiertEnd, fDatumStart, fDatumEnd, fDeskriptor, fDokumentart, fDokumentnummer, fDrucksache, fDrucksachetyp, fFrageNummer, fId, fPlenarprotokoll, fSachgebiet, fUrheber, fVorgangstyp, fVorgangstypNotation, fWahlperiode, fZuordnung, cursor, format)

Liefert eine Liste von Metadaten zu Aktivitäten

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AktivittenApi;

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

    AktivittenApi apiInstance = new AktivittenApi(defaultClient);
    OffsetDateTime fAktualisiertStart = OffsetDateTime.parse(""); // OffsetDateTime | Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum. 
    OffsetDateTime fAktualisiertEnd = OffsetDateTime.parse(""); // OffsetDateTime | Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum. 
    LocalDate fDatumStart = LocalDate.parse(""); // LocalDate | Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen. 
    LocalDate fDatumEnd = LocalDate.parse(""); // LocalDate | Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen. 
    List<String> fDeskriptor = Arrays.asList(); // List<String> | Deskriptor  Selektiert alle Entitäten, die mit dem angegebenen Deskriptor verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Deskriptoren zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere Deskriptoren ist mit einer einzigen Abfrage nicht möglich. Die Deskriptoren müssen dazu einzeln abgefragt werden. 
    String fDokumentart = "Drucksache"; // String | Drucksache oder Plenarprotokoll  Selektiert alle Entitäten, die mit der angegebenen Dokumentart verknüpft sind. 
    List<String> fDokumentnummer = Arrays.asList(); // List<String> | Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren. Hinterlegt ist eine ODER-Suche. 
    Integer fDrucksache = 56; // Integer | ID einer verknüpften Drucksache  Selektiert alle Entitäten, die mit der angegebenen Drucksache verknüpft sind. 
    String fDrucksachetyp = ""; // String | Typ der Drucksache  Selektiert alle Entitäten, die mit dem angegebenen Drucksachetyp verknüpft sind. 
    List<String> fFrageNummer = Arrays.asList(); // List<String> | Fragenummer/Listenziffer  Selektiert alle Entitäten, die mit der angegebenen Fragenummer in einer Drucksache verknüpft sind. Kann wiederholt werden, um mehrere Fragenummern zu selektieren. Hinterlegt ist eine ODER-Suche. 
    List<Integer> fId = Arrays.asList(); // List<Integer> | ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren. 
    Integer fPlenarprotokoll = 56; // Integer | ID eines verknüpften Plenarprotokolls  Selektiert alle Entitäten, die mit dem angegebenen Plenarprotokoll verknüpft sind. 
    List<String> fSachgebiet = Arrays.asList(); // List<String> | Sachgebiet  Selektiert alle Entitäten, die mit dem angegebenen Sachgebiet verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Sachgebiete zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere Sachgebiete ist mit einer einzigen Abfrage nicht möglich. Die Sachgebiete müssen dazu einzeln abgefragt werden. 
    List<String> fUrheber = Arrays.asList(); // List<String> | Urheber  Selektiert alle Entitäten, die mit dem angegebenen Urheber in einer Drucksache verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Urheber zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere Urheber ist mit einer einzigen Abfrage nicht möglich. Die Urheber müssen dazu einzeln abgefragt werden. 
    List<String> fVorgangstyp = Arrays.asList(); // List<String> | Vorgangstyp  Selektiert alle Entitäten, die dem angegebenen Vorgangstyp zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche. 
    List<Integer> fVorgangstypNotation = Arrays.asList(); // List<Integer> | Vorgangstyp-Notation  Selektiert alle Entitäten, die der angegebenen Vorgangstyp-Notation zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche. 
    List<Integer> fWahlperiode = Arrays.asList(); // List<Integer> | Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren. Hinterlegt ist eine ODER-Suche. 
    Zuordnung fZuordnung = Zuordnung.fromValue("BT"); // Zuordnung | Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer
    String cursor = "cursor_example"; // String | Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden. 
    String format = "json"; // String | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML.
    try {
      AktivitaetListResponse result = apiInstance.getAktivitaetList(fAktualisiertStart, fAktualisiertEnd, fDatumStart, fDatumEnd, fDeskriptor, fDokumentart, fDokumentnummer, fDrucksache, fDrucksachetyp, fFrageNummer, fId, fPlenarprotokoll, fSachgebiet, fUrheber, fVorgangstyp, fVorgangstypNotation, fWahlperiode, fZuordnung, cursor, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AktivittenApi#getAktivitaetList");
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
| **fDeskriptor** | [**List&lt;String&gt;**](String.md)| Deskriptor  Selektiert alle Entitäten, die mit dem angegebenen Deskriptor verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Deskriptoren zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere Deskriptoren ist mit einer einzigen Abfrage nicht möglich. Die Deskriptoren müssen dazu einzeln abgefragt werden.  | [optional] |
| **fDokumentart** | **String**| Drucksache oder Plenarprotokoll  Selektiert alle Entitäten, die mit der angegebenen Dokumentart verknüpft sind.  | [optional] [enum: Drucksache, Plenarprotokoll] |
| **fDokumentnummer** | [**List&lt;String&gt;**](String.md)| Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fDrucksache** | **Integer**| ID einer verknüpften Drucksache  Selektiert alle Entitäten, die mit der angegebenen Drucksache verknüpft sind.  | [optional] |
| **fDrucksachetyp** | **String**| Typ der Drucksache  Selektiert alle Entitäten, die mit dem angegebenen Drucksachetyp verknüpft sind.  | [optional] |
| **fFrageNummer** | [**List&lt;String&gt;**](String.md)| Fragenummer/Listenziffer  Selektiert alle Entitäten, die mit der angegebenen Fragenummer in einer Drucksache verknüpft sind. Kann wiederholt werden, um mehrere Fragenummern zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fId** | [**List&lt;Integer&gt;**](Integer.md)| ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren.  | [optional] |
| **fPlenarprotokoll** | **Integer**| ID eines verknüpften Plenarprotokolls  Selektiert alle Entitäten, die mit dem angegebenen Plenarprotokoll verknüpft sind.  | [optional] |
| **fSachgebiet** | [**List&lt;String&gt;**](String.md)| Sachgebiet  Selektiert alle Entitäten, die mit dem angegebenen Sachgebiet verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Sachgebiete zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere Sachgebiete ist mit einer einzigen Abfrage nicht möglich. Die Sachgebiete müssen dazu einzeln abgefragt werden.  | [optional] |
| **fUrheber** | [**List&lt;String&gt;**](String.md)| Urheber  Selektiert alle Entitäten, die mit dem angegebenen Urheber in einer Drucksache verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Urheber zu selektieren. Hinterlegt ist eine UND-Suche.  Eine ODER-Suche über mehrere Urheber ist mit einer einzigen Abfrage nicht möglich. Die Urheber müssen dazu einzeln abgefragt werden.  | [optional] |
| **fVorgangstyp** | [**List&lt;String&gt;**](String.md)| Vorgangstyp  Selektiert alle Entitäten, die dem angegebenen Vorgangstyp zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fVorgangstypNotation** | [**List&lt;Integer&gt;**](Integer.md)| Vorgangstyp-Notation  Selektiert alle Entitäten, die der angegebenen Vorgangstyp-Notation zugeordnet sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fWahlperiode** | [**List&lt;Integer&gt;**](Integer.md)| Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren. Hinterlegt ist eine ODER-Suche.  | [optional] |
| **fZuordnung** | [**Zuordnung**](.md)| Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer | [optional] [enum: BT, BR, BV, EK] |
| **cursor** | **String**| Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden.  | [optional] |
| **format** | **String**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] [default to json] [enum: json, xml] |

### Return type

[**AktivitaetListResponse**](AktivitaetListResponse.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metadaten zu Aktivitäten |  -  |
| **400** | Syntaxfehler in einem der Anfrageparameter |  -  |
| **401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |

