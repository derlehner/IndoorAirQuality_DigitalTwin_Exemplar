# Send Data from IoT Hub to Azure Digital Twin 

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

# FOR SETTING UP NEXT STEP
For sending the data succefully you need to setup the Azure which you can see the entire (process here)[https://github.com/derlehner/DigitalTwin_Airquality_For_Covid_Risk_Assessment/blob/development/azure/readme.md].

=======
>>>>>>> d33a7b984ab2e45aee127af3526c7b4387c032be:raspberry/actual_data/README.md





