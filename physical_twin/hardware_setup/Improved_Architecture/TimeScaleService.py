class TimeScaleService:
    
    def send_data(device_id, sensor_id, property_name, timestamp, value):
        jsonObjects={}
        url="http://140.78.155.6:5000/api/sensordata"
        headers = {
        'Content-Type':'application/json', 
        'Accept':'application/json'}

        # TODO: sent data should be in format [device_id, sensor_id, property_name, timestamp, value]

        jsonObjects['sensorname']= sensor_id       # SENSOR NAME
        # TODO: change roomnumber to deviceId (also in Timescale DB on Webserver)
        jsonObjects['roomnumber']=device_id      # ROOM NUMBER
        # TODO: make sure that the server accepts requests where only one of temperature, humidity and co2 is sent, NOT all three at once
        jsonObjects[property_name]=float(value)           # CO2 VALUE
        # TODO: add timestamp to request
        jsonformat=json.dumps(jsonObjects)      # DUMPING DATA TO BE SENT
        response=requests.post(url,headers=headers,data=jsonformat)     # SENDING THE DATA
        if response.status_code==201:
            print('Sensor data sending successfully....')
        else:
            print(response.text+'Failed to post Sensor data to server!')
        return response