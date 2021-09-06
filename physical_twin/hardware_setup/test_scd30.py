import time
from datetime import datetime
import time
from scd30_i2c import SCD30
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING_scd_30 = "HostName=AirQualityIoT.azure-devices.net;DeviceId=RaspiAir01-CCS811;SharedAccessKey=ae88fHX6LSBvugewqOSZ4hLs4n1AomvcoRg4PGTgf1c="
def iothub_client_init(sensor_name):
    # Create an IoT Hub client
    if sensor_name == "scd_30":
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING_scd_30)
    else:
        print('Error on creating iothub_client_init')
        return None
    return client

def iothub_client_telemetry_run():
    try:
        client_scd30 = iothub_client_init('scd_30')

        while True:
            scd30 = SCD30()

            scd30.set_measurement_interval(2)
            scd30.start_periodic_measurement()

            time.sleep(2)

            while True:
                if scd30.get_data_ready():
                    m = scd30.read_measurement()
                    if m is not None:
                        message = f"CO2: {m[0]:.2f}ppm, temp: {m[1]:.2f}'C, rh: {m[2]:.2f}%"
                        print(f"CO2: {m[0]:.2f}ppm, temp: {m[1]:.2f}'C, rh: {m[2]:.2f}%")
                        client_scd30.send_message(message)
                    # time.sleep(0.5)
                else:
                    pass
    except KeyboardInterrupt:
        print('iot stopped')
        
if __name__ = '__main__':
    iothub_clilent_telemetry_run()
    
