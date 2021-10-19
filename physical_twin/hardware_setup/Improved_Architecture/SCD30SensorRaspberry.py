import time
from scd30_i2c import SCD30
from datetime import datetime

class SCD30Sensor:
    def __init__(self, port, sensor_name, property_name):
        self.port = port
        self.sensor_name = sensor_name
        self.property_name = property_name
        self.sensor = SCD30()
        self.sensor.set_measurement_interval(2)
        self.sensor.start_periodic_measurement()
        
    def get_data(self):
        if scd30.get_data_ready():
            if self.property_name == "temperature":
                    m = scd30.read_measurement()
                    if m is not None:
                        print(f"CO2: {m[0]:.2f}ppm, temp: {m[1]:.2f}'C, rh: {m[2]:.2f}%")
                        # time.sleep(0.5)
                        value = m[1]
                        timestamp = datetime.now()
                        return (timestamp, value)
            elif self.property_name == "co2":
                m = scd30.read_measurement()
                if m is not None:
                    print(f"CO2: {m[0]:.2f}ppm, temp: {m[1]:.2f}'C, rh: {m[2]:.2f}%")
                    # time.sleep(0.5)
                    value = m[0]
                    timestamp = datetime.now()
                    return (timestamp, value)
            elif self.property_name == "humidity":
                m = scd30.read_measurement()
                if m is not None:
                    print(f"CO2: {m[0]:.2f}ppm, temp: {m[1]:.2f}'C, rh: {m[2]:.2f}%")
                    # time.sleep(0.5)
                    value = m[2]
                    timestamp = datetime.now()
                    return (timestamp, value)
