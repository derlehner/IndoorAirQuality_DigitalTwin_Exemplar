from sqlite3 import Timestamp
from xmlrpc.client import DateTime
from pydantic import BaseModel
from datetime import datetime


class RoomTable(BaseModel):
    room_id: str
    room_size:int
    measurement_unit:str
  
    class Config:
        orm_mode = True

class UpdateRoomTable(BaseModel):
    room_size:int
    measurement_unit:str
  
    class Config:
        orm_mode = True

class AirQualityPropertiesTable(BaseModel):
    room_id: str
    ventilator:str
    totalnumberofpeople:int
    co2:int
    co2measurementunit:str
    temperature:int
    temperaturemeasurementunit:str
    humidity:int
    humiditymeasurementunit:str
    time:Timestamp
    
    class Config:
        orm_mode = True

class AirQualityTemperatureTable(BaseModel):
    room_id: str
    ventilator:str
    totalnumberofpeople:int
    temperature:int
    temperaturemeasurementunit:str
    time:Timestamp
    
    class Config:
        orm_mode = True

class AirQualityHumidityTable(BaseModel):
    room_id: str
    ventilator:str
    totalnumberofpeople:int
    humidity:int
    humiditymeasurementunit:str
    time:Timestamp
    
    class Config:
        orm_mode = True     

class AirQualityCo2Table(BaseModel):
    room_id: str
    ventilator:str
    totalnumberofpeople:int
    co2:int
    co2measurementunit:str
    time:Timestamp
    
    class Config:
        orm_mode = True             

class Doors(BaseModel):
    room_id: str
    door_id:str
    door_lock:bool
    connectsdoor:str
    connecteddoors:str
    time:Timestamp
    class Config:
        orm_mode = True

class Lights(BaseModel):
    room_id: str
    light_id:str
    turnon:bool
    energyconsumption:int
    energyconsumptionunit:str
    time:Timestamp
    class Config:
        orm_mode = True

class LightOperation(BaseModel):
    
    turnon:bool
    time:Timestamp
    class Config:
        orm_mode = True        

class Windows(BaseModel):
    room_id: str
    window_id:str
    isopen:bool
    time:Timestamp
    class Config:
        orm_mode = True   

class WindowOperation(BaseModel):
   
    isopen:bool
    time:Timestamp
  
    class Config:
        orm_mode = True

class Ventilators(BaseModel):
    room_id: str
    ventilator_id:str
    turnon:bool
    time:Timestamp
    

    class Config:
        orm_mode = True

class VentilatorOperation(BaseModel):
   
    turnon:bool
    time:Timestamp
  
    class Config:
        orm_mode = True
