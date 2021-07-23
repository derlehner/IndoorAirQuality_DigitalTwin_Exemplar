import time
import board
import adafruit_dht

class sensor_DHT11:
    def __init__(self):
        # pin assignment
        # initialize sensor values
        self.temperature = 0.0
        self.humidity = 0.0
        self.dhtDevice = adafruit_dht.DHT11(board.D22, use_pulseio = False)
        
        

    def update_telemetry(self):
        humi = None
        temp = None

        while humi is None and temp is None:
            temp = self.dhtDevice.temperature
            # temperature = temperature_c * (9 / 5) + 32
            humi = self.dhtDevice.humidity
            print('while loop is running')
            time.sleep(2.0)
        self.humidity = humi
        self.temperature = temp
