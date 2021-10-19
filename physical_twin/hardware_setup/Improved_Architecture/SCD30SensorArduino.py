import pyfirmata
import time
import board
import adafruit_scd30
from datetime import datetime



class SCD30SensorArduino:
    def __init__(self, port, sensor_name, property_name):
        self.port = port
        self.sensor_name = sensor_name
        self.property_name = property_name

        # initialize i2c
        i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
        self.sensor = adafruit_scd30.SCD30(i2c)
        
        

    def get_data(self):
        if self.property_name == "temperature":
            temp = self.sensor.temperature
            timestamp = datetime.now()
            return (timestamp, temp)
            
        elif self.property_name == "co2":
            co2 = self.sensor.co2
            timestamp = datetime.now()
            return (timestamp, co2)


        if self.property_name == "humidity":
            humidity = self.sensor.relative_humidity
            timestamp = datetime.now()
            return (timestamp, humidity)

