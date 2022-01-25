import uvicorn
from fastapi import FastAPI, status
from config import settings
from session import engine   
# from dotenv import load_dotenv
from schema import Classes as SchemaClasses
from schema import Objects as SchemaObjects
from schema import Slots as SchemaSlots
from schema import DataPoints as SchemaDataPoints
from schema import ObjectsToClassRelations as SchemaObjectToClassRelations
# from models import Classes as ModelClasses
# from models import Objects as ModelObjects
# from models import Classes
# from models import Objects
# from fastapi_sqlalchemy import db, DBSessionMiddleware


app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)




@app.post("/AddClasses/", response_model=SchemaClasses, status_code=status.HTTP_201_CREATED)
async def create_Classes(ClassesBody: SchemaClasses):
   # db_classes = ModelClasses(name=ClassesBody.name)
   # db.session.add(db_classes)
   # db.session.commit()
    return ClassesBody

@app.post("/AddObjects/", response_model=SchemaObjects, status_code=status.HTTP_201_CREATED)
async def create_Objects(ObjectsBody: SchemaObjects):
    # db_objects = ModelObjects(name=ObjectsBody.name)
    # db.session.add(db_objects)
    # db.session.commit()
    return ObjectsBody

@app.post("/AddSchemaObjectToClassRelations/", response_model=SchemaObjectToClassRelations, status_code=status.HTTP_201_CREATED)
async def create_SchemaObjectToClassRelations(SchemaObjectToClassRelationsBody: SchemaObjectToClassRelations):
    # db_objects = ModelObjects(name=ObjectsBody.name)
    # db.session.add(db_objects)
    # db.session.commit()
    return SchemaObjectToClassRelationsBody

@app.post("/AddSlots/", response_model=SchemaSlots, status_code=status.HTTP_201_CREATED)
async def create_Slots(SlotsBody: SchemaSlots):
    # db_objects = ModelObjects(name=ObjectsBody.name)
    # db.session.add(db_objects)
    # db.session.commit()
    return SlotsBody

@app.post("/AddDataPoints/", response_model=SchemaDataPoints, status_code=status.HTTP_201_CREATED)
async def create_Slots(DataPointsBody: SchemaDataPoints):
    # db_objects = ModelObjects(name=ObjectsBody.name)
    # db.session.add(db_objects)
    # db.session.commit()
    return DataPointsBody

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)