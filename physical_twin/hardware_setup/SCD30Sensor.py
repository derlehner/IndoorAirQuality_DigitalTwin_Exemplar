import time
import board
import adafruit_dht

class SCD30Sensor:
    def __init__(self, port, sensor_name, property_name, azure_connection_string):
        self.port = port
        self.sensor_name = sensor_name
        self.property_name = property_name
        self.azure_connection_string = azure_connection_string
        
        

    def get_data(self):
        if self.property_name == "temperature":
            # TODO: fill this with data to get temperature value
            pass
        elif self.property_name == "co2":
            # TODO: fill this with data to get co2 value
            pass
        if self.property_name == "humidity":
            # TODO: fill this with data to get humidity value
            pass
