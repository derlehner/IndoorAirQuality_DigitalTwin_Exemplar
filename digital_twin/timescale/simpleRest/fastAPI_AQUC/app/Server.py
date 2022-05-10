""" from datetime import datetime
import socket
import sys
import requests
import time
from scd30_i2c import SCD30
from signal import signal,SIGPIPE,SIG_DFL
import json 

signal(SIGPIPE,SIG_DFL)

HOST = '140.78.42.92'  # Standard loopback interface address (localhost)
PORT = 65433        # Port to listen on (non-privileged ports are > 1023)


def sensor_data():          # ANY DATA YOU WANT TO SEND WRITE YOUR SENSOR CODE HERE
    scd30 = SCD30()
    scd30.set_measurement_interval(2)
    scd30.start_periodic_measurement()
    time.sleep(2)
    try:
      while True:
        if scd30.get_data_ready():
         m = scd30.read_measurement()
         if m is not None:
          print("CO2: {m[0]:.2f}ppm, temp: {m[1]:.2f}'C, rh: {m[2]:.2f}%")
          CO2 = round(m[0],2)
          Temp = round(m[1],2)
          Humidity=round(m[2],2)
          my_sensor = "{},{},{}".format(CO2,Temp,Humidity)
          return my_sensor                            # return data seperated by comma
         else:
          print('cannot receive sensor measurements!')
    except KeyboardInterrupt:
          print('Interrupted with keyboard!')
          sys.exit(0)


def post_SensorData_Server():
    jsonObjects={}
    url="http://140.78.42.92:8080/docs/"
    headers = {
    'Content-Type':'application/json', 
    'Accept':'application/json'}
              
    raspi_sensordata = sensor_data()
    co2,temp,hum=raspi_sensordata.split(',')
    jsonObjects['room_id']='Room_S3_0090'
    jsonObjects['ventilator']='no'
    jsonObjects['totalnumberofpeople']=4
    jsonObjects['co2measurementunit']='ppm'
    jsonObjects['temperaturemeasurementunit']='degree celcius'
    jsonObjects['humiditymeasurementunit']='rh'
    jsonObjects['co2']=float(co2)
    jsonObjects['temperature']=float(temp)
    jsonObjects['humidity']=float(hum)
    jsonObjects['time']=str(datetime.now())
    jsonformat=json.dumps(jsonObjects)
    print(jsonformat)
    postdata=requests.post(url,headers=headers,data=jsonformat)
    response=postdata.text
    
    if postdata.status_code==201:
        print('Sensor data successfully sent to server!')
    else:
        print(postdata.text+'Failed to post Sensor data to server!')
    return response

def my_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
     s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
     print("Server Started waiting for client to connect ")
     s.bind((HOST, PORT))
     s.listen(5)
     conn, addr = s.accept()
    with conn:
     print('Connected by', addr)
     print("Sending data ")
     my_data = sensor_data()
     server_data=post_SensorData_Server()
     x_encoded_data = my_data.encode('utf-8')
     conn.sendall(x_encoded_data)
     print('Sensor data successfully sent to client!')
    if server_data==201:
     print('Sensor data successfully sent to server!')
     

if __name__ == '__main__':
        while 1:
            my_server()
 """