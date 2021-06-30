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