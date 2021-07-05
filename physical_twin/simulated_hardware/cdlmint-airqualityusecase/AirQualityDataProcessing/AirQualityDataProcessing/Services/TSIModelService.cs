using AirQualityDataProcessing.Model;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;

namespace AirQualityDataProcessing.Services
{
    public class TSIModelService
    {
        private const string URL = "https://5099d72a-08e4-416b-8cc6-173009801d45.env.timeseries.azure.com/timeseries/instances/$batch?api-version=2020-07-31";
        private const string ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiIxMjBkNjg4ZC0xNTE4LTRjZjctYmQzOC0xODJmMTU4ODUwYjYiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9iY2M3NmFhNy1iYmI1LTQxZjQtYmY1Ny0zMTIwNDJlMzE2ZTUvIiwiaWF0IjoxNjE3OTc2ODUzLCJuYmYiOjE2MTc5NzY4NTMsImV4cCI6MTYxNzk4MDc1MywiYWNyIjoiMSIsImFpbyI6IkFVUUF1LzhUQUFBQVRna3lXNDFab1d0ejgyaDF0OUVpdzA5WGM5OVJVbHlrYmpFVTBLbnJqVi9Rdkt2MlJpWjF4S1JVK2U3R3dtdWtQcGZUS3A1Z3ZHL0NEUHBNd1FHTmdRPT0iLCJhbHRzZWNpZCI6IjE6bGl2ZS5jb206MDAwM0JGRkRBREE3NzBCNSIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiIwNGIwNzc5NS04ZGRiLTQ2MWEtYmJlZS0wMmY5ZTFiZjdiNDYiLCJhcHBpZGFjciI6IjAiLCJlbWFpbCI6ImRhbmllbGdvdHRAbGl2ZS5hdCIsImZhbWlseV9uYW1lIjoiTGVobmVyIiwiZ2l2ZW5fbmFtZSI6IkRhbmllbCIsImdyb3VwcyI6WyJjYjQ3MmNmYi1iY2NkLTQ2YzctYjVjYy05YTcwM2Q4YTA4NWUiXSwiaWRwIjoibGl2ZS5jb20iLCJpcGFkZHIiOiI5MS4xMTUuMTA4LjUiLCJuYW1lIjoiRGFuaWVsIExlaG5lciIsIm9pZCI6IjJlMmI3NjJmLTVkMmQtNDBkOC1hYjg0LTk1ZWE1Njc1MWViNSIsInB1aWQiOiIxMDAzN0ZGRTkzNUUwNkIxIiwicmgiOiIwLkFSRUFwMnJIdkxXNzlFR19WekVnUXVNVzVaVjNzQVRialJwR3UtNEMtZUdfZTBZUkFQRS4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiJtOFh0TUJ0WHNCWk1QYUNwUFQ3MFRwN0cyek9tdlNjSXMxdHVoS0ozc3RBIiwidGlkIjoiYmNjNzZhYTctYmJiNS00MWY0LWJmNTctMzEyMDQyZTMxNmU1IiwidW5pcXVlX25hbWUiOiJsaXZlLmNvbSNkYW5pZWxnb3R0QGxpdmUuYXQiLCJ1dGkiOiJLM0dnYTh0QmRrS2R5Z3pBcXJUZEFBIiwidmVyIjoiMS4wIn0.Ir3044WzgJluVjMkDJpJrLYQXHg1gIqtEPNy7755rEy2zl2_AzNF29J_cnpf7Jnhpm9upmRrQ_YGdv_1YcbyyWDCo5yMqbqQq7gs3pIHZipWeiEN8KLwYNnaakeCElS2O_csOIBEuW-vPogBGNn6S_5maBA_4WjKiufpoOaQlYqYQ3hcsNnnonu5B-rb9nKCfz5LQryzcRZx_KLhBcKGlf_RTV6iC9ET90VddvpNCBTNDc2Hq6MrRbDrE9mk1rnMC0BtqHg9H7UZJNWu3ovl_YhCRmUTfroTgm0yDIt6A4e9jA01_iJ4IMfUNwnnQt1gqnMQiCnawvWWA4B3CgzBpQ";
        public static void addInstance(UpdateInstanceRequest request)
        {
            HttpClient client = new HttpClient();
            client.BaseAddress = new Uri(URL);

            // Add an Accept header for JSON format + add Bearer Access Token for TSI API.
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", ACCESS_TOKEN);
            client.DefaultRequestHeaders.Accept.Add(
            new MediaTypeWithQualityHeaderValue("application/json"));
            HttpResponseMessage response = client.PostAsJsonAsync(URL, request).Result;
            var ErrMsg = JsonConvert.DeserializeObject<dynamic>(response.Content.ReadAsStringAsync().Result);

            // Dispose once all HttpClient calls are complete. This is not necessary if the containing object will be disposed of; for example in this case the HttpClient instance will be disposed automatically when the application terminates so the following call is superfluous.

            client.Dispose();
        }

        public static void addType()
        {
            throw new NotImplementedException();
        }

        public static String getIdForTypeName()
        {
            throw new NotImplementedException();
        }
    }
}
