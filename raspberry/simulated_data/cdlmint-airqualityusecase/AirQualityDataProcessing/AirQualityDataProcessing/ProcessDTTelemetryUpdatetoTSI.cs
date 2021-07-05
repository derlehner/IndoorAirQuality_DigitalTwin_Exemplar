using Microsoft.Azure.EventHubs;
using Microsoft.Azure.WebJobs;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System.Threading.Tasks;
using System.Text;
using System.Collections.Generic;
using System;
using AirQualityDataProcessing.Services;
using System.Linq;

namespace UpdateTSI
{
    public static class ProcessDTTelemetryUpdatetoTSI
    {
      
        private const double TEMPERATURE_THRESHOLD_YELLOW = 1000;
        private const double TEMPERATURE_THRESHOLD_RED = 2000;
        private static NotificationService notifier = new AppNotificationService();

         [FunctionName("ProcessDTUpdatetoTSI")]
        public static async Task Run(
            [EventHubTrigger("eventhub", Connection = "EventHubAppSetting-Twins")] EventData myEventHubMessage,
            [EventHub("timeserieshub", Connection = "EventHubAppSetting-TSI")] IAsyncCollector<string> outputEvents,
            ILogger log)
        {
            // retrieve telemetry from requuest content
            string triggerBody = Encoding.UTF8.GetString(myEventHubMessage.Body);
            JObject message = (JObject)JsonConvert.DeserializeObject(triggerBody);
            log.LogInformation("Reading event:" + message.ToString());
            IList<string> keys = message.Properties().Select(p => p.Name).ToList();  // taken from https://stackoverflow.com/questions/6522358/how-can-i-get-a-list-of-keys-from-json-net/6529408
            string name = keys.First();
            Object value = message[name];
            //get the timestamp (mock up timestamp)
            string timestamp = keys.Last();
            Object tvalue = message[timestamp];

            // if telemetry is of type oxygen, send a notification if oxygen threshold is exceeded
            if (name.Equals("carbonDioxideValue"))
            {
                double temperature = Convert.ToDouble(value.ToString());
                if (isTemperatureThreshholdViolated(temperature))
                {
                    notifier.sendOxygenThreshholdNotification();
                }
            }
            // add telemetry value to TSI
            Dictionary<string, object> tsiUpdate = new Dictionary<string, object>();
            string dtId = myEventHubMessage.Properties["cloudEvents:source"].ToString();
            //int index = dtId.LastIndexOf("/");
            int index = dtId.LastIndexOf("/") + 1;
            dtId = dtId.Substring(index);
            if (myEventHubMessage.Properties["cloudEvents:subject"] != null)
            {
                dtId += "."+ myEventHubMessage.Properties["cloudEvents:subject"].ToString();
            }
            tsiUpdate.Add("dtdl", dtId);
            tsiUpdate.Add("timestamp", message["timestamp"].ToString());
            tsiUpdate.Add("carbonDioxideValue", value);
            string json = JsonConvert.SerializeObject(tsiUpdate);
            log.LogInformation("Writing event: " + json);
            await outputEvents.AddAsync(JsonConvert.SerializeObject(json));
        }

        private static bool isTemperatureThreshholdViolated(double value)
        {
            if (value <= TEMPERATURE_THRESHOLD_YELLOW)
            {
                return false;
            }
            return true;
        }
    }
}
 // primaryconnectionstring for updatetsi: "Endpoint=sb://airqualitydatabus.servicebus.windows.net/;SharedAccessKeyName=automation;SharedAccessKey=XofKaml2JUwI4qaX4MNVPSMh0ns+K5XW1YXUFHVDn30=;EntityPath=updatetsi"
        // primaryconnectionstring for pulltsifromdt: Endpoint=sb://airqualitydatabus.servicebus.windows.net/;SharedAccessKeyName=automation;SharedAccessKey=YyON7M3Tg4WD5Hv6tDmlraZ4tyAFvF/sNdvTq2Ri0U4=;EntityPath=pulltsifromdt
       /**
         * Sources for threshhold values:
         * https://smartbuildingsmagazine.com/features/carbon-dioxide-monitoring-to-lower-the-coronavirus-threat
         * https://www.infineon.com/dgdl/Infineon-EETimes_November2020_PASCO2sensor_Article-Article-v01_00-EN.pdf?fileId=5546d46275b79adb0175d1a459eb5b6c
         * https://depositonce.tu-berlin.de/handle/11303/11478.2
         * https://www.sciencedirect.com/science/article/pii/S0925753520302630#b0125
         */ 
        // dtId += "/" + myEventHubMessage.Properties["cloudEvents:subject"].ToString();