#!/usr/bin/python3
# This Script is desined to read the data from the sensor and send to azure clould system
# Please take note on which sensor is used {'CCS811', 'SCD_30'}
# To run the script use python 3 with all the pacakages installed

import time
from datetime import datetime
#from azure.iot.device import IoTHubDeviceClient, Message
from SCD30SensorRaspberry import SCD30Sensor
from TimeScaleService import TimeScaleService
from scd30_i2c import SCD30
import urllib3
import sys
import requests
import json
urllib3.disable_warnings()

SLEEP_TIME = 2
DEVICE_ID = "Raspi_01"
# with open('device_id.txt', 'r') as f:
#    DEVICE_ID = f.readline()
port = DEVICE_ID
sensorName = "SCD-30"
sensorProperties = ["co2", "temperature", "humidity"]
sensors = SCD30Sensor(port, sensorName)
alarms = []
dt_service = TimeScaleService()  # alternatively: AzureService()

while True:
    for prop in sensorProperties:
        try:
            result = sensors.get_data(prop)
            print(result[0], result[1], result[2])
        except Exception as err:
            print("Error getting data from sensor: " + err)
        try:
            print(port, sensorName,
                  result[0], result[2])
            dt_service.send_data(port, sensorName,
                                 result[0], result[2])
        except Exception as err:
            print("Error getting data from sensor: " + err)
