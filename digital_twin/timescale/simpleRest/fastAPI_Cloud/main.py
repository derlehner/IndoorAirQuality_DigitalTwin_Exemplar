import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from session import db_Session 
import databases

# import the schema 
from schema import Classes as SchemaClasses
from schema import Objects as SchemaObjects
from schema import Slots as SchemaSlots
from schema import DataPoints as SchemaDataPoints
from schema import ObjectsToClassRelations as SchemaObjectToClassRelations
#import db models
from models import Class as ModelClass
from models import Object as ModelObjects
from models import Objectstoclassrelation as Object_Class_Relation
from models import Slot as ModelSlot
from models import Datapoint as ModelDataPoint


database = databases.Database(settings.DATABASE_URL)

app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

""" @app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect() """

@app.post("/AddClasses/", response_model=SchemaClasses, status_code=status.HTTP_201_CREATED)
async def create_Classes(classesBody: SchemaClasses):
    db_classes = ModelClass(name=classesBody.name)
    db_Session.add(db_classes)
    db_Session.commit()
    return classesBody

@app.post("/AddObjects/", response_model=SchemaObjects, status_code=status.HTTP_201_CREATED)
async def create_Objects(objectsBody: SchemaObjects):
    db_objects = ModelObjects(name=objectsBody.name)
    db_Session.add(db_objects)
    db_Session.commit()
    return objectsBody

@app.post("/AddSchemaObjectToClassRelations/", response_model=SchemaObjectToClassRelations, status_code=status.HTTP_201_CREATED)
async def create_SchemaObjectToClassRelations(schemaObjectToClassRelationsBody: SchemaObjectToClassRelations):
    db_objects_class = Object_Class_Relation(object=schemaObjectToClassRelationsBody.object_name,_class=schemaObjectToClassRelationsBody.class_name,valid_from=schemaObjectToClassRelationsBody.valid_from,valid_to=schemaObjectToClassRelationsBody.valid_to)
    db_Session.add(db_objects_class)
    db_Session.commit()
    return schemaObjectToClassRelationsBody

@app.post("/AddSlots/", response_model=SchemaSlots, status_code=status.HTTP_201_CREATED)
async def create_Slots(slotsBody: SchemaSlots):
    db_slots = ModelSlot(name=slotsBody.name,_class=slotsBody.className)
    db_Session.add(db_slots)
    db_Session.commit()
    return slotsBody

@app.post("/AddDataPoints/", response_model=SchemaDataPoints, status_code=status.HTTP_201_CREATED)
async def create_Slots(DataPointsBody: SchemaDataPoints):
    db_data_points = ModelDataPoint(type=DataPointsBody.type,object=DataPointsBody.object,value=DataPointsBody.value,timestamp=DataPointsBody.timestamp)
    db_Session.add(db_data_points)
    db_Session.commit()
    return DataPointsBody

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)