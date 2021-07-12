import random
import time
from azure.iot.device import IoTHubDeviceClient, Message
# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity connection-string show --hub-name {YourIoTHubName} --device-id {YourDeviceId} --output table

CONNECTION_STRING = "HostName=IoTHub-CDL.azure-devices.net;DeviceId=Raspberry1;SharedAccessKey=VCS2Vi8SIooykpFsSO0tNnOGh2hr+Io5ihb1/n44t1I="
# Define the JSON message to send to IoT Hub.
TEMPERATURE = 20.0
HUMIDITY = 60
CARBONDIOXIDE=1000


MSG_TXT = '{{"Temperature": {Temperature},"Humidity": {Humidity},"CarbonDioxideValue":{CarbonDioxideValue}}}'

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        while True:
            # Build the message with simulated telemetry values.
            Temperature = TEMPERATURE + (random.random() * 15)
            Humidity = HUMIDITY + (random.random() * 20)
            CarbonDioxideValue=CARBONDIOXIDE+(random.random()*2)


            msg_txt_formatted = MSG_TXT.format(Temperature=Temperature, Humidity=Humidity,CarbonDioxideValue=CarbonDioxideValue)
            message = Message(msg_txt_formatted)

            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            if Temperature > 30:
              message.custom_properties["temperatureAlert"] = "true"
            else:
              message.custom_properties["temperatureAlert"] = "false"

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ("Message successfully sent")
            time.sleep(1)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #1 - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()
