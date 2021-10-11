#!/usr/bin/python3
'''
This Script is desined to read the data from the sensor and send to azure clould system
Please take note on which sensor is used {'CCS811', 'SCD_30', 'DHT11'}
To run the script use python 3 with all the pacakages installed
'''
import time
from datetime import datetime
from azure.iot.device import IoTHubDeviceClient, Message
from sensor_DHT11 import sensor_DHT11
from sensor_CCS811 import sensor_CCS811
from scd30_i2c import SCD30
import digital_twin_api
import urllib3
import sys
import requests
import json
urllib3.disable_warnings()


#The device connection string to authenticate the device with your IoT hub.
CONNECTION_STRING_CCS811 = "<specify the connection string>"
CONNECTION_STRING_SCD_30 = "<specify the connection string>"


### messages format or IoT Hub  ###
# TODO: could be parameterized
MSG_TXT_CCS811 = '{{"temperature": {temperature},"co2Value": {eco2},"tvoc": {tvoc}}}'
MSG_TXT_RASPI = '{{"alarmC02": {alarmCO2}}}'

# could be parameterized
SLEEP_TIME = 2

'''
This parameterised function used to post the data to the server
'''
def post_SensorData_Server(co2, temp, hum, sensor_name, room_number):
    jsonObjects={}
    url="http://140.78.155.6:5000/api/sensordata"
    headers = {
    'Content-Type':'application/json', 
    'Accept':'application/json'}

    co2,temp,hum=raspi_sensordata.split(',')
    jsonObjects['sensorname']='scd30'       # SENSOR NAME
    jsonObjects['roomnumber']='s30076'      # ROOM NUMBER
    jsonObjects['co2']=float(co2)           # CO2 VALUE
    jsonObjects['temperature']=float(temp)  # Temp VALUE
    jsonObjects['humidity']=float(hum)      # Hum VALUE
    jsonformat=json.dumps(jsonObjects)      # DUMPING DATA TO BE SENT
    postdata=requests.post(url,headers=headers,data=jsonformat)     # SENDING THE DATA
    if postdata.status_code==201:
        print('Sensor data sending successfully....')
    else:
        print(postdata.text+'Failed to post Sensor data to server!')
    return response

'''
This funciton used to connect to azure service using connection string
'''
def iothub_client_init(sensor_name):
    # Create an IoT Hub client
    if sensor_name == "CCS811":
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING_CCS811)
        return client
    elif sensor_name == "scd_30":
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING_SCD_30)
        return client
'''
This funciton uses used to read the data and sensor in use
'''
def iothub_client_telemetry_run(sensor_in_use):
    if sensor_in_use == "CCS811":
        try:
            clientCCS811 = iothub_client_init("CCS811")     # initialize clients
            sensorCCS811 = sensor_CCS811()                  # initialize sensors
            print ("IoT Hub device sending periodic messages, press Ctrl-C to exit")
            while True:
                try:
                    sensorCCS811.update_telemetry()
                except RuntimeError:
                    print('Runtime Error is initiated')
                # Sending Telemetry data to cloud
                digital_twin_api.send_telemetry_for_component(DEVICE_ID, 'CO2Sensor', "'carbonDioxideValue': {}".format(sensorCCS811.eco2))
                time.sleep(SLEEP_TIME)

        except KeyboardInterrupt:
            print ( "IoTHubClient sample stopped" )

    elif sensor_in_use == "scd_30":
        try:
            clientscd_30 = iothub_client_init("scd_30")     # initialize clients
            sensorsdc_30 = SCD30()      # initialize sensors
            sensorsdc_30.set_measurement_interval(2)
            sensorsdc_30.start_periodic_measurement()
            time.sleep(2)
            print("IoT Hub device sending periodic messages, press Ctrl-C to exit")
            while True:
                if sensorsdc_30.get_data_ready():
                    scd_co2, scd_temp, scd_rh = sensorsdc_30.read_measurement()
                    if scd_co2 is not None:
                        print(f"CO2: {scd_co2:.2f}ppm, temp: {scd_temp:.2f}'C, rh: {scd_rh:.2f}%")
                        # Sending Telemetry data to cloud
                        scd_co2=scd_co2:.2f
                        scd_temp=scd_temp:.2f
                        scd_rh=scd_rh:.2f
                        post_SensorData_Server(co2=scd_co2, temp= scd_temp, hum= scd_rh, sensor_name='scd30', room_number='s30076')
                        time.sleep(SLEEP_TIME)
                else:
                    pass
        except KeyboardInterrupt:
            print("IoTHubClient sample stopped")

if __name__ == '__main__':
    sensor_in_use = "scd_30"   # Specify either {'scd_30', 'CCS811'}
    iothub_client_telemetry_run(sensor_in_use)
    print ( "IoT Hub connection for sensors" )
    print ( "Press Ctrl-C to exit" )


