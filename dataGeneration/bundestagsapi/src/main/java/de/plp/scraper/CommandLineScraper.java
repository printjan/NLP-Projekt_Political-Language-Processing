package de.plp.scraper;

import java.util.ArrayList;
import java.util.List;

import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.api.PlenarprotokolleApi;
import org.openapitools.client.auth.ApiKeyAuth;
import org.openapitools.client.model.Plenarprotokoll;
import org.openapitools.client.model.PlenarprotokollListResponse;

public class CommandLineScraper {
	public static void main(String[] args) {
		if (args.length == 0) {
			System.out.println("Verwendung: bundestagsapi.jar <Wahlperiode>");
			System.exit(0);
		}
		int wahlperiode;
		try {
			wahlperiode = Integer.parseInt(args[0]);
		} catch (NumberFormatException e) {
			System.out.println("Die Wahlperiode muss als Zahl angegeben werden.");
			return;
		}
		ApiClient defaultClient = Configuration.getDefaultApiClient();
		defaultClient.setBasePath("https://search.dip.bundestag.de/api/v1");

		// Configure API key authorization: ApiKeyHeader
		ApiKeyAuth ApiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyHeader");
		ApiKeyHeader.setApiKey("I9FKdCn.hbfefNWCY336dL6x62vfwNKpoN2RZ1gp21");
		// Uncomment the following line to set a prefix for the API key, e.g. "Token"
		// (defaults to null)
		// ApiKeyHeader.setApiKeyPrefix("Token");
		// Configure API key authorization: ApiKeyQuery
		ApiKeyAuth ApiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyQuery");
		ApiKeyQuery.setApiKey("I9FKdCn.hbfefNWCY336dL6x62vfwNKpoN2RZ1gp21");
		// Uncomment the following line to set a prefix for the API key, e.g. "Token"
		// (defaults to null)
		// ApiKeyQuery.setApiKeyPrefix("Token");

		PlenarprotokolleApi apiInstance = new PlenarprotokolleApi(defaultClient);
		String format = "json"; // String | Steuert das Datenformat der Antwort, möglich sind JSON
														// (voreingestellt) oder XML.
		try {
			List<Integer> wahlperiodeList = new ArrayList<>();
			wahlperiodeList.add(wahlperiode);
			PlenarprotokollListResponse response = apiInstance.getPlenarprotokollList(null, null, null, null, null, null,
					null, null, wahlperiodeList, null, null, format);
					for (Plenarprotokoll protokoll : response.getDocuments()) {
						
						System.out.println(protokoll.getDokumentnummer());
					}
		} catch (ApiException e) {
			System.err.println("Exception when calling PlenarprotokolleApi#getPlenarprotokoll");
			System.err.println("Status code: " + e.getCode());
			System.err.println("Reason: " + e.getResponseBody());
			System.err.println("Response headers: " + e.getResponseHeaders());
			e.printStackTrace();
		}
	}
}
