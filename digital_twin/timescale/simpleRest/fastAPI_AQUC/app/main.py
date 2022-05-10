from asyncio.log import logger
from datetime import datetime
from typing import List
from pip import main
import uvicorn
from fastapi import FastAPI, status,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from session import db_Session 
from databases import Database

# import the schema 
from schema import Room,Airqualityproperty

#import db models
from models import Room_Object,Update_RoomObject,AirQuality_Properties_Object,AirQuality_Temperature_Object,AirQuality_Humidity_Object,AirQuality_Co2_Object
# establish connection
import client
#ngrok

import nest_asyncio
import sys 
from pyngrok import ngrok

database = Database(settings.DATABASE_URL)

def init_webhooks(base_url):
    # Update inbound traffic via APIs to use the public-facing ngrok URL
    pass



app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
""" 
if settings.USE_NGROK:
    from pyngrok import ngrok
    port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else 8000

   
    public_url = ngrok.connect(port).public_url
    logger.info("ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))
    settings.BASE_URL = public_url
    init_webhooks(public_url) """
# room
@app.post("/Rooms/",response_model=Room_Object, status_code = status.HTTP_201_CREATED)
#@measure_energy
async def add_Room(addRoom:Room_Object):
    db_classes = Room(room_id=addRoom.room_id,room_size=addRoom.room_size,measurement_unit=addRoom.measurement_unit)
    try:
        db_Session.add(db_classes)
        db_Session.flush()
        db_Session.commit()
    except Exception as ex:
        logger.error(f"{ex.__class__.__name__}: {ex}")
        db_Session.rollback()
   
    return addRoom
 
@app.get("/Rooms/", response_model=List[Room_Object], status_code = status.HTTP_200_OK)
async def get_AllRoom_Details():
    """ query = 'SELECT * FROM room'
    cur.execute(query)
    for i in cur:
        print(i) """
    results=db_Session.query(Room).all()
    return results         

@app.get("/Room/{room_id}/", response_model=List[Room_Object], status_code = status.HTTP_200_OK)
async def get_Specific_Room(room_id:str):
    specificRoomDetail=db_Session.query(Room).filter(Room.room_id==room_id).all()        
    return specificRoomDetail

@app.put("/Room/{room_id}",status_code = status.HTTP_200_OK)
async def update_RoomDetails(room_id:str,request:Update_RoomObject):
    updateRoomDetail=db_Session.query(Room).filter(Room.room_id==room_id)
    if not updateRoomDetail.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Room with the id {room_id} is not available')
    updateRoomDetail.update({'room_size':request.room_size,'measurement_unit':request.measurement_unit})
    db_Session.commit()
    return {"code":"success","message":"updated room"}

@app.delete("/Room/{room_id}", status_code = status.HTTP_200_OK)
async def delete_Room(room_id:str):
    deleteRoom=db_Session.query(Room).filter(Room.room_id==room_id).one()
    if not deleteRoom:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Room with the room id {room_id} is not found')
    db_Session.delete(deleteRoom)
    db_Session.commit()
    return {"code":"success","message":f"deleted room with id {room_id}"} 
  
# airQualityinRoom

@app.post("/Room/AirQuality/", response_model=AirQuality_Properties_Object, status_code = status.HTTP_201_CREATED)
async def add_AirQuality_Properties(addAirQuality:AirQuality_Properties_Object):
    db_AQP=Airqualityproperty(room_id=addAirQuality.room_id,ventilator=addAirQuality.ventilator,totalnumberofpeople=addAirQuality.totalnumberofpeople,co2=addAirQuality.co2,co2measurementunit=addAirQuality.co2measurementunit,temperature=addAirQuality.temperature,temperaturemeasurementunit=addAirQuality.temperaturemeasurementunit,humidity=addAirQuality.humidity,humiditymeasurementunit=addAirQuality.humiditymeasurementunit,time=addAirQuality.time)
    try:
        db_Session.add(db_AQP)
        db_Session.flush()
        db_Session.commit()
    except Exception as ex:
        logger.error(f"{ex.__class__.__name__}: {ex}")
        db_Session.rollback()
    return addAirQuality

@app.get("/Room/AirQuality/", response_model=AirQuality_Properties_Object, status_code = status.HTTP_200_OK)
async def get_AirQuality_Rooms():
    
    AQPresults=db_Session.query(Airqualityproperty).all()
      
    return AQPresults         
  
@app.get("/Room/{room_id}/AirQuality/temperature/{timestamp}/", response_model=List[AirQuality_Temperature_Object], status_code = status.HTTP_200_OK)
async def get_AirQuality_Temperature(room_id:str,timestamp:datetime):
    AQPTemperature=db_Session.query(Airqualityproperty.room_id,Airqualityproperty.temperature,Airqualityproperty.temperaturemeasurementunit,Airqualityproperty.totalnumberofpeople,Airqualityproperty.ventilator,Airqualityproperty.time).filter(Airqualityproperty.room_id==room_id,Airqualityproperty.time==timestamp).all()
    return AQPTemperature

@app.get("/Room/{room_id}/AirQuality/humidity/{timestamp}", response_model=List[AirQuality_Humidity_Object], status_code = status.HTTP_200_OK)
async def get_AirQuality_Humidity(room_id:str,timestamp:datetime):
    AQPHumidity=db_Session.query(Airqualityproperty.room_id,Airqualityproperty.humidity,Airqualityproperty.humiditymeasurementunit,Airqualityproperty.totalnumberofpeople,Airqualityproperty.ventilator,Airqualityproperty.time).filter(Airqualityproperty.room_id==room_id,Airqualityproperty.time==timestamp).all()
    return AQPHumidity

@app.get("/Room/{room_id}/AirQuality/co2/{timestamp}/", response_model=List[AirQuality_Co2_Object], status_code = status.HTTP_200_OK)
async def get_AirQuality_Co2(room_id:str,timestamp:datetime):
    AQPCo2=db_Session.query(Airqualityproperty.room_id,Airqualityproperty.co2,Airqualityproperty.co2measurementunit,Airqualityproperty.totalnumberofpeople,Airqualityproperty.ventilator,Airqualityproperty.time).filter(Airqualityproperty.room_id==room_id,Airqualityproperty.time==timestamp).all()
    return AQPCo2    




if __name__ == "__main__":
 uvicorn.run("main:app",port=8000, reload=True)
 """ ngrok_tunnel = ngrok.connect(8000)
 print('Public URL:', ngrok_tunnel.public_url)
 nest_asyncio.apply()
 """