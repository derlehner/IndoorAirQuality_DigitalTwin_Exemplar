#!/usr/bin/python3
# This Script is desined to read the data from the sensor and send to azure clould system
# Please take note on which sensor is used {'CCS811', 'SCD_30'}
# To run the script use python 3 with all the pacakages installed

import time
from datetime import datetime
from azure.iot.device import IoTHubDeviceClient, Message
from SCD30Sensor import SCD30Sensor
from TimeScaleService import TimeScaleService
from scd30_i2c import SCD30
import urllib3
import sys
import requests
import json
urllib3.disable_warnings()

SLEEP_TIME = 2
DEVICE_ID = "raspi01"
with open('device_id.txt', 'r') as f:
    DEVICE_ID = f.readline()
sensors = [SCD30Sensor("port", "Sensor1", "co2"), SCD30Sensor("port", "Sensor1", "temperature"), SCD30Sensor("port", "Sensor1", "humidity")]
alarms = []
dt_service = TimeScaleService() # alternatively: AzureService()

while True:
    for sensor in sensors:
        try:
            timestamp, value = sensor.get_data()
        except Exception as err:
            print("Error getting data from sensor: " + err.message)
        try:
            dt_service.send_data(DEVICE_ID, sensor.sensor_name, sensor.property_name, timestamp, value)
        except Exception as err:
             print("Error sending data to server: " + err.message)

