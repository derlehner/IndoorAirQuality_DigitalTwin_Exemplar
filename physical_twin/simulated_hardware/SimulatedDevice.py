import random
import time
import csv
from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity connection-string show --hub-name {YourIoTHubName} --device-id {YourDeviceId} --output table

CONNECTION_STRING = "HostName=IoTHub-CDL.azure-devices.net;DeviceId=Raspberry1;SharedAccessKey=VCS2Vi8SIooykpFsSO0tNnOGh2hr+Io5ihb1/n44t1I="

# Define the JSON message to send to IoT Hub.
MSG_TXT = '{{"Temperature": {Temperature},"Humidity": {Humidity},"CarbonDioxideValue":{CarbonDioxideValue}}}'

# Define the csv file name to parse
csvFilePath='sensorData.csv'

 
def parse_csv(csvFilePath):
#read csv file
 with open(csvFilePath, encoding='utf-8') as csvFile:
    #load csv file data using csv library's dictionary reader
    csvReader=csv.DictReader(csvFile)
    data=[];
    for rows in csvReader:
     data.append(rows)
    return data

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        sensorData=parse_csv(csvFilePath)
        while True:
            # Build the message with actual sensor data from room.
            for d in sensorData:

             Temperature = d['temperature']
             Humidity = d['humidity']
             CarbonDioxideValue=d['co2']


             msg_txt_formatted = MSG_TXT.format(Temperature=Temperature, Humidity=Humidity,CarbonDioxideValue=CarbonDioxideValue)
             message = Message(msg_txt_formatted)

            

             # Send the message.
             print( "Sending message: {}".format(message) )
             client.send_message(message)
             print ("Message successfully sent")
             time.sleep(1)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #1 - Simulated Sensor Data" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()
