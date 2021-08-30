using System;
using Azure;
using System.Net.Http;
using Azure.Core.Pipeline;
using Azure.DigitalTwins.Core;
using Azure.Identity;
using Microsoft.Azure.EventGrid.Models;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.EventGrid;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System.Threading.Tasks;
using System.Text;

namespace IotHubtoTwins
{
    public class IoTHubtoTwins
    {
        private static readonly string adtInstanceUrl = Environment.GetEnvironmentVariable("ADT_SERVICE_URL");
        private static readonly HttpClient httpClient = new HttpClient();

        [FunctionName("IoTHubtoTwins")]
        public static async Task Run([EventGridTrigger] EventGridEvent eventGridEvent, ILogger log)
        {
            log.LogInformation(eventGridEvent.Data.ToString());
            if (adtInstanceUrl == null) log.LogError("Application setting \"ADT_SERVICE_URL\" not set");

            try
            {
                // Authenticate with Digital Twins
                var cred = new ManagedIdentityCredential("https://digitaltwins.azure.net");
                var client = new DigitalTwinsClient(
                    new Uri(adtInstanceUrl),
                    cred,
                    new DigitalTwinsClientOptions { Transport = new HttpClientTransport(httpClient) });
                log.LogInformation($"ADT service client connection created.");

                if (eventGridEvent != null && eventGridEvent.Data != null)
                {
                    log.LogInformation(eventGridEvent.Data.ToString());

                    // <Find_device_ID_and_temperature>
                    JObject deviceMessage = (JObject)JsonConvert.DeserializeObject(eventGridEvent.Data.ToString());
                    string deviceId = (string)deviceMessage["systemProperties"]["iothub-connection-device-id"];

                    // body seems to be a base64 encoded string
                    string base64EncodedBody =  (string)deviceMessage["body"];
                    var decodedBody = Encoding.UTF8.GetString(Convert.FromBase64String(base64EncodedBody));
                    JObject messageBody = (JObject)JsonConvert.DeserializeObject(decodedBody);

                    var temperature = messageBody["Temperature"];
                    var humidity = messageBody["Humidity"];
                    var co2Value = messageBody["CarbonDioxideValue"];
                    // </Find_device_ID_and_temperature>

                    log.LogInformation($"Device:{deviceId} Temperature is:{temperature}");
                    log.LogInformation($"Device:{deviceId} Humidity is:{humidity}");
                    log.LogInformation($"Device:{deviceId} co2Value is:{co2Value}");
                    // <Update_twin_with_device_temperature>
                    var updateTwinData = new JsonPatchDocument();
                    updateTwinData.AppendReplace("/Temperature", temperature.Value<double>());
                    updateTwinData.AppendReplace("/Humidity", humidity.Value<double>());
                    updateTwinData.AppendReplace("/CarbonDioxideValue", co2Value.Value<double>());
                    await client.UpdateDigitalTwinAsync(deviceId, updateTwinData);
                    // </Update_twin_with_device_temperature>
                }
            }
            catch (Exception ex)
            {
                log.LogError($"Error in ingest function: {ex.Message}");
            }
        }
    }
}