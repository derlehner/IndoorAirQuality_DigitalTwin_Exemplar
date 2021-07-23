#!/usr/bin/python3

import time
from datetime import datetime

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message
from sensor_DHT11 import sensor_DHT11
from sensor_CCS811 import sensor_CCS811
import digital_twin_api
import urllib3
urllib3.disable_warnings()

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
# TODO: could be parameterized
#CONNECTION_STRING_DHT11 = "HostName=AirQualityIoT.azure-devices.net;DeviceId=thermostat67;SharedAccessKey=stCRsRvwpv+jPuq5hc3X31Q412RXb4UV5djdq1aXBNk="
#CONNECTION_STRING_DHT11  = "HostName=AirQualityIoT.azure-devices.net;DeviceId=RaspiAir01-DHT11;SharedAccessKey=8UKEuIaJ6CkcE+RA+AYs9qHWlWRAEGw1dM0ZZ5YsqIk="
CONNECTION_STRING_CCS811 = "HostName=cdl2iot.azure-devices.net;DeviceId=Raspberry1;SharedAccessKey=Z0F/vMGuHY83UfXXcp7bAlkcPRs+SLl0IGSLwu3uZNU="

# messages format or IoT Hub
# TODO: could be parameterized
MSG_TXT_DHT11 = '{{"temperature": {temperature},"humidity": {humidity}}}'
MSG_TXT_CCS811 = '{{"temperature": {temperature},"co2Value": {eco2},"tvoc": {tvoc}}}'
MSG_TXT_RASPI = '{{"alarmC02": {alarmCO2}}}'

# TODO: could be parameterized
SLEEP_TIME = 2

# with open('file_name.txt', 'r') as f:
#     DEVICE_ID = f.readline()

DEVICE_ID = 'Raspberry1'

def iothub_client_init(sensor_name):
    # Create an IoT Hub client
    if sensor_name == "CCS811":
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING_CCS811)
        return client

def iothub_client_telemetry_run():
    try:
        # initialize clients
        #clientDHT11 = iothub_client_init("DHT11")
        clientCCS811 = iothub_client_init("CCS811")

        # initialize sensors
        # sensorDHT11 = sensor_DHT11()
        sensorCCS811 = sensor_CCS811()

        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        while True:
            # Build the message with telemetry values.
            # DHT11 telemetry
            # try:
            #     sensorDHT11.update_telemetry()
            # except RuntimeError:
            #     print('Runtime Error is initiated')
            # msg_txtDHT11_formatted = MSG_TXT_DHT11.format(temperature=sensorDHT11.temperature, humidity=sensorDHT11.humidity)
            # messageDHT11 = Message(msg_txtDHT11_formatted)
            # messageDHT11 = Message(msg_txtDHT11_formatted, content_encoding='utf-8', content_type='application/json')

            # CSS811 telemetry
            try: 
                sensorCCS811.update_telemetry()
            except RuntimeError:
                print('Runtime Error is initiated')
            
            
            # msg_txtCCS811_formatted = MSG_TXT_CCS811.format(temperature=sensorCCS811.temperature, eco2=sensorCCS811.eco2, tvoc=sensorCCS811.tvoc)
            # messageCCS811 = Message(msg_txtCCS811_formatted, content_encoding='utf-8', content_type='application/json')
            # messageCCS811 = Message(msg_txtCCS811_formatted)

            # Send the messages.
            # print( "{} - Sending DHT11 message: {}".format(datetime.now(), messageDHT11) )
            # #clientDHT11.send_message(messageDHT11)
            # print ( "Message successfully sent" )
            # time.sleep(1)
            # print( "{} - Sending CCS811 message: {}".format(datetime.now(), messageCCS811) )
            # clientCCS811.send_message(messageCCS811)
            # print ( "Message successfully sent" )

            # Sending Telemetry data to cloud
            digital_twin_api.send_telemetry_for_component(DEVICE_ID, 'CO2Sensor', "'carbonDioxideValue': {}".format(sensorCCS811.eco2))
            time.sleep(SLEEP_TIME)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    iothub_client_telemetry_run()
    print ( "IoT Hub connection for sensors" )
    print ( "Press Ctrl-C to exit" )


