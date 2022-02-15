import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from schema import room,airQualityProperties,lights,doors,windows,ventilators
app = FastAPI(title="CDL-MINT Home Automation")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# room
@app.post("/addRooms/", response_model=room, status_code = status.HTTP_200_OK)
async def add_Room(addRoom:room):
    return addRoom
@app.get("/getAllRooms/", response_model=room, status_code = status.HTTP_200_OK)
async def get_AllRoomDetails(allRoomDetails:room):
    return allRoomDetails
@app.get("/getSpecificRoom/{room_id}/", response_model=room, status_code = status.HTTP_200_OK)
async def get_SpecificRoom(specificRoomDetail:room):
    return specificRoomDetail
@app.put("/updateRoom/{room_id}",response_model=room, status_code = status.HTTP_200_OK)
async def update_RoomDetails(updateRoom:room):
    return updateRoom
@app.delete("/deleteRoom/{room_id}",response_model=room, status_code = status.HTTP_200_OK)
async def delete_RoomDetails(deleteRoom:room):
    return deleteRoom    

# airQualityinRoom

@app.post("/addAirQualityProperties/", response_model=airQualityProperties, status_code = status.HTTP_200_OK)
async def add_AirQuality_Rooms(addAirQualityRoom:airQualityProperties):
    return addAirQualityRoom
@app.get("/getAirQualityProperties/", response_model=airQualityProperties, status_code = status.HTTP_200_OK)
async def get_AirQuality_Rooms(airQualityinAllRooms:airQualityProperties):
    return airQualityinAllRooms
@app.get("/getSpecificAirQualityProperties/{room_id}/", response_model=airQualityProperties, status_code = status.HTTP_200_OK)
async def get_AirQuality_SpecificRoom(airQualityinSpecificRoom:airQualityProperties):
    return airQualityinSpecificRoom
@app.put("/updateAirQualityProperties/{room_id}/", response_model=airQualityProperties, status_code = status.HTTP_200_OK)
async def update_AirQuality_SpecificRoom(updateAirQualityRoom:airQualityProperties):
    return updateAirQualityRoom
@app.delete("/deleteAirQualityProperties/{room_id}/", response_model=airQualityProperties, status_code = status.HTTP_200_OK)
async def delete_AirQuality_SpecificRoom(deleteAirQualityRoom:airQualityProperties):
    return deleteAirQualityRoom

# lights
@app.post("/addLight/", response_model=lights, status_code=status.HTTP_201_CREATED)
async def add_light(addLight: lights):
    return addLight
@app.get("/getAllLights/", response_model=lights, status_code=status.HTTP_201_CREATED)
async def get_AllLights(getAllLights: lights):
    return getAllLights
@app.get("/getSpecificLight/{room_id}/{light_id}", response_model=lights, status_code=status.HTTP_201_CREATED)
async def get_SpecificLight(getSpecificLight: lights):
    return getSpecificLight
@app.put("/updateRoomLight/{room_id}/{light_id}", response_model=lights, status_code=status.HTTP_201_CREATED)
async def update_light(updateLight: lights):
    return updateLight
@app.delete("/deleteRoomLight/{room_id}/{light_id}", response_model=lights, status_code=status.HTTP_201_CREATED)
async def delete_light(deleteLight: lights):
    return deleteLight

# doors
@app.post("/addDoors/", response_model=doors, status_code=status.HTTP_201_CREATED)
async def add_Doors(addDoors: doors):
   
    return addDoors
@app.get("/getAllDoors/", response_model=doors, status_code=status.HTTP_201_CREATED)
async def get_AllDoors(getAllDoors: doors):
   
    return getAllDoors
@app.get("/getSpecificDoor/{room_id}/{door_id}", response_model=doors, status_code=status.HTTP_201_CREATED)
async def get_SpecificDoor(getSpecificDoor: doors):
   
    return getSpecificDoor
@app.put("/updateDoor/{room_id}/{door_id}", response_model=doors, status_code=status.HTTP_201_CREATED)
async def update_door(updateDoor: doors):
   
    return updateDoor
@app.post("/deleteDoor/{room_id}/{door_id}", response_model=doors, status_code=status.HTTP_201_CREATED)
async def delete_door(deleteDoor: doors):
   
    return deleteDoor


# windows
@app.post("/addWindows/", response_model=windows, status_code=status.HTTP_201_CREATED)
async def create_windows(addWindows: windows):
   
    return addWindows
@app.get("/allWindows/", response_model=windows, status_code=status.HTTP_201_CREATED)
async def get_AllWindows(getAllwindows: windows):
   
    return getAllwindows
@app.get("/specificWindow/{room_id}/{window_id}", response_model=windows, status_code=status.HTTP_201_CREATED)
async def get_SpecificWindow(getSpecificWindow: windows):
   
    return getSpecificWindow
@app.put("/updateWindows/{room_id}/{window_id}", response_model=windows, status_code=status.HTTP_201_CREATED)
async def update_window(updateWindow: windows):
   
    return updateWindow
@app.delete("/deleteWindows/{room_id}/{window_id}", response_model=windows, status_code=status.HTTP_201_CREATED)
async def delete_window(deleteWindow: windows):
   
    return deleteWindow

#ventilators
@app.post("/addVentilators/", response_model=ventilators, status_code=status.HTTP_201_CREATED)
async def create_ventilators(addVentilators: ventilators):
   
    return addVentilators
@app.get("/getAllVentilators/", response_model=ventilators, status_code=status.HTTP_201_CREATED)
async def get_ventilators(getAllVentilators: ventilators):
   
    return getAllVentilators
@app.get("/get_Specific_ventilators/{room_id}", response_model=ventilators, status_code=status.HTTP_201_CREATED)
async def create_ventilators(getSpecificVentilator: ventilators):
   
    return getSpecificVentilator
@app.put("/update_ventilators/{room_id}", response_model=ventilators, status_code=status.HTTP_201_CREATED)
async def get_ventilators(updateVentilator: ventilators):
   
    return updateVentilator
@app.delete("/delete_Ventilators/{room_id}", response_model=ventilators, status_code=status.HTTP_201_CREATED)
async def create_ventilators(deleteVentilator: ventilators):
   
    return deleteVentilator
  
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)