class TimeScaleService:
    
    def send_data(device_id, sensor_id, property_name, timestamp, value):
        jsonObjects={}
        url="http://140.78.155.6:5000/api/sensordata"
        headers = {
        'Content-Type':'application/json', 
        'Accept':'application/json'}

        # TODO: sent data should be in format [device_id, sensor_id, property_name, timestamp, value]

        co2,temp,hum=raspi_sensordata.split(',')
        jsonObjects['sensorname']='scd30'       # SENSOR NAME
        jsonObjects['roomnumber']='s30076'      # ROOM NUMBER
        jsonObjects['co2']=float(co2)           # CO2 VALUE
        jsonObjects['temperature']=float(temp)  # Temp VALUE
        jsonObjects['humidity']=float(hum)      # Hum VALUE
        jsonformat=json.dumps(jsonObjects)      # DUMPING DATA TO BE SENT
        postdata=requests.post(url,headers=headers,data=jsonformat)     # SENDING THE DATA
        if postdata.status_code==201:
            print('Sensor data sending successfully....')
        else:
            print(postdata.text+'Failed to post Sensor data to server!')
        return response