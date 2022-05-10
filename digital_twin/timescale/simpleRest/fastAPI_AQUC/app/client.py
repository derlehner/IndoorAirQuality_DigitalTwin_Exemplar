""" #
import socket
import threading
import time

HOST = '140.78.42.121'  
PORT = 65432 

def process_data_from_Raspi(airQualityData):
    co2, temp, humidity = airQualityData.split(",")
    print(co2, temp, humidity)
    return co2, temp, humidity

def my_client():
    threading.Timer(11, my_client).start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((HOST, PORT))
        my = 'receiveDataFromRaspi'
        my_inp = my.encode('utf-8')
        s.sendall(my_inp)
        data = s.recv(1024).decode('utf-8')
        print('Connection is established with raspi')
        Co2, Temperature, Humidity = process_data_from_Raspi(data)
        print(Co2, Temperature, Humidity)
        s.close()
        time.sleep(5)

my_client() """