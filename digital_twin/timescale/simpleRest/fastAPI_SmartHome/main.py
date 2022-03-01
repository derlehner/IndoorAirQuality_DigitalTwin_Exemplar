from asyncio.log import logger
from datetime import datetime
import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from session import db_Session,conn 
from databases import Database 
from schema import Room,Airqualityproperty,Door,Light,Window,Ventilator
from fastAPI_models import  RoomTable,UpdateRoomTable,AirQualityPropertiesTable,AirQualityTemperatureTable,AirQualityHumidityTable,AirQualityCo2Table,Doors,Lights,LightOperation,Windows,WindowOperation,Ventilators,VentilatorOperation
from typing import List
database = Database(settings.DATABASE_URL)

app = FastAPI(title=settings.PROJECT_NAME)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
cur = conn.cursor()
                
# room
@app.post("/Rooms/",response_model=RoomTable, status_code = status.HTTP_201_CREATED)
async def add_Room(addRoom:RoomTable):
    db_classes = Room(room_id=addRoom.room_id,room_size=addRoom.room_size,measurement_unit=addRoom.measurement_unit)
    try:
        db_Session.add(db_classes)
        db_Session.flush()
        db_Session.commit()
    except Exception as ex:
        logger.error(f"{ex.__class__.__name__}: {ex}")
        db_Session.rollback()
   
    return addRoom
 
@app.get("/Rooms/", response_model=List[RoomTable], status_code = status.HTTP_200_OK)
async def get_AllRoom_Details():
    """ query = 'SELECT * FROM room'
    cur.execute(query)
    for i in cur:
        print(i) """
    results=db_Session.query(Room).all()
    return results         

@app.get("/Room/{room_id}/", response_model=List[RoomTable], status_code = status.HTTP_200_OK)
async def get_Specific_Room(room_id:str):
    specificRoomDetail=db_Session.query(Room).filter(Room.room_id==room_id).all()        
    return specificRoomDetail

@app.put("/Room/{room_id}",status_code = status.HTTP_200_OK)
async def update_RoomDetails(room_id:str,request:UpdateRoomTable):
    updateRoomDetail=db_Session.query(Room).filter(Room.room_id==room_id)
    if not updateRoomDetail.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Room with the id {room_id} is not available')
    updateRoomDetail.update({'room_size':request.room_size,'measurement_unit':request.measurement_unit})
    db_Session.commit()
    return {"code":"success","message":"updated room"}

@app.delete("/Room/{room_id}",response_model=RoomTable, status_code = status.HTTP_200_OK)
async def delete_RoomDetails(room_id:str):
    deleteRoomDetail=db_Session.delete(Room).where(Room.room_id==room_id).all()
    return deleteRoomDetail
    
# airQualityinRoom

@app.post("/Room/AirQuality/", response_model=AirQualityPropertiesTable, status_code = status.HTTP_201_CREATED)
async def add_AirQuality_Properties(addAirQuality:AirQualityPropertiesTable):
    db_AQP=Airqualityproperty(room_id=addAirQuality.room_id,ventilator=addAirQuality.ventilator,totalnumberofpeople=addAirQuality.totalnumberofpeople,co2=addAirQuality.co2,co2measurementunit=addAirQuality.co2measurementunit,temperature=addAirQuality.temperature,temperaturemeasurementunit=addAirQuality.temperaturemeasurementunit,humidity=addAirQuality.humidity,humiditymeasurementunit=addAirQuality.humiditymeasurementunit,time=addAirQuality.time)
    try:
        db_Session.add(db_AQP)
        db_Session.flush()
        db_Session.commit()
    except Exception as ex:
        logger.error(f"{ex.__class__.__name__}: {ex}")
        db_Session.rollback()
    return addAirQuality

@app.get("/Room/AirQuality/", response_model=AirQualityPropertiesTable, status_code = status.HTTP_200_OK)
async def get_AirQuality_Rooms():
    
    AQPresults=db_Session.query(Airqualityproperty).all()
      
    return AQPresults         
  
@app.get("/Room/{room_id}/AirQuality/temperature/{timestamp}/", response_model=List[AirQualityTemperatureTable], status_code = status.HTTP_200_OK)
async def get_AirQuality_Temperature(room_id:str,timestamp:datetime):
    AQPTemperature=db_Session.query(Airqualityproperty.room_id,Airqualityproperty.temperature,Airqualityproperty.temperaturemeasurementunit,Airqualityproperty.totalnumberofpeople,Airqualityproperty.ventilator,Airqualityproperty.time).filter(Airqualityproperty.room_id==room_id,Airqualityproperty.time==timestamp).all()
    return AQPTemperature

@app.get("/Room/{room_id}/AirQuality/humidity/{timestamp}", response_model=List[AirQualityHumidityTable], status_code = status.HTTP_200_OK)
async def get_AirQuality_Humidity(room_id:str,timestamp:datetime):
    AQPHumidity=db_Session.query(Airqualityproperty.room_id,Airqualityproperty.humidity,Airqualityproperty.humiditymeasurementunit,Airqualityproperty.totalnumberofpeople,Airqualityproperty.ventilator,Airqualityproperty.time).filter(Airqualityproperty.room_id==room_id,Airqualityproperty.time==timestamp).all()
    return AQPHumidity

@app.get("/Room/{room_id}/AirQuality/co2/{timestamp}/", response_model=List[AirQualityCo2Table], status_code = status.HTTP_200_OK)
async def get_AirQuality_Co2(room_id:str,timestamp:datetime):
    AQPCo2=db_Session.query(Airqualityproperty.room_id,Airqualityproperty.co2,Airqualityproperty.co2measurementunit,Airqualityproperty.totalnumberofpeople,Airqualityproperty.ventilator,Airqualityproperty.time).filter(Airqualityproperty.room_id==room_id,Airqualityproperty.time==timestamp).all()
    return AQPCo2    

@app.delete("/Room/AirQualityProperties/{room_id}/", response_model=AirQualityPropertiesTable, status_code = status.HTTP_200_OK)
async def delete_AirQuality_SpecificRoom(room_id:str):
    deleteAirQualityDetail=db_Session.delete(Airqualityproperty).where(Airqualityproperty.room_id==room_id)
    return deleteAirQualityDetail 

# lights
@app.post("/Room/Light/", response_model=Lights, status_code=status.HTTP_201_CREATED)
async def add_light(addLight: Lights):
    addLight=Light(room_id=addLight.room_id,light_id=addLight.light_id,turnon=addLight.turnon,energyconsumption=addLight.energyconsumption,energyconsumptionunit=addLight.energyconsumptionunit,time=addLight.time)
    try:
        db_Session.add(addLight)
        db_Session.flush()
        db_Session.commit()
    except Exception as ex:
        logger.error(f"{ex.__class__.__name__}: {ex}")
        db_Session.rollback()
    
    return addLight

@app.get("/Room/{room_id}/Light/", response_model=List[Lights], status_code=status.HTTP_200_OK)
async def get_All_Lights(room_id: str):
    getAllLights=db_Session.query(Light).filter(Light.room_id==room_id).all()
    return getAllLights

@app.get("/Room/{room_id}/Light/{light_id}/", response_model=List[Lights], status_code=status.HTTP_200_OK)
async def get_Specific_Light(room_id: str,light_id: str):
    getSpecificLight=db_Session.query(Light).filter(Light.room_id==room_id,Light.light_id==light_id).all()
    return getSpecificLight

@app.get("/Room{room_id}/Light{light_id}/isOn{timestamp}", response_model=Lights, status_code=status.HTTP_200_OK)
async def check_Light(room_id: str,light_id: str,time:datetime):
    checkLight=db_Session.query(Light).filter(Light.room_id==room_id,Light.light_id==light_id,Light.time==time)
    return checkLight   

""" @app.get("/Room{room_id}/Light{light_id}/energyConsumption", response_model=Lights, status_code=status.HTTP_200_OK)
async def get_SpecificLight(getSpecificLight: Lights):
    return getSpecificLight """      

@app.put("/Room/{room_id}/Light/{light_id}", status_code=status.HTTP_200_OK)
async def update_light(room_id: str,light_id:str,request: LightOperation):
    updateLight=db_Session.query(Light).filter(Light.room_id==room_id,Light.light_id==light_id)
    if not updateLight.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Light with the id {light_id} is not available')
    updateLight.update({'turnon':request.turnon,'time':request.time})
    db_Session.commit()
    return {"code":"success","message":"updated light settings"}
 
@app.delete("/Room{room_id}/Light{light_id}", response_model=Lights, status_code=status.HTTP_200_OK)
async def delete_light(room_id: str,light_id: str):
    deleteLight=db_Session.delete(Light).where(Light.room_id==room_id,Light.light_id==light_id)
    return deleteLight 

# windows
@app.post("/Room/Windows/", response_model=Windows, status_code=status.HTTP_201_CREATED)
async def create_Windows(addWindows: Windows):
    db_window=Window(room_id=addWindows.room_id,window_id=addWindows.window_id,isopen=addWindows.isopen,time=addWindows.time)
    try:
        db_Session.add(db_window)
        db_Session.flush()
        db_Session.commit()
    except Exception as ex:
        logger.error(f"{ex.__class__.__name__}: {ex}")
        db_Session.rollback()
    
    return addWindows

@app.get("/Room/{room_id}/Windows/", response_model=List[Windows], status_code=status.HTTP_200_OK)
async def get_All_Windows(room_id: str):
    get_AllWindow=db_Session.query(Window).filter(Window.room_id==room_id).all()
    return get_AllWindow    

@app.get("/Room/{room_id}/Windows/{window_id}/", response_model=List[Windows], status_code=status.HTTP_200_OK)
async def get_Specific_Window(room_id: str,window_id:str):
    get_SpecificWindow=db_Session.query(Window).filter(Window.room_id==room_id,Window.window_id==window_id).all()
    return get_SpecificWindow

""" 
@app.get("/Room/{room_id}/Windows/{window_id}/isOpen{timestamp}", response_model=Windows, status_code=status.HTTP_200_OK)
async def check_Specific_Window(room_id: str,window_id: str,time:datetime):
    check_Window=db_Session.query(Window).filter(Window.room_id==room_id,Window.window_id==window_id,Window.time==time)
    return check_Window
 """
@app.put("/Room/{room_id}/Windows/{window_id}", status_code=status.HTTP_200_OK)
async def update_window(room_id: str,window_id:str,request: WindowOperation):
    updateWindow=db_Session.query(Window).filter(Window.room_id==room_id,Window.window_id==window_id)
    if not updateWindow.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Window with the id {window_id} is not available')
    updateWindow.update({'isopen':request.isopen,'time':request.time})
    db_Session.commit()
    return {"code":"success","message":"updated window settings"}

@app.delete("Room{room_id}/Windows{window_id}", response_model=Windows, status_code=status.HTTP_200_OK)
async def delete_window(deleteWindow: Windows):
   return deleteWindow 


#ventilators
@app.post("/Room/Ventilators/", response_model=Ventilators, status_code=status.HTTP_201_CREATED)
async def create_Ventilators(addVentilators: Ventilators):
    db_ventilator = Ventilator(room_id=addVentilators.room_id,ventilator_id=addVentilators.ventilator_id,turnon=addVentilators.turnon,time=addVentilators.time)
    try:
        db_Session.add(db_ventilator)
        db_Session.flush()
        db_Session.commit()
    except Exception as ex:
        logger.error(f"{ex.__class__.__name__}: {ex}")
        db_Session.rollback()
    return addVentilators 

@app.get("/Room/{room_id}/Ventilators/", response_model=List[Ventilators], status_code=status.HTTP_200_OK)
async def get_All_Ventilators(room_id:str):
    getVentilators=db_Session.query(Ventilator).filter(Ventilator.room_id==room_id).all()
    return getVentilators

@app.get("/Room/{room_id}/Ventilators/{ventilator_id}/", response_model=List[Ventilators], status_code=status.HTTP_200_OK)
async def get_Specific_Ventilator(room_id:str,ventilator_id:str):
    getSpecificVentilators=db_Session.query(Ventilator).filter(Ventilator.room_id==room_id,Ventilator.ventilator_id==ventilator_id).all()
    return getSpecificVentilators

""" @app.get("/Room/{room_id}/Ventilators/{ventilator_id}/isOn{timestamp}", response_model=Ventilators, status_code=status.HTTP_200_OK)
async def check_Ventilators(room_id:str,ventilator_id:str,timestamp:datetime):
    checkVentilators=db_Session.query(Ventilator).filter(Ventilator.room_id==room_id,Ventilator.ventilator_id==ventilator_id,Ventilator.time==timestamp).all()
    return checkVentilators
     """

@app.put("/Room/{room_id}/Ventilators/{ventilator_id}", status_code=status.HTTP_200_OK)
async def update_ventilators(room_id:str,ventilator_id:str,request: VentilatorOperation):
    updateVentilator=db_Session.query(Ventilator).filter(Ventilator.room_id==room_id,Ventilator.ventilator_id==ventilator_id)
    if not updateVentilator.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Ventilator with the id {ventilator_id} is not available')
    updateVentilator.update({'turnon':request.turnon,'time':request.time})
    db_Session.commit()
    return {"code":"success","message":"updated ventilator settings"}

@app.delete("/Room/{room_id}/Ventilators/{ventilator_id}", response_model=Ventilators, status_code=status.HTTP_200_OK)
async def delete_ventilators(room_id: str,ventilator_id:str):
    deleteVentilator=db_Session.delete(Ventilator).where(Ventilator.room_id==room_id,Ventilator.ventilator_id==ventilator_id)
    return deleteVentilator 

# doors
@app.post("/Room/Doors/", response_model=Doors, status_code=status.HTTP_201_CREATED)
async def add_Doors(addDoors: Doors):
    db_doors = Door(room_id=addDoors.room_id,door_id=addDoors.door_id,door_lock=addDoors.door_lock,connectsdoor=addDoors.connectsdoor,connecteddoors=addDoors.connecteddoors,time=addDoors.time)
    db_Session.add(db_doors)
    db_Session.flush()
    db_Session.commit()
    return addDoors

@app.get("/Room/Doors/", response_model=List[Doors], status_code=status.HTTP_200_OK)
async def get_AllDoors():
    getDoors=db_Session.query(Door).all()
    return getDoors

@app.get("/Room{room_id}/Doors{door_id}/isOpen{timestamp}", response_model=Doors, status_code=status.HTTP_201_CREATED)
async def get_SpecificDoor(getSpecificDoor: Doors):
   
    return getSpecificDoor

@app.put("/Room{room_id}/Doors{door_id}", response_model=Doors, status_code=status.HTTP_201_CREATED)
async def update_door(updateDoor: Doors):
   
    return updateDoor

@app.delete("/Room{room_id}/Doors{door_id}", response_model=Doors, status_code=status.HTTP_201_CREATED)
async def delete_door(deleteDoor: Doors):
   #TO DO
    return deleteDoor


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)