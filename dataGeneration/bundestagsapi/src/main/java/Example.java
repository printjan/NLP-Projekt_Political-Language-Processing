// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.AktivittenApi;

public class Example {
    public static void example() {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://search.dip.bundestag.de/api/v1");

        // Configure API key authorization: ApiKeyHeader
        ApiKeyAuth ApiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyHeader");
        ApiKeyHeader.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //ApiKeyHeader.setApiKeyPrefix("Token");

        // Configure API key authorization: ApiKeyQuery
        ApiKeyAuth ApiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyQuery");
        ApiKeyQuery.setApiKey("I9FKdCn.hbfefNWCY336dL6x62vfwNKpoN2RZ1gp21");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //ApiKeyQuery.setApiKeyPrefix("Token");

        AktivittenApi apiInstance = new AktivittenApi(defaultClient);
        Integer id = (Integer) 1; // Integer |
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
