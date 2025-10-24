// region: imports
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.ApiKeyAuth;
import org.openapitools.client.api.PlenarprotokolleApi;
import org.openapitools.client.model.PlenarprotokollText;
import org.openapitools.client.model.PlenarprotokollTextListResponse;

import java.io.FileWriter;
import java.io.IOException;
import java.io.File;
import java.util.Collections;

import com.google.gson.*;
import java.time.LocalDate;
import java.lang.reflect.Type;
// endregion: imports


public class LoadProtocols {

    public static void main(String[] args) {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://search.dip.bundestag.de/api/v1");

        ApiKeyAuth apiKey = (ApiKeyAuth) client.getAuthentication("ApiKeyQuery");
        apiKey.setApiKey("I9FKdCn.hbfefNWCY336dL6x62vfwNKpoN2RZ1gp21");

        PlenarprotokolleApi api = new PlenarprotokolleApi(client);
        Gson gson = new GsonBuilder()
                .setPrettyPrinting()
                .registerTypeAdapter(LocalDate.class, (JsonSerializer<LocalDate>) (src, typeOfSrc, context) -> new JsonPrimitive(src.toString()))
                .registerTypeAdapter(java.time.OffsetDateTime.class, (JsonSerializer<java.time.OffsetDateTime>) (src, typeOfSrc, context) -> new JsonPrimitive(src.toString()))
                .create();

        for (int wahlperiode : new int[]{19, 20}) {
            String outputDir = "rawdata" + wahlperiode + "json";
            new File(outputDir).mkdirs(); // Create directory if it doesn't exist

            String cursor = null;
            boolean hasMore = true;

            while (hasMore) {
                try {
                    PlenarprotokollTextListResponse response = api.getPlenarprotokollTextList(
                            null, null, // aktualisiertStart/End
                            null, null, // datumStart/End
                            null, null, // dokumentnummer, id
                            null, null, // vorgangstyp, vorgangstypNotation
                            Collections.singletonList(wahlperiode), // aktuelle Wahlperiode
                            null, // zuordnung
                            cursor, // cursor (Pagination)
                            "json" // Format
                    );

                    if (response.getDocuments() == null || response.getDocuments().isEmpty()) {
                        hasMore = false;
                        break;
                    }

                    for (PlenarprotokollText protokoll : response.getDocuments()) {
                        String filename = outputDir + "/protokoll_" + protokoll.getId() + ".json";
                        try (FileWriter writer = new FileWriter(filename)) {
                            gson.toJson(protokoll, writer);
                            System.out.println("[" + wahlperiode + "] Gespeichert: " + filename);
                        } catch (IOException e) {
                            System.err.println("[" + wahlperiode + "] Fehler beim Speichern: " + filename);
                            e.printStackTrace();
                        }
                    }

                    cursor = response.getCursor();
                    if (cursor == null || cursor.isEmpty()) {
                        hasMore = false;
                    }

                } catch (ApiException e) {
                    System.err.println("[" + wahlperiode + "] API-Fehler: " + e.getMessage());
                    e.printStackTrace();
                    break;
                }
            }
        }

        System.out.println("Alle Protokolle für WP 19 und 20 geladen.");
    }
}
