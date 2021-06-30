# Send Data from IoT Hub to Azure Digital Twin 



**Introduction**

This project briefly describes about creation of IoT Hub, digital twin and communication between them. The main goal is to measure and predict COVID-19 risk with mock up sensor data. In this project, we will set up IoT hub and Azure Digital Twin and send telemetry data from IoT device to Digital Twin

**Prerequisites**

Azure account subscription
[DL] We can set a link here to the readme file where the creation of the azure account is described

**Resources**

1. IoT Hub

2. Azure Digital Twin

[DL] We can also set links to the tools here.

**IoT Hub Setup:**

what is IoT Hub?

**IoT Hub** is a Platform-as-a-Services (PaaS) managed service, hosted in the cloud, that acts as a central message **hub** for bi-directional communication between an **IoT** application and the devices it manages

1. Create a new resource, IoT Hub by typing in the search bar,create new resource group for managing all the azure resources.

Create IoT Hub by specifying subscription, resource group, region and assign IoT hub name

**Azure Digital Twin**

what is Azure Digital Twin?

Azure Digital Twin is an Internet of Things (IoT) platform that enables users to create digital representation of real-world things and monitor the asset, component or process in real-time

   **Workflow**



![Workflow](./images/01.jpg)



**IoT Hub Setup**

1. Create a new resource IoT Hub by typing in the search bar,we require resource group for managing all the azure resources, if it not created then create new resource group and add IoT Hub to the resource group. Choose your Azure subscription, resource group, region and assign IoT Hub name

![IoTHub](https://github.com/derlehner/DigitalTwin_Airquality_For_Covid_Risk_Assessment/tree/development/raspberry/simulation/images/02.jpg)



2. Create IoT device in IoT Hub, provide device id name , for instance we have assigned device id as twinModel, After successful creation, list of IoT devices appears as shown below

   

![IoTDevice](https://github.com/derlehner/DigitalTwin_Airquality_For_Covid_Risk_Assessment/tree/development/raspberry/simulation/images/03.jpg)



3. Create a separate consumer group for IoT Hub to send data from IoT Hub to other cloud resources. Go to IoT Hub → Built-in endpoints → Events and create consumer group under Events section

   ![IoTconsumergroup](https://github.com/derlehner/DigitalTwin_Airquality_For_Covid_Risk_Assessment/tree/development/raspberry/simulation/images/04.jpg)



**Client App for Mock-up data generation**

Prepare the client application to send mock-up telemetry data to the created IoT device
[DL] we have to put the code for this client app into this github folder, and then reference the files from here
[DL] Then, we can first describe the adaptations that a user has to do after downloading the code, and then which commands has to be entered in order to send example data to the created service

1. Required libraries:

   1.a) azure.iot.device

   The client app could be developed using any of the languages Python, C#, Java, JavaScript Go. We are using Python to create the client app and the script is as follows.

   ```python
   import random
   import time
   from azure.iot.device import IoTHubDeviceClient, Message
   # The device connection string to authenticate the device with your IoT hub.
   # Using the Azure CLI:
   # az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
   CONNECTION_STRING = "HostName=Ramya-IoTHub.azure-devices.net;DeviceId=twinModel;SharedAccessKey=KzmFZY2yj889Yc3t64wX8WFcEJMwOrxhVWnlKk7ezB4="
   
   # Define the JSON message to send to IoT Hub.
   TEMPERATURE = 20.0
   HUMIDITY = 60
   CARBONDIOXIDE=1000
   TSID="5d9d9cb1-f5cd-43a5-af86-83bb1ef9dc2d"
   MSG_TXT = '{{"Temperature": {Temperature},"Humidity": {Humidity},"CarbonDioxideValue":{CarbonDioxideValue},"tsId":{tsId}}}'
   
   def iothub_client_init():
       # Create an IoT Hub client
       client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
       return client
   
   def iothub_client_telemetry_sample_run():
   
       try:
           client = iothub_client_init()
           print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
   
           while True:
               # Build the message with simulated telemetry values.
               Temperature = TEMPERATURE + (random.random() * 15)
               Humidity = HUMIDITY + (random.random() * 20)
               CarbonDioxideValue=CARBONDIOXIDE+(random.random()*2)
               tsId=TSID
               msg_txt_formatted = MSG_TXT.format(Temperature=Temperature, Humidity=Humidity,CarbonDioxideValue=CarbonDioxideValue,tsId=tsId)
               message = Message(msg_txt_formatted)
   
               # Add a custom application property to the message.
               # An IoT hub can filter on these properties without access to the message body.
               if Temperature > 30:
                 message.custom_properties["temperatureAlert"] = "true"
               else:
                 message.custom_properties["temperatureAlert"] = "false"
   
               # Send the message.
               print( "Sending message: {}".format(message) )
               client.send_message(message)
               print ( "Message successfully sent" )
               time.sleep(1)
   
       except KeyboardInterrupt:
           print ( "IoTHubClient sample stopped" )
   
   if __name__ == '__main__':
       print ( "IoT Hub Quickstart #1 - Simulated device" )
       print ( "Press Ctrl-C to exit" )
       iothub_client_telemetry_sample_run()
   
   ```

   

The client app is connected with IoT device using the device connection string,replace the connection string property with your own  IoT device primary connection string of the to which the telemetry data is to be sent.

**Get the IoT device connection string**

Go to IoT Hub ---> click on specific IoT device to which you need to send data ---> detailed view of IoT device with properties such as device id, primary and secondary key etc

![IoTconnectionstring](https://github.com/derlehner/DigitalTwin_Airquality_For_Covid_Risk_Assessment/tree/development/raspberry/simulation/images/05.jpg)

copy paste the connection string into the python script.

python function description:

1. iothub_client_init()

Initializes the Azure IoT Hub 

2. iothub_client_telemetry_sample_run()

if client is initialized then set up  telemetry data properties with random values

Telemetry properties :

1. Temperature

2. Humidity

3. CarbonDioxideValue

   

   **Run the Client App**

   Using windows command line navigate to the python file and run python script with command

   ```python
   python {filename.py}
   ```

   **Output of the Client App**

   ![outputClientApp](https://github.com/derlehner/DigitalTwin_Airquality_For_Covid_Risk_Assessment/tree/development/raspberry/simulation/images/09.jpg)



**Testing the Client App:**

**Method-1:** IoT Hub Overview

To verify if the telemetry data is sent to Azure IoT Device , there are metrics charts in IoT hub that shows the incoming device to cloud messages, messages used per day etc

![outputIoTOverview](https://github.com/derlehner/DigitalTwin_Airquality_For_Covid_Risk_Assessment/tree/development/raspberry/simulation/images/07.jpg)



**Method-2:** Azure CLI

Open the cloud shell from Azure portal and you need to create storage account when using it for first time.

Two cloud shells are present you can use either of them to test

1. PowerShell -command line for **windows** and 

2. Bash- command line for **Linux** operating system

   Install extensions in Azure CLI before using IoT commands

   **Required Extensions:**

   1. azure iot extension

   ```python
   az extension add --name azure-cli-iot-ext
   ```

   **Monitor the events of IoT Hub device**

   ```python
   az iot hub monitor-events --hub-name {iot hub name} --device-id {digital twin name} --consumer-group {consumer group name of iot hub events}
   ```

   Replace the IoT Hub name, digital twin name and consumer group name accordingly.

   We can see that telemetry data sent from client app is received in the Azure IoT digital twin model

   ![outputAzureCLI](https://github.com/derlehner/DigitalTwin_Airquality_For_Covid_Risk_Assessment/tree/development/raspberry/simulation/images/08.jpg)





