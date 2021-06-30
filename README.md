Digital Twin Airquality For Covid Risk Assessment

Using Microsoft Azure Cloud Service

#### Hari Shankar

#### Last update:

#### June 30, 2021


## Contents

- 1 Setup: Sensor-Module
   - 1.1 Project Road Map
   - 1.2 Raspberry Pi
   - 1.3 Installing Ubuntu On Raspberry
      - 1.3.1 Raspberry Pi Setup
      - 1.3.2 Remote access via SSH
   - 1.4 Hardware Setup
      - 1.4.1 LED
      - 1.4.2 Buzzer
      - 1.4.3 Temperature and Humidity sensor DHT11
      - 1.4.4 CO2 sensor CCS811
      - 1.4.5 CO2 sensor SCD30
   - 1.5 Required Libraries for the project
   - 1.6 Code
      - 1.6.1 LED
      - 1.6.2 Buzzer
      - 1.6.3 DHT11
      - 1.6.4 CCS811
- 2 Setup: Microsoft Azure
   - 2.1 Create Account
   - 2.2 Install Azure CLI on your PC
   - 2.3 IoT Hub App
      - 2.3.1 Creating the hub app
      - 2.3.2 Usage and further info
   - 2.4 Create Digital Twins Platform
      - 2.4.1 Digital Twin Explorer
      - 2.4.2 To connect DT explorer to your Azure DT:
      - 2.4.3 Creating and uploading the model
   - 2.5 Local development with Azure
      - 2.5.1 Azure in Visual Studio
      - 2.5.2 Visual Studio Code Azure Extension
   - 2.6 Azure library for Python on Raspberry Pi
   - 2.7 Setup Debug Environment for Azure Functions in Visual Studio


# Chapter 1

# Setup: Sensor-Module

### 1.1 Project Road Map

In this section we will discuss about how our project is planned, its working architecture and
data flow. Azure is the things we concentrate on more here as Hardware setup is explained
earlier now its time to concentrate on azure part where this is the place the data is arrived and
plans for further computations.

```
Figure 1.1: Data Flow map from sensor to our Planned applications
```
First a ”Data Receiving point” IOT hub will be created, then a Digital Twins platform will
be created were data flows through it for sake of visualising the entire sensor archetechture. A
related documentation is part of the linked [Quickstart](https://docs.microsoft.com/en-us/azure/digital-twins/quickstart-adt-explorer).

### 1.2 Raspberry Pi

There were already some [Raspberry](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) boards at the CDL available, so it was an easy
decision to go for this hardware platform. Other platforms would be Arduino or even smaller
and cheaper boards, because of the low requirements for this Use-Case.
Required hardware:

- Raspberry Pi 4
- Power adapter for Raspberry Pi 4 (USB-C)
- SD-card
- LAN-cable
- Card-Reader (for initialization)
- Keyboard (for initialization)
- Micro-HDMI to HDMI cable (for initialization)

### 1.3 Installing Ubuntu On Raspberry

This procedure is needed when you bought new Raspberry/need to flash old raspberry to install
new Ubuntu.
Required Things:

<img align="right" src="pictures/piimager.png" width= 400/>

1. Brand new Raspberry / Raspberry that need to be flashed new
2. Download thePi Imagerfile and install it from [Here](https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi##1-overview)
3. If your in Linux InstallPi Imagerby following the command
    sudo snap i n s t a l l r p i−i m a g e r

4. choose the OS asRaspberry pi OS 32 bitprobably it will be in first option
5. insert the sd card and click write
6. After its been installed you can insert this sd card into raspberry and you have freshly
    installed linux on you device.

#### 1.3.1 Raspberry Pi Setup

For the setup of the Raspberry Pi an introduction is given on the [Raspberry Pi homepage](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up).
In the following section a short overview is given.
First of all an operation system needs to be downloaded and an image needs to be installed
on the SD-card. For this step the Card-Reader is needed. For this project the Raspberry Pi


OS Lite (32-bit) is used, which is a port of Debian with no desktop environment. There is an
Imager program available to fasten the [installation step here](https://www.raspberrypi.org/software/). The instructions of the program
need to be followed and afterward the SD-Card is ready to use.
The next step is to connect the Raspberry Pi (Power adapter, LAN-cable, Keyboard and
HDMI cable) and to insert the SD-Card. The initial startup is done and thedefault login
data is:

- user: pi
- password: raspberry
A few setting needs to be done initially, therefore enter the command

sudo raspi-config

into the console. The following settings had been changed:

- System Options - Password: the password has been changed tocdl, the username remains
    the same
- System Options - Hostname: the hostname has been changed torpi-cdl(this name will
    be needed later to get the IP of the Raspberry Pi without a monitor)
- Interfacing Options - SSH: enable remote command line access to the Raspberry Pi via
    SSH
- Interfacing Options - I2C: enable I2C interface and loading the I2C kernel module auto-
    matically (will be needed for some of the used sensors)
Afterward the Raspberry Pi needs to be restarted and logged in with the new password.
To be sure that the OS and its programs are up-to-date the following commands need to be
executed:

sudo apt-get update
sudo apt-get upgrade

#### 1.3.2 Remote access via SSH

It is planned that the AirQuality module will be running continuously in a predefined position
(e.g.: in the stairway below the TV), therefor it needs to be accessible remotely without any
monitor and input device connected. To solve this requirement, the Raspberry Pi can be
accessed via SSH which can be enabled insudo raspi-configas mentioned in subsection
1.3.1. The IP address of the Raspberry Pi can be set as static, to ensure the connection to
it. It is also possible to get the IP address with apingcommand on the hostname of the
Raspberry Pi from another computer. For Linux it is easy as entering the following command.

ping rpi-cdl

For Windows it is needed to add the parameter -4 to the ping command, so that the resolved
IP address is in the IPv4 format.

ping -4 rpi-cdl

With this IP address it is easy to access the Raspberry Pi with an SSH capable tool like
putty. Figure 1.3 shows a screenshot of the applicationputtywith the local IP address of the
Raspberry Pi, the Port 22 and the connection type SSH marked. These settings can be saved
and used for later access. If the Raspberry Pi was connected over another LAN-connection,
the IP address needs to be updated.

<img align="center" src="pictures/puttyScreenshot_marked.png" width= 400/>


Figure 1.3: Applicationputtywith example settings for the SSH connection to the Raspberry
Pi.

### 1.4 Hardware Setup

In this section the setup of the Hardware is further described. Figure 1.4 shows a picture of
the setup of the AirQuality Hardware. The current setup is done on a breadboard, for further
usage it is recommended to solder the components to a board. The AirQuality Sensor-Module
includes the following components:

- LED (currently only one LED is connected, but this can be extended)
- Buzzer (the connection can be used for an Active Buzzer or an Passive Buzzer)
- Temperature and Humidity sensor DHT
- CO2 sensor CCS811 (MOS sensor)
- CO2 sensor SCD30 (NDIR sensor; not connected yet)

Raspberry Pi GPIOs are limited to max. 15 mA current per pin and 50 mA over all GPIOs.
It is recommended to use transistors to keep the current on the GPIOs at a minimum. A
transistor has 3 pins and is connected between the GPIO and the component, which should
be connected to the GPIO. The current is taken from the 3.3 V or 5 V supply pin and it
needs to be connected to the ground too. An example can of such a circuit is shown in figure
??in subsection 1.4.1 LED. The transistor prevents that the component is using too much
current from the GPIO and instead is using the voltage suppy pin to power the component.
The complete circuit diagram of the current state of the AirQuality Raspberry Pi Module is
shown in figure 1.5. Table 1.1 lists all the components connected to the AirQuality Raspberry
Pi and their connected pin and GPIO references.

#### 1.4.1 LED

The LEDs will be used to give a visual response to the user about the CO2 amount in the air
and therefor about the air quality. It should be used as an indicator to open the windows and
insert fresh air into the room. At the moment only one LED is connected to the board and
is used as an indicator, that a set of telemetry is sent to the hub. The LED used was already
part of the CDL equipment and i was not sure if it was part of the Arduino Sensor Pack, which

<img align="center" src="pictures/fotoHWAll.jpg" width= 400/>


```
component pin GPIO
LED Pin 11 GPIO 17
Buzzer Pin 13 GPIO 27
DHT11 Pin 15 GPIO 22
CCS811 SDA Pin 3 GPIO 2 (SDA)
CCS811 SCL Pin 5 GPIO 3 (SCL)
```
Table 1.1: List of components connected to the AirQuality Raspberry Pi with related pin and
GPIO references.

would include some specification for the components. The specification for the LED of the
Arduino Pack listed the LEDs as follow:

```
Color V (max) mA (peak)
red 2.0 (2.5) 50 (100)
yellow 2.0 (2.5) 50 (100)
green 3.6 (4.0) 20 (50)
```
```
Table 1.2: Specification values for LED of Andurino Sensor Set
```
The values for the calculation needs to be in between the two values listed in the table 1.
The LED connection is done indirect over a transistor, so that the GPIO of the Raspberry
Pi is not stressed out. See image /reffigure:circuitLED for the circuit diagram. The circuit
consists of an LED, two resistors and a transistor. One resistor is set between the GPIO and
the transistor, the other one is set between the power source and the LED, which is connected
to the transistor. Depending on the transistor and LED in use, the resistors need to be sized
accordingly.
More information on how to access the LED in Python can be found in subsection 1.6.1.

<img align="center" src="pictures/circuitAll_marked.png" width= 400/>

Figure 1.5: Circuit diagram of current AirQuality Raspberry Pi Setup. The supply and ground
connection are marked: blue - ground, yellow - 3.3 V supply, red - 5 V supply.

<img align="center" src="pictures/circuitLED.png" width= 400/>


#### 1.4.2 Buzzer

The buzzer will be used to give an acoustical response to the user. It should be used as an
indicator to open the windows and insert fresh air into the room. At the moment the buzzer
is not used in code. Both active and passive Buzzer need a 5 V power supply. The connection
of the GPIO is also done via transistor, but only one resistor is needed between the GPIO and
the transistor, because the buzzer itself does not need an additional one. There are two types
of buzzers, active and passive. In the Arduino Sensor Pack is one of each available. There is
no difference in connecting them, but there is a difference in accessing them via code. At the
moment, the passive buzzer is connected.
For more information on how to access a buzzer (active and passive), see subsection 1.6.2.

#### 1.4.3 Temperature and Humidity sensor DHT11

The DHT11 sensor is used because this sensor was already available at the CDL and is part of
the sensor set for Arduino. This sensor is connected via single wire. Because the sensor given
is already on a module, there is no need for filtering capacitor and pull-up resistor on the data
wire. Both are available on the module. The sensor is connected to a GPIO, the 3.3 V power
supply and the ground. To access the sensor in code a Python package is available. (More in
subsection 1.6.3 in section Software Setup). A datasheet is located at the repository for further
information.

#### 1.4.4 CO2 sensor CCS811

This sensor is using the I2C protocol, because of that, the I2C was enabled in raspi-config. The
wiring is simple, the SDA (data) and SCL (clock) pins of the sensor need to be connected to
the SDA and SCL pins on the Raspberry Pi. It is based on the MOS (metal oxide semicon-
ductor) principle and can provide a total volatile organic compound (tVOC) or carbon dioxide
equivalent (eCO2) level as well as a temperature value. The eCO2 value is not as accurate as
an CO2 value and can only be used as a reference.
To get valid data a initial burn-in of 48 hours and a warm-up time of 20 min is recommended.
There are datasheet and manual available at the homepage of [joy-it](https://joy-it.net/en/products/SEN-CCS811V1). The manual also includes
an example of how to access the sensor in code. A short summery is available in subsection
1.6.4 datasheet and manual are located at the repository for further information.

#### 1.4.5 CO2 sensor SCD30

This sensor is using the i2C protocol too. The wiring is the same as for the CCS811 sensor. It
is based on the NDIR (non-dispersive infrared) principle and can provide a CO2 value and a
temperature value. NDIR sensors are more accurate and durable than MOS sensors, but they
are more expensive.
At the moment this sensor is not connected to the AirQuality Sensor-Modul, but it is
compatible with the Raspberry Pi and an extension with it should be easy. There are libraries
for Python and C available to access the sensor via code. The datasheet can be located at the
repository for further information.



### 1.5 Required Libraries for the project

Now, you need to install some packages with the integrated package installer of Pythonpip.
You can do this by entering the following command, where<PackageName>represents the name
of one of the packages listed in table 1.3.

python3 -m pip install <PackageName>

```
Package for Link to section
RPi.GPIO Raspberry Pi GPIO (LED & Buzzer) 1.6.1, 1.6.
Adafruit-DHT temperature sensor DHT 1.6.
adafruit-circuitpython-ccs811 CO2 sensor CCS811 1.6.
azure-iot-device Azure IoT device functions 2.
```
Table 1.3: Python packages needed for this project on the Raspberry Pi with links to the
related sections.

### 1.6 Code

In this section the code of the various components connected to the Raspberry Pi is descried
with examples and links to resources.

#### 1.6.1 LED

To access the GPIOs of the Raspberry Pi the packageRPi.GPIOis used. There are other
packages available too, but this documentation will stay with this package. To simplify the later
code it is possible to useimport RPi.GPIO as GPIOso you can access the functions behind by
simply usingGPIO.as used later in this section and in the project. Code snipped used in this
section are from/home/pi/py_code/gpio_test.pyon the Raspberry Pi and on the repository.
First the GPIO mode needs to be set to access the pins by GPIO number:

GPIO.setmode(GPIO.BCM)

The other mode isGPIO.BOARDthat will set the pins to be accessed by the pin number. Second
the GPIO needs to be set as output, because you want to send signals out to the LED.

RED_LED_GPIO = 17
GPIO.setup(RED_LED_GPIO, GPIO.OUT)

The variable for the GPIO is used, because it will be needed more often.
To enable the LED you will need to set the output to HIGH.

GPIO.output(RED_LED_GPIO, GPIO.HIGH)

To disable the LED you will have to set the output to LOW, by simply replace the HIGH with
a LOW in the command above. If you want the LED to blink, you just need the output to
toggle with a delay in between.

for x in range(3):
GPIO.output(RED_LED_GPIO, GPIO.HIGH)
time.sleep(1)
GPIO.output(RED_LED_GPIO, GPIO.LOW)
time.sleep(1)


#### 1.6.2 Buzzer

To access the buzzer you will need the same steps as for the LED in subsection 1.6.1 to enable
the GPIO and access it. If the active buzzer is connected, it will make a sound if you send a
HIGH to the GPIO followed by a delay and then a LOW. Similar to the LED, but in this case
the delay will set the note of the sound.

GPIO.output(BUZZ_GPIO, GPIO.HIGH)
time.sleep(3)
GPIO.output(BUZZ_GPIO, GPIO.LOW)

If you want a sound like a siren, you will need to put this into a loop.
With the passive buzzer it is on the one side more complicated to get a sound out of it,
but on the other side it is easier to control the note of the sound. You could even create an
instrument with it. To initiate the passive buzzer use the following command in addition to
setting the GPIO as output.

p = GPIO.PWM(BUZZ_GPIO, 1)
p.start(0)
time.sleep(1)

This sets the pin to PWM which allows you to send a continues stream. To generate a sound
the output needs to be a sinus wave. The next code snipped demonstrate a possible address of
the buzzer:

p.start(50)
for x in range (0,361):
sinVal = math.sin(x * (math.pi / 180.0))
toneVal = 2000 + sinVal * 500
p.ChangeFrequency(toneVal)
time.sleep(0.001)
p.stop()
time.sleep(1)

The sound will change with the frequency used to send to the PWM output.

#### 1.6.3 DHT11

There are a lot of libraries available for the DHT11 temperature and humidity sensor. For this
project we used the Python library [AdafruitDHT](https://github.com/adafruit/Adafruit_Python_DHT/). There is a problem with the detection of
the Raspberry Pi, that need some fixes. The library is checking, which version of Raspberry
Pi or Beaglebord is used. But the Version for Raspberry Pi 4 is not covered and needs to be
added. You will get an error, that there is no Raspberry Pi or Beagleboard found. To fix this
you need to go to the directory on the Raspberry Pi where the library is:

/usr/local/lib/python3.7/dist-packages/Adafruit_DHT

Here you need to open and change the fileplatformdetect.py. The script is reading the file
/proc/cpuinfoand checks if the entry forHardwareis matching with one of the requested
versions. At the end of the file you will find a functionpiversion. Inside this function you
will find a search with a Regex and a if-elif-else construct afterwards. To fix the problem, you
need to add anelifreferencing the Hardware version for the Raspberry Pi 4 like this:




```
elif match.group(1) == ’BCM2711’:
# Pi 4b
return 3
```
You can check the cpuinfo if the version isBCM2711or just use the lines above and retry to
use the library. The library should work as intended after this fix and there where no further
issues detected.
The filesensortestDT11.pyis situated in thepicodefolder and has an example im-
plementation to access the DHT11 sensor. The current values are requested with the following
function:

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

The variables humidity and temperature are floats and can then be used for further use.

#### 1.6.4 CCS811

Adafruit provides a Python library for the [CCS811 sensor](https://github.com/adafruit/Adafruit_CircuitPython_CCS811). In subsection Python and Libraries
1.5 you will find more information on how to install the library. This sensor is using I2C for
communication, therefor it is important to activate it like mentioned in subsection Raspberry
Pi Setup 1.3.1.
The example below is located on the Raspberry Pi inside thepycodefolder namedsen-
sortestCCS811.py.
i2c = busio. I2C ( board .SCL, board .SDA)
ccs811 = adafruit ccs811. CCS811( i2c )
print ( ccs811 )
# Wait f o r the sensor to be ready and c a l i b r a t e the thermistor
while not ccs811. data ready :
pass
temp = ccs811. temperature
ccs811. temp offset = temp− 25.

while True :
print (”CO2: {}PPM, TVOC: {} PPM, Temp: {} C”. format ( ccs811. eco2 , ccs811. tvoc , ccs811. temperature ))
time. sleep ( 0. 5 )
First the script is configuring the I2C with the related SCL and SDA pins, then it waits for
the sensor to be ready by checking if dataready is true. When finished a temperature offset
(tempoffset) will be added to get more accurate results. From this point on the data can be
read periodically with a delay in between.


# Chapter 2

# Setup: Microsoft Azure

Microsoft Azure is a cloud solution with a lot of recources and services. The once that are
interessting for this project and are covered by this documentation. The following sections
describe the relevant steps to get an Azure Setup needed for this project. All information
covered by this chapter are also covered by the documentation of Microsoft. The links with the
related steps will be linked in the footnodes.

### 2.1 Create Account

It is possible to get a free Microsoft Azure account, but it is recommended to create an Microsoft
Azure student account, because it will apply$100 credit to the account.
To create an Microsoft Azure student account it is necessary to have 2 different e-mail
addresses:

- The academic e-mail address (@jku.at) to verify you are eligible or the student account,
- another e-mail address, that will be used as login and main e-mail address for Azure.

[This Link](https://azure.microsoft.com/en-us/free/students/) leads to the sign-up page of Microsoft Azure for Students. To start,
the ”Activate now” button needs to be pressed. Then you need to sign in with an existing
Microsoft account or create a new one, but keep in mind that you do not use your academic
e-mail address. While following the sign-in instructions you will need to state your country
and date of birth. Furthermore you will need to confirm your e-mail address by entering a
verification code which will be sent to you (watch your Spam folder). If everything is fine you
have a new Microsoft account incl. Microsoft Azure or you have a new Microsoft Azure account
linked to your existing Microsoft account. Either way in the next step you will need to confirm
your academic status with entering your academic e-mail address. Now you have a new account
and can start with the next steps.

### 2.2 Install Azure CLI on your PC

Azure CLI is available for Windows, macOS and Linux. There is a [related documentation](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
available for the different operating systems. After the installation it is possible to access Azure
via terminal with the keywordaz. There are extensions of commands that are related to [Digital Twins](https://docs.microsoft.com/en-us/cli/azure/ext/azure-iot/dt?view=azure-cli-latest) (az dt) and [IoT hub](https://docs.microsoft.com/en-us/cli/azure/iot?view=azure-cli-latest) (az iot).




For working on azure azure CLI is one of recommended thing to be installed on working
device (not on raspi). It can be done using commends below you can find the details:

- Linux by single line command:
    curl -sL https://aka.ms/InstallAzureCLIDeb — sudo bash
- On Windows and Others:
    https://docs.microsoft.com/en-us/cli/azure/install-azure-cli

With Azure CLI it is possible to sign into your Azure account and do most of the steps, that
are possible at the Azure Portal homepage. It is recommended to install Azure CLI because it
is the easiest way to log into your Azure account and some steps are done via Azure CLI in the
documentation. The reference for Azure CLI is [available online](https://docs.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest).

### 2.3 IoT Hub App

This is one of the services which Azure enables highly secure and reliable communication
between your Internet of Things (IoT) application and the devices it manages. Azure IoT Hub
provides a cloud-hosted solution back end to connect virtually any device.

<img align="center" src="pictures/iothubhomepage.png" width= 400/>


IoT Hub is the entry point to the data which we actually want to work on after receiving here
we have huge options to work on with. We can use the IoT app as a source for other azure
services. In this section an Azure IoT hub will be created. A related documentation is part of
the [linked Quickstart](https://docs.microsoft.com/en-us/azure/iot-hub/quickstart-send-telemetry-python#create-an-iot-hub).

#### 2.3.1 Creating the hub app

1. In the azure resources search for IoT Hub
2. click create
3. Using this required data create the azure app. The required data:
- Resource group
- Resource Locationd
- IOT hub Name

<img align="center" src="pictures/iothub.png" width= 400/>



#### 2.3.2 Usage and further info

- Manage IoT Devices (make successful connections for data transfer)
- You can send Telemetry-data securely from physical hardware (sensor) to Azure. For info
    [refer this website](https://docs.microsoft.com/en-us/azure/iot-hub/quickstart-send-telemetry-python)
- Using ‘Message Routhing’ option telemetry messages can be sent to : Events, Storage,
    Event Hubs and much more.

<img align="center" src="pictures/iotrouting.png" width= 400/>


For further info:


- About[ IOT Hub](https://channel9.msdn.com/Shows/Azure-Friday/Azure-IoT-Hub?term=iot)
- For [Device Streaming](https://channel9.msdn.com/Shows/Internet-of-Things-Show/Azure-IoT-Hub-Device-Streams?term=iot)
- IOT to [Event Grid Integration](https://channel9.msdn.com/Shows/Internet-of-Things-Show/IoT-Devices-and-Event-Grid?term=iot)

### 2.4 Create Digital Twins Platform

Azure Digital Twins is an Internet of Things (IoT) platform that enables you to create a digital
representation of real-world things, places, and business processes. Azure Digital Twins is an
IoT platform that enables the creation of comprehensive digital models of entire environments
to gain insights that drive better products, optimization of operations, cost reduction and
breakthrough customer experiences. Examples include buildings, factories.

- Model any environment and bring digital twins to life in a scalable and secure manner.
- Connect assets such as IoT devices as well as existing business systems to Azure Digital
    Twins.

<img align="center" src="pictures/digitaltwinhomepage.png" width= 400/>


In this section a Digital Twins platform will be created. A related documentation is part of
the [linked Quickstart](https://docs.microsoft.com/en-us/azure/digital-twins/quickstart-adt-explorer).

1. Search for”Azure Digital Twin”in [azure resource](https://portal.azure.com)
2. You will need to press the Button+ Addat the Azure Digital Twins page.
3. At the next page you will have to add
    - a resource group,
    - a location and
    - a name for the Digital Twins service.

<img align="center" src="pictures/digitaltwincreation.png" width= 400/>

In above figure you can find the”Host Name”where you can find in DT homepage is the
string should be noted. It is used further for installing DT Explorer.
The resource group will be later used for all other resources related to the AirQuality project.
It needs to be created, if this wasn’t done before. To do so, press theCreate newbutton
below the Resource group selection. You only need a name or the resource group to do so.
Regarding location, it is worth to mention that the Digital Twins resource is only available
for Australia East, East US, East US 2, North Europe, South Central US, Southeast Asia,
UK South, West Central US, West Europe and West US 2 at the moment. These locations
are the locations of the Azure servers. For the current instance for the AirQuality project the
locationWest Europewas chosen. If everything is filled out, you can continue by clicking the
Review + createbutton at the lower left corner. A short summery to check again will be
listed. By pressing theCreatebutton in the lower left corner you will finish the creation. The
deployment will take some. A window in the upper right corner will show you a message when
completed.

#### 2.4.1 Digital Twin Explorer

Digital Twin Exploreris the easy way to visualise our model architecture, import, export
our models. This should be installed in our pc. Requirements for DT Explorer: Node.js (not
less then version 10), npm. The process to install DT Explorer:

1. Installing node.js on ubuntu by command line:
    sudo a p t i n s t a l l c u r l
       c u r l −sL h t t p s : / / deb. n o d e s o u r c e. com/ s e t u p 1 0. x | sudo −E bash −
    sudo a p t i n s t a l l n o d e j s
2. Download and extract the Digital Twin Explorer files []]:^13
2. Download and extract the Digital Twin Explorer files [from the git]()




3. Run terminal under this directory: digital-twins-explorer-main/client/src
4. Run the command: to install the npm
    npm i n s t a l l
5. Run the command: to start the DT Explorer
    npm run s t a r t
<img align="center" src="pictures/dtexplorer.png" width= 400/>


#### 2.4.2 To connect DT explorer to your Azure DT:

1. Copy host name from your Digital twin home page, and add‘https://’ in front for
    example:
    https://DigitalTwin-DigitalTwinApp.api.weu.digitaltwins.azure.net
2. Then click login icon on top right on DT explorer you already opened Paste the string
    here and click ok. You will be now connected to the azure

#### 2.4.3 Creating and uploading the model

1. All dt models should be written in .json file

2. Open your favourite code editor and create new .json file
<img align="center" src="pictures/dtexplorer.png" width= 400/>

3. This code above is the example simple model which contains ‘temperature’ and ‘Humid-
    ity’: It is based on azure dtdl language. [More about it](https://docs.microsoft.com/en-us/azure/digital-twins/concepts-models)
4. For uploading click the upload button on DT explorer and select the .json file you created before. Then your model will be shown below.

<img align="center" src="pictures/uploadmodel.png" width= 200/>

5. Then finally the model is created and will be visualised if added to explorer.
<img align="center" src="pictures/dtmodel.png" width= 400/>


### 2.5 Local development with Azure

There are three ways to improve working with Azure on a local maschine.

- Install Azure CLI
- Azure in Visual Studio
- Azure in Visual Studio Code

This section will give a overview and short installation guides of this features.

#### 2.5.1 Azure in Visual Studio

The easiest way to create Azure related programs (e.g.: Azure Functions) is by using Visual
Studio. It is important, that the version of Visual Studio is 2019 or higher, because with version
2019 Azure was integrated into the basic installation. Otherwise you will need to install the
Azure Plug-in. To login your Azure account, you will need to log in Visual Studio with your
Microsoft account, that is linked to your Azure account (the one used for creating the Azure
account) and you are ready to go.




Visual Studio has a lot of functionalities that help you create Azure Functions and so on.
For further information about the usage of Visual Studio with Azure Functions, please check
[the documentation](https://docs.microsoft.com/en-us/azure/azure-functions/functions-develop-vs).
For the AirQuality project Visual Studio 2019 was used to implement Azure functions.

#### 2.5.2 Visual Studio Code Azure Extension

If you prefer Visual Studio Code or are working with a operating system that do not support
Visual Studio, there are extensions available for Azure in [Visual Studio Code](https://code.visualstudio.com/docs/azure/extensions). The extensions
are available in a package calledAzure App Serviceor can be installed separately as needed.
A documentation on how to create a Azure function in Visual Studio Code is [available online](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-csharp).

### 2.6 Azure library for Python on Raspberry Pi

There is a documentation available on how to install Azure library [packages for Python](https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-install) and
the code to the Python Device SDK for IoT Hub can be [found on github](https://github.com/Azure/azure-iot-sdk-python/tree/master/azure-iot-device).
For this project the library namedazure-iot-deviceis needed. To install simply usepip
with the following command:

python3 -m pip intall azure-iot-device

To use the library you will need toimport azure-iot-deviceor one of the included classes
or packages.

from azure.iot.device import IoTHubDeviceClient, Message

This is an example that is used in the IoTHubDevice.py script??on the Raspberry Pi. To get
more information about the library you can check the documentation and github links or you
start a python shell, import the library and execute the help command:

python
import azure.iot.device
help(azure.iot.device)

This can be also done for classes or packages inside the library.
Additional libraries that are of interests:

- azure-iot-hub
- azure-iothub-device-client
- azure-iothub-service-client

To use the libraries you will need to install them with pip as mentioned earlier in this section.

### 2.7 Setup Debug Environment for Azure Functions in Visual Studio

Azure Functions are services that are running in the cloud. For debugging it is possible to
connect to the Azure environment in order to access services like IoT Hub and Digital Twins.
There is a good article on how to setup the debugging for Azure Function Event Grid Trigger,
that are used for this project, in the [Azure documentation](https://docs.microsoft.com/en-us/azure/azure-functions/functions-debug-event-grid-trigger-local). To give a little inside, you will
need to create a local server instance and make a event subscription with a Web Hook endpoint
to a storage event on Azure Portal.
Keep in mind that the local server instance is time-limited to 2 hours and you will need to
update the endpoint in Azure evertime the server is restarted.


### 2.8 Physical Model
This is to show sample [click here](https://github.com/derlehner/DigitalTwin_Airquality_For_Covid_Risk_Assessment/tree/development/applications/physical_model) it should land to physical model readme.