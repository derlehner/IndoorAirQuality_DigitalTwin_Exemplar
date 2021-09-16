from datetime import datetime
import time
from scd30_i2c import SCD30
import json
import requests



def post_SensorData_Server(co2, temp, hum, sensor_name, room_number):
    jsonObjects={}
    url="http://140.78.155.6:5000/api/sensordata"
    headers = {
    'Content-Type':'application/json', 
    'Accept':'application/json'}

    
    jsonObjects['sensorname']= sensor_name     # SENSOR NAME
    jsonObjects['roomnumber']=room_number     # ROOM NUMBER
    jsonObjects['co2']=float(co2)           # CO2 VALUE
    jsonObjects['temperature']=float(temp)  # Temp VALUE
    jsonObjects['humidity']=float(hum)      # Hum VALUE
    jsonformat=json.dumps(jsonObjects)      # DUMPING DATA TO BE SENT
    postdata=requests.post(url,headers=headers,data=jsonformat)     # SENDING THE DATA
    response = postdata.text
    if postdata.status_code==201:
        print('Sensor data sending successfully....')
    else:
        print(postdata.text+'Failed to post Sensor data to server!')
    return response



scd30 = SCD30()

scd30.set_measurement_interval(2)
scd30.start_periodic_measurement()

time.sleep(2)

while True:
    if scd30.get_data_ready():
        m = scd30.read_measurement()
        if m is not None:
            print(f"CO2: {m[0]:.2f}ppm, temp: {m[1]:.2f}'C, rh: {m[2]:.2f}%")
        # time.sleep(0.5)
            post_SensorData_Server(co2=m[0], temp=m[1], hum=m[2],  sensor_name='scd30', room_number='s30076')
    else:
        pass
    
