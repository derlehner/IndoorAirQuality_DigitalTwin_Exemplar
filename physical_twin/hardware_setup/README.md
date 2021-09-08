# Setup Physical Twin with actual hardware

## Contents
- [Prerequisites](#Prerequisites)
- [Hardware setup](#Hardware_setup)
	- [Raspberry Pi](#Raspberry)
	- [Sensor CCS811](#ccs811)
	- [Sensor SCD30](#scd30)
- [Initial Setup of Raspberry OS](#Initial_Setup_of_Raspberry_OS)
- [Send Sensor data to cloud](#Send_Sensor_data_to_cloud)
	- [Required Libraries for the project](#libraries)
	- [Remote access via SSH](#ssh)
	- [Deploy Code to Raspberry](#Deploy)
	- [Deploy Code to multiple Raspberries](#DeployMultiDevice)
	- [Sending data to IoT-hub](#Sending)
- [Possilble Frequent Errors](#Possilble_Frequent_Errors)

## <a name="Prerequisites"></a>Prerequisites
- Raspberry and accessories
- CCS811 and DHT11 Sensors
- Electronics like resistors, LED lights 
- Bread board and connection wires

## <a name="Hardware_setup"></a>Hardware setup
### <a name="Raspberry"></a>Raspberry Pi
 We ue [Raspberry Pi 4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) boards. Raspberry is a dedicated computer with all neccesary functions just like an ordinary pc.  The raspberry sends measured co2 values to the cloud and is also used to command the treshold triggers if the values reach above the limit by changing the color of the LED or by Beeping sounds. 
 <img src='https://cdn.idealo.com/folder/Product/6628/1/6628198/s2_produktbild_max/raspberry-pi-4-model-b.jpg'  width=400 />
 
 An alternative would be NVIDIA's [Jetson Nano](https://developer.nvidia.com/embedded/jetson-nano-developer-kit). However in this project a Raspberry is used and for this following hardware for setting up the raspberry is needed:
- (Fully Integrated) Raspberry Pi 4 - Board
- Power adapter for Raspberry Pi 4 (USB-C)
- SD-card
- LAN-cable
- Card-Reader (for initialization)
- Keyboard (for initialization)
- Micro-HDMI to HDMI cable (for initialization)

### <a name="ccs811"></a>Sensor CCS811 
- This [Adafruit CCS811](https://joy-it.net/en/products/SEN-CCS811V1) sensor is using the I2C protocol
- It has Measurement range: 400 ppm – 8192 ppm for $CO^2$ values
- To get valid data a initial burn-in of 48 hours and a warm-up time of 20 min is recommended.
- There are datasheet and manual available at the homepage of joy-it. The manual also includes an example of how to access the sensor in code. A short summery is available in (subsection - 1.6.4) datasheet documentation and manual are located at the repository for further information.
- Wiring scheme:
 
| sensor pin 	| Raspi pin  	|
|------------	|------------	|
| vdd        	| +5v        	|
| gnd        	| Ground     	|
| sda        	| data line  	|
| scl        	| clock line 	|
| Rst        	| Reset port 	|

### <a name="scd30"></a>Sensor SCD30
-  SCD30 - Sensor Module for HVAC and Indoor Air Quality Applications. it has Integrated temperature and humidity sensor
-  It has Measurement range: 400 ppm – 10.000 ppm for $CO^2$ values
-  works with Digital interface UART or I2C modules
-  further documentation can be found under this [homepage](https://www.sensirion.com/en/environmental-sensors/carbon-dioxide-sensors/carbon-dioxide-sensors-scd30/)

| sensor pin 	| Raspi pin  	|
|------------	|------------	|
| vdd        	| +3v        	|
| gnd        	| Ground     	|
| sda        	| data line  	|
| scl        	| clock line 	|
| Rst        	| Reset port 	|


## <a name="Initial_Setup_of_Raspberry_OS"></a>Initial Setup of Raspberry OS 
After having the new Raspberry or when Need to flash old raspberry to install new  Ubuntu.
Required Things:
1. Brand new Raspberry / Raspberry that need to be flashed new
2. Download thePi Imagerfile and install it from [this link](https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#)
3. If your in Linux InstallPi Imagerby following the command
```sh
 sudo snap install rpi-imager
```
4. choose the OS as [Raspberry pi OS](https://www.raspberrypi.org/software/) 32 bitprobably it will be in first option

<img align="center" src="https://www.raspberrypi.org/app/uploads/2020/03/RPI_intro-e1583228263677.png" width= 400/>

6. insert the sd card and click write
7. After it has been installed you can insert this sd card into raspberry and you have an updated version of linux
    installed on you device.

For the setup of the Raspberry Pi an introduction is given on the Raspberry Pi's official homepage. In the following section a short overview is given. First of all an operating system needs to be downloaded and an image needs to be installed on the SD-card. For this step the Card-Reader is needed. For this project the Raspberry Pi OS Lite (32-bit) is used, which is a port of Debian with no desktop environment. There is an Imager program available to speed up the installation step. The instructions of the program need to be followed and afterward the SD-Card is ready to use. The next step is to connect the Raspberry Pi (Power adapter, LAN-cable, Keyboard and HDMI cable) and to insert the SD-Card. The initial startup is done and thedefault login data is:

- user: pi
- password: raspberry

A few setting needs to be done initially, therefore enter the command:
```sh
sudo raspi-config
```
into the console. The following settings had been changed:

- System Options - Password: the password has been changed tocdl, the username remains  the same 
- System Options - Hostname: the hostname has been changed torpi-cdl(this name will
    be needed later to get the IP of the Raspberry Pi without a monitor)
- Interfacing Options - SSH: enable remote command line access to the Raspberry Pi via SSH
- Interfacing Options - I2C: enable I2C interface and loading the I2C kernel module automatically (will be needed for some of the used sensors)

Afterward the Raspberry Pi needs to be restarted and logged in with the new password. To be sure that the OS and its programs are up-to-date the following commands need to be executed:
```sh
sudo apt-get update
sudo apt-get upgrade
```
## <a name="Send_Sensor_data_to_cloud"></a>Send Sensor data to cloud
### <a name="libraries"></a>Required Libraries for the project

Now, you need to install some packages with the integrated package installer of Pythonpip.
The Required packages are as follows:
- RPi.GPIO
- Adafruit-DHT
- adafruit-circuitpython-ccs811CO2
- azure-iot-device

You can Install these packages by following this syntax below in the command terminal.
```sh
	For example:
	python3 -m pip install <PackageName>	
```
Execute all these commands one by one each:
```sh
	python3 -m pip install RPi.GPIO
	python3 -m pip install Adafruit-DHT
	python3 -m pip install adafruit-circuitpython-ccs811
	python3 -m pip install azure-iot-device
```

### <a name="ssh"></a>Remote access via SSH

It is planned that the AirQuality module will be running continuously in a predefined position (e.g.: in the stairway below the TV), therefore it needs to be accessible remotely without any connected monitor and input device. To solve this requirement, the Raspberry Pi can be accessed via SSH which can be enabled insudo raspi-configas mentioned in subsection. The IP address of the Raspberry Pi can be set as static, to ensure the connection to it. It is also possible to get the IP address with apingcommand on the hostname of the Raspberry Pi from another computer. For Linux it is easy as entering the following command.
```sh
syntax:
ping <pi_hostname>.local
```
For Windows it is needed to add the parameter -4 to the ping command, so that the resolved IP address is in the IPv4 format.
```sh
ping rpi-cdl.local
```
With this IP address it is easy to access the Raspberry Pi with an SSH capable tool like
putty. Figure 1.2 shows a screenshot of the applicationputtywith the local IP address of the Raspberry Pi, the Port 22 and the connection type SSH marked. These settings can be saved and used for later access. If the Raspberry Pi was connected over another LAN-connection, the IP address would have needed to be updated.

### <a name="Deploy"></a>Deploy Code to single Raspberry

To deploy the script to make the raspberry to use just we need `IoTHubDevice.py` script under this directory [IndoorAirQuality_DigitalTwin_Exemplar/physical_twin/hardware_setup/](https://github.com/derlehner/IndoorAirQuality_DigitalTwin_Exemplar/tree/main/physical_twin/hardware_setup) with all required packages installed in the machine. Please follow the procedure below:

Steps to follow:
1. copy the `IoTHubDevice.py` script for each raspberry device under home directry
2. make sure all the packages are installed in it. if not refer the topic above [Required Libraries for the project](#libraries).
3. create new txt file as  `device_id.txt` and enter device id as one line without spaces. this will considered as device_id for that particular device. if not the device will be set to default id as `raspi_01` for example given below:
```ruby
Raspberry_KitchenRoom
```
5. Set the connection string varibale to appropriate string accoding to [azure IoT-Hub readme.md](https://github.com/derlehner/IndoorAirQuality_DigitalTwin_Exemplar/tree/main/digital_twin/azure). And it should be unique for each devices in IoT-Hub
```ruby
CONNECTION_STRING_CCS811 = "<specify the connection string>"
CONNECTION_STRING_SCD_30 = "<specify the connection string>"
```
6. Start run the `IoTHubDevice.py` by python3 by running the command in the cmd terminal
```ruby
python3 IoTHubDevice.py
```
4. Finally the script will start send the data to the cloud

### <a name="DeployMultiDevice"></a>Deploy Code to multiple Raspberries
1. We can use the Automation script for deploying code to multiple raspberries. the scipt can by found in same directory as `auto_deploy_script.py`
2. First addd the 'Destination_file_path', ip_address, user_id, passcode, deviceid as list as shown in the code snippet below in the line 48: 	
```ruby
rasp01 = ['cdlmint_airqualityusecase', '140.78.42.111', 'pi', 'cdl', 'Rasp01']

# ADD MORE RASPBERRY HERE AS THE EXAMPLE SHOWN IN NEXT LINE
#rasp02 = ['haridir', '192.168.0.136', 'pi', 'cdl', 'Rasp02']
```
3. Run the script by the command
```ruby
python auto_depoly_script.py
```
5. This will deploy script on to device which are scpecified in the list with unique device id

###  <a name="Sending"></a>Sending data to IoT-hub

In this section the code of the various components connected to the Raspberry Pi is described. 
Before Continuing please make sure that (1) you completed the previous steps of this tutorial, and (2) your azure environemnt is already setup to make it ready for receiving our data. The Tutorial on how to set up the azure environment is found here: [IndoorAirQuality_DigitalTwin_Exemplar/digital_twin/azure/readme.md](https://github.com/derlehner/IndoorAirQuality_DigitalTwin_Exemplar/tree/main/digital_twin/azure)

In the current folder [IndoorAirQuality_DigitalTwin_Exemplar/physical_twin/hardware_setup/](https://github.com/derlehner/IndoorAirQuality_DigitalTwin_Exemplar/tree/main/physical_twin/hardware_setup) there is a file named **IoTHubDevice.py**  which will be used to get the data from the sensor and send it to the azure environment.

> Note: in IoTHubDevice.py please make sure you have updated `connection_string` from your azure portal: under iot-hub/iot-devices for sending the data from raspberry. further notes can be found under Setup `IoT-Hub`  in [IndoorAirQuality_DigitalTwin_Exemplar/digital_twin/azure/](https://github.com/derlehner/IndoorAirQuality_DigitalTwin_Exemplar/tree/main/digital_twin/azure) 

- After make sure correct packages are installed successfully and Run the **IoTHubDevice.py** script using python v3.


Wait for the sensor to be ready and calibrate the thermistor. First the script is configuring the I2C with the related SCL and SDA pins, then it waits for the sensor to be ready by checking if dataready is true. When finished a temperature offset (tempoffset) will be added to get more accurate results. From this point on the data can be read periodically with a delay in between.

## <a name="Possilble_Frequent_Errors"></a>Possilble Frequent Errors
###### Error: `Script not running in raspberry`:
Make sure you have the updated OS and all lybraries installed and make sure the script is running in `python v3` not in v2

###### Error: `Runtime Errror`: 
Baud Rate of device and sensor isn't matching preferred one is `Baud Rate = '100000'` kHz. process to change is decribed above.

###### Error: `Device not Found`:
Wiring is not good for sensor. you can always check the sensor is in connection by the command:
```sh
sudo i2cdetect -y 1
```
This will show if the device is connected or not. Further detailed discription is under [this link](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)

###### Error: `Try Reapplying the voltage`:
Some wiring connection problem

###### Error: `Constant CO2 value`:
Sensor is not sensing good or sensor calibration is needed.
###### Error: `Data not receieved on Azure`:
Connection string is bad or no device is to receive the data from Azure side



