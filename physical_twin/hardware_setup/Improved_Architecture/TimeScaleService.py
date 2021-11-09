import json
import requests
from datetime import datetime, timezone


class TimeScaleService:

    def send_data(device_id, sensor_id, property_name, value):
        jsonObjects = {}
        url = "https://airquality.se.jku.at/api/sensordata"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}

        # TODO: sent data should be in format [device_id, sensor_id, property_name, timestamp, value]

        jsonObjects['container'] = device_id       # SENSOR NAME
        # TODO: change roomnumber to deviceId (also in Timescale DB on Webserver)
        jsonObjects['instance'] = sensor_id      # ROOM NUMBER
        # TODO: make sure that the server accepts requests where only one of temperature, humidity and co2 is sent, NOT all three at once
        jsonObjects['property'] = property_name           # CO2 VALUE
        # TODO: add timestamp to request
        jsonObjects['time'] = datetime.now(timezone.utc)
        jsonObjects['value'] = value
        jsonformat = json.dumps(jsonObjects)      # DUMPING DATA TO BE SENT
        response = requests.post(url, headers=headers,
                                 data=jsonformat)     # SENDING THE DATA
        if response.status_code == 201:
            print('Sensor data sending successfully....')
        else:
            print(response.text+'Failed to post Sensor data to server!')
        return response
