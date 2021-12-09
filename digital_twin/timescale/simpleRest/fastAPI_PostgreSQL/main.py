from typing import List
import databases
import sqlalchemy
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from schema import TypesRequest,TypesResponse,PropertiesRequest,PropertiesResponse,InstancesRequest,InstancesResponse,ValuesRequest,ValuesResponse
from datetime import datetime
import os
import urllib

host_server = os.environ.get('host_server', 'localhost')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
database_name = os.environ.get('database_name', 'cdl-mint')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'postgres')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'cdlmint')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)
database = databases.Database(DATABASE_URL)


app = FastAPI(title = "CDL-MINT REST_APIs for connecting to Postgresql")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/Types/", response_model=List[TypesResponse], status_code = status.HTTP_200_OK)
async def read_types(skip: int = 0, take: int = 20):
    query = Types.select().offset(skip).limit(take)
    return await database.fetch_all(query)

@app.get("/Types/{name}/", response_model=TypesResponse, status_code = status.HTTP_200_OK)
async def read_types(name: str):
    query = Types.select().where(Types.c.name == name)
   
    return await database.fetch_all(query)

@app.post("/Types/", response_model=TypesResponse, status_code = status.HTTP_201_CREATED)
async def create_Types(TypesBody: TypesRequest):
     query = Types.insert().values(name=TypesBody.name)
     last_record_id =await database.execute(query)
     return {**TypesBody.dict()}

@app.get("/Properties/", response_model=List[PropertiesResponse], status_code = status.HTTP_200_OK)
async def read_types(skip: int = 0, take: int = 20):
    query = Properties.select().offset(skip).limit(take)
    return await database.fetch_all(query)

@app.get("/Properties/{name}/", response_model=PropertiesResponse, status_code = status.HTTP_200_OK)
async def read_types(name: str):
    query = Properties.select().where(Properties.c.name == name)
   
    return await database.fetch_all(query)

@app.post("/Properties/", response_model=PropertiesResponse, status_code = status.HTTP_201_CREATED)
async def create_Types(PropertiesBody: PropertiesRequest):
     query = Properties.insert().values(name=PropertiesBody.name)
     last_record_id =await database.execute(query)
     return {**PropertiesBody.dict()}

@app.get("/Instances/", response_model=List[InstancesResponse], status_code = status.HTTP_200_OK)
async def read_Instances(skip: int = 0, take: int = 20):
    query = Instances.select().offset(skip).limit(take)
    return await database.fetch_all(query)

@app.get("/Instances/{typename}/", response_model=InstancesResponse, status_code = status.HTTP_200_OK)
async def read_Instances(typename: str):
    query = Instances.select().where(Instances.c.typename == typename)
   
    return await database.fetch_one(query)

@app.post("/Instances/", response_model=InstancesResponse, status_code = status.HTTP_201_CREATED)
async def create_Instances(InstancesBody: InstancesRequest):
     query = Instances.insert().values(name=InstancesBody.name, typename=InstancesBody.typename)
     last_record_id =await database.execute(query)
     return {**InstancesBody.dict()}

@app.get("/Values/", response_model=List[ValuesResponse], status_code = status.HTTP_200_OK)
async def read_Values(skip: int = 0, take: int = 20):
    query = Values.select().offset(skip).limit(take)
    return await database.fetch_all(query)

@app.get("/Values/{instancename}/", response_model=ValuesResponse, status_code = status.HTTP_200_OK)
async def read_Values(instancename: str):
    query = Values.select().where(Values.c.instancename == instancename)
   
    return await database.fetch_one(query)

@app.post("/Values/", response_model=ValuesResponse, status_code = status.HTTP_201_CREATED)
async def create_Values(ValuesBody: ValuesRequest):
     query = Values.insert().values(propertyname=ValuesBody.propertyname, instancename=ValuesBody.instancename, value=ValuesBody.value, time=ValuesBody.time)
     last_record_id =await database.execute(query)
     return {**ValuesBody.dict()}        


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)   