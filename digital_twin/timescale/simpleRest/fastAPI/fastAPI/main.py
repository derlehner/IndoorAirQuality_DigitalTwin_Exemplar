from typing import List
import databases
#import sqlalchemy
from sqlalchemy import *
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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
metadata = MetaData()

Types = Table(
    "Types",
    metadata,
    Column("name", String(32),unique=True,
                 nullable=False,  primary_key=True),
    Column("container", String(32), nullable=False, primary_key=True),
    UniqueConstraint('name', 'container')
    
)
Instances = Table(
    "Instances",
    metadata,
    Column("name", String(32),
                 nullable=False,  primary_key=True),
    Column("container", String(32), nullable=False, primary_key=True),
    Column("typename", String(32), nullable=False),
    Column("typecontainer", String(32), nullable=False),
    UniqueConstraint('name', 'container'),
    ForeignKeyConstraint(['typename', 'typecontainer'],
                                ['Types.name', 'Types.container'])
    
)
ActualSensorData = Table(
    "ActualSensorData",                                       
    metadata,
    Column("container", String(32),
                 nullable=False),
    Column("instance", String(32), nullable=False),
    Column("property", String(32), nullable=False, primary_key=True),
    Column("time", DateTime(), default=datetime.utcnow,
                     onupdate=datetime.utcnow, primary_key=True),
    Column("value", String(32), nullable=False),
  
    UniqueConstraint('property', 'time'),
    ForeignKeyConstraint(['container', 'instance'],
                                ['Instances.container', 'Instances.name'])
    
)

engine = create_engine(
    DATABASE_URL, pool_size=3, max_overflow=0
)
metadata.create_all(engine)

class TypesRequest(BaseModel):
    name: str
    container: str

class TypesResponse(BaseModel):
   
    name: str
    container: str

class InstancesRequest(BaseModel):
    name: str
    container: str
    typename: str
    typecontainer: str

class InstancesResponse(BaseModel):
    name: str
    container: str
    typename:  str
    typecontainer: str 

class ActualSensorDataRequest(BaseModel):
    container : str
    instance : str
    property : str
    #time: str
    value: str

class ActualSensorDataResponse(BaseModel):
    container : str
    instance : str
    property : str
    #time: str
    value:str 


app = FastAPI(title = "REST API using FastAPI PostgreSQL Async EndPoints")
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

@app.get("/Types/{container}/", response_model=TypesResponse, status_code = status.HTTP_200_OK)
async def read_types(container: str):
    query = Types.select().where(Types.c.container == container)
   
    return await database.fetch_all(query)

@app.post("/Types/", response_model=TypesResponse, status_code = status.HTTP_201_CREATED)
async def create_Types(TypesBody: TypesRequest):
     query = Types.insert().values(name=TypesBody.name, container=TypesBody.container)
     last_record_id =await database.execute(query)
     return {**TypesBody.dict()}
""" 
@app.put("/Types/{container}/", response_model=TypesResponse, status_code = status.HTTP_200_OK)
async def update_Types(container: str, payload: TypesRequest):
    query = Types.update().where(Types.c.container == container).values(name=payload.name, container=payload.container)
    await database.execute(query)
    return {**payload.dict(), "container": container}

@app.delete("/Types/{container}/", status_code = status.HTTP_200_OK)
async def delete_Types(container: str):
    query = Types.delete().where(Types.c.container == container)
    await database.execute(query)
    return {"message": "Types with container: {} deleted successfully!".format(container)}
 """
@app.get("/Instances/", response_model=List[InstancesResponse], status_code = status.HTTP_200_OK)
async def read_Instances(skip: int = 0, take: int = 20):
    query = Instances.select().offset(skip).limit(take)
    return await database.fetch_all(query)

@app.get("/Instances/{container}/", response_model=InstancesResponse, status_code = status.HTTP_200_OK)
async def read_Instances(container: str):
    query = Instances.select().where(Instances.c.container == container)
   
    return await database.fetch_one(query)

@app.post("/Instances/", response_model=InstancesResponse, status_code = status.HTTP_201_CREATED)
async def create_Instances(InstancesBody: InstancesRequest):
     query = Instances.insert().values(name=InstancesBody.name, container=InstancesBody.container,typename=InstancesBody.typename,typecontainer=InstancesBody.typecontainer)
     last_record_id =await database.execute(query)
     return {**InstancesBody.dict()}

@app.get("/ActualSensorData/", response_model=List[ActualSensorDataResponse], status_code = status.HTTP_200_OK)
async def read_Instances(skip: int = 0, take: int = 20):
    query = ActualSensorData.select().offset(skip).limit(take)
    return await database.fetch_all(query)

@app.get("/ActualSensorData/{container}/", response_model=ActualSensorDataResponse, status_code = status.HTTP_200_OK)
async def read_Instances(container: str):
    query = ActualSensorData.select().where(ActualSensorData.c.container == container)
   
    return await database.fetch_one(query)

@app.post("/ActualSensorData/", response_model=ActualSensorDataResponse, status_code = status.HTTP_201_CREATED)
async def create_Instances(ActualSensorDataBody: ActualSensorDataRequest):
     #query = ActualSensorData.insert().values(container=ActualSensorDataBody.container, instance=ActualSensorDataBody.instance, property=ActualSensorDataBody.property,time=ActualSensorDataBody.time, value=ActualSensorDataBody.value)
     query = ActualSensorData.insert().values(container=ActualSensorDataBody.container, instance=ActualSensorDataBody.instance, property=ActualSensorDataBody.property, value=ActualSensorDataBody.value)
     last_record_id =await database.execute(query)
     return {**ActualSensorDataBody.dict()}     