from sqlite3 import Timestamp
from typing import List


from pydantic import BaseModel,StrictBool

class room(BaseModel):
    roomId:int
    roomSize:int
    ventilator:str
    numberOfPeopleFrom:Timestamp
    numberOfPeopleTo:Timestamp
    numberOfPeople:str
    numberOfPeopleAt:Timestamp   

class airQualityProperties(BaseModel):
    roomId:int
    temperatureFrom: Timestamp
    temperatureTo:Timestamp
    temperature:str
    temperatureAt:Timestamp
    humidityFrom:Timestamp
    humidityTo:Timestamp
    humidity:str
    humidityAt:Timestamp
    co2From:Timestamp
    co2To:Timestamp
    co2:str
    co2At:Timestamp
    """ ventilator:str
    numberOfPeopleFrom:Timestamp
    numberOfPeopleTo:Timestamp
    numberOfPeople:str
    numberOfPeopleAt:Timestamp """
    class Config:
        orm_mode = True

class lights(BaseModel):
    roomId:int
    isOnFrom: Timestamp
    isOnTo:Timestamp
    isOn:str
    isOnAt:Timestamp
    turnOn:StrictBool
    energyConsumption:str
    class Config:
        orm_mode = True

class doors(BaseModel):
    roomId:int
    isOpenFrom: Timestamp
    isOpenTo:Timestamp
    isOpen:str
    isOpenAt:Timestamp
    lock:StrictBool
    unlock:str
    connectsDoor:str
    class Config:
        orm_mode = True

class windows(BaseModel):
    roomId:int
    isOpenFrom: Timestamp
    isOpenTo:Timestamp
    isOpen:str
    isOpenAt:Timestamp
    class Config:
        orm_mode = True

class ventilators(BaseModel):
    roomId:int
    turnOn:StrictBool
    isOnFrom: Timestamp
    isOnTo:Timestamp
    isOn:str
    isOnAt:Timestamp

    class Config:
        orm_mode = True


