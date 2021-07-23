using AirQualityDataProcessing.Model;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;

namespace AirQualityDataProcessing.Services
{
    public class ADTService
    {
        private const string URL = "https://aiquality-usecase.api.wcus.digitaltwins.azure.net/models/";
        private const string ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiIwYjA3ZjQyOS05ZjRiLTQ3MTQtOTM5Mi1jYzVlOGU4MGM4YjAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9iY2M3NmFhNy1iYmI1LTQxZjQtYmY1Ny0zMTIwNDJlMzE2ZTUvIiwiaWF0IjoxNjE3OTc2Nzk4LCJuYmYiOjE2MTc5NzY3OTgsImV4cCI6MTYxNzk4MDY5OCwiYWNyIjoiMSIsImFpbyI6IkFVUUF1LzhUQUFBQVkwMForWFluTk9BVnVHMGJTS1N6YThwL1BBY0JUQlo4b3hURStxUFc2TERVekR2d1EyVG16a0kyb3drN1hwQ3Y3K2pJQWVDZjRhbEViZENHMFdsdTFRPT0iLCJhbHRzZWNpZCI6IjE6bGl2ZS5jb206MDAwM0JGRkRBREE3NzBCNSIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiIwNGIwNzc5NS04ZGRiLTQ2MWEtYmJlZS0wMmY5ZTFiZjdiNDYiLCJhcHBpZGFjciI6IjAiLCJlbWFpbCI6ImRhbmllbGdvdHRAbGl2ZS5hdCIsImZhbWlseV9uYW1lIjoiTGVobmVyIiwiZ2l2ZW5fbmFtZSI6IkRhbmllbCIsImlkcCI6ImxpdmUuY29tIiwiaXBhZGRyIjoiOTEuMTE1LjEwOC41IiwibmFtZSI6IkRhbmllbCBMZWhuZXIiLCJvaWQiOiIyZTJiNzYyZi01ZDJkLTQwZDgtYWI4NC05NWVhNTY3NTFlYjUiLCJwdWlkIjoiMTAwMzdGRkU5MzVFMDZCMSIsInJoIjoiMC5BUkVBcDJySHZMVzc5RUdfVnpFZ1F1TVc1WlYzc0FUYmpScEd1LTRDLWVHX2UwWVJBUEUuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiUnBnZVVFZTBTc2I3aVFDTEFIZHAxU0laVV9TZGtWQThiaDNnNDFWZHNVdyIsInRpZCI6ImJjYzc2YWE3LWJiYjUtNDFmNC1iZjU3LTMxMjA0MmUzMTZlNSIsInVuaXF1ZV9uYW1lIjoibGl2ZS5jb20jZGFuaWVsZ290dEBsaXZlLmF0IiwidXRpIjoiWmw0ME5McXk4MHFLbkxJbEhQSmVBQSIsInZlciI6IjEuMCJ9.kTgCrZqV70EbQX6GbY1wHwSHnoaGyEIRmfvnDrdjWKG11lAV7o28IDQ1IG-t1jc-4Aclr-LY4niIvVYgXJZy0uqz7YdXfMVM_0XdcSXjdw_VJYvBDvEdPol-0VyVQpEMlz-5OG7oPFvC1nxmSLy9rmNfTrqC6wfK-fOjR-TL5c8_03yAC7Ql6mq2d3VEDU5zinkij83CFTa20hGTAfXT6NOE5Q2rjqJf3GGx_0fX2xBYcROBSkM2lsRWBRa0fDKdsuCm87dPe6OMDbNezkswfgm_iL7LLt9eO4oHOgIUqBwQ-gmOxgCLqaUPw5WlZtcjZFaxsVPhsEK6KxD3ixxv6Q";
        public static Dictionary<String, String> getComponents(String typeId)
        {
            Dictionary<String, String> result = new Dictionary<String, String>();
            HttpClient client = new HttpClient();
            client.BaseAddress = new Uri(URL);

            // Add an Accept header for JSON format + add Bearer Access Token for TSI API.
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", ACCESS_TOKEN);
            client.DefaultRequestHeaders.Accept.Add(
            new MediaTypeWithQualityHeaderValue("application/json"));
            HttpResponseMessage response = client.GetAsync(URL + typeId + "?includeModelDefinition=True&api-version=2020-10-31").Result;

            if (response.IsSuccessStatusCode)
            {
                Model.Type model = response.Content.ReadAsAsync<Model.Type>().Result;
                foreach(Model.Type.TwinModel.ModelContent content in model.model.contents)
                {
                    if (content.contentType.Contains("Component"))
                    {
                        result[content.name] = content.schema;
                    }
                }
            }


            // Dispose once all HttpClient calls are complete. This is not necessary if the containing object will be disposed of; for example in this case the HttpClient instance will be disposed automatically when the application terminates so the following call is superfluous.
            client.Dispose();
            return result;
        }

        public static bool getTelemetries (String typeId)
        {
            HttpClient client = new HttpClient();
            client.BaseAddress = new Uri(URL);

            // Add an Accept header for JSON format + add Bearer Access Token for TSI API.
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", ACCESS_TOKEN);
            client.DefaultRequestHeaders.Accept.Add(
            new MediaTypeWithQualityHeaderValue("application/json"));
            HttpResponseMessage response = client.GetAsync(URL + typeId + "?includeModelDefinition=True&api-version=2020-10-31").Result;
            client.Dispose();
            if (response.IsSuccessStatusCode)
            {
                Model.Type model = response.Content.ReadAsAsync<Model.Type>().Result;
                foreach (Model.Type.TwinModel.ModelContent content in model.model.contents)
                {
                    if (content.contentType.Contains("Telemetry"))
                    {
                        return true;
                    }
                }
            } 
            return false;
        }

        public static String hasTelemetryComponent()
        {
            throw new NotImplementedException();
        }
    }
}
