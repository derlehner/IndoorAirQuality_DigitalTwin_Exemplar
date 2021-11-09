import time
from scd30_i2c import SCD30
from datetime import datetime, timezone


class SCD30Sensor:
    def __init__(self, port, sensor_name):
        self.port = port
        self.sensor_name = sensor_name
        self.sensor = SCD30()
        self.sensor.set_measurement_interval(2)
        self.sensor.start_periodic_measurement()

    def get_data(self, property_name):
        if self.sensor.get_data_ready():
            m = self.sensor.read_measurement()
            if m is not None:
                if property_name == "co2":
                    value = round(m[0], 4)
                    timestamp = datetime.now(timezone.utc)
                    time.sleep(3)
                    return [property_name, timestamp, value]
                elif property_name == "temperature":
                    value = round(m[1], 4)
                    timestamp = datetime.now(timezone.utc)
                    time.sleep(3)
                    return [property_name, timestamp, value]
                elif property_name == "humidity":
                    value = round(m[2], 4)
                    timestamp = datetime.now(timezone.utc)
                    time.sleep(3)
                    return [property_name, timestamp, value]
            else:
                print('no measurement values')
        else:
            print('sensor is not yet ready')
