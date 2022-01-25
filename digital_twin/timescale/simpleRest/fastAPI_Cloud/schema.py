from sqlite3 import Timestamp
from pydantic import BaseModel
from datetime import datetime


class Classes(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Objects(BaseModel):
    name: str

    class Config:
        orm_mode = True

class ObjectsToClassRelations(BaseModel):
    object_name: str
    class_name: str
    valid_from: Timestamp
    valid_to: Timestamp

class Slots(BaseModel):
    name: str
    className: str

    class Config:
        orm_mode = True


class DataPoints(BaseModel):
    type: str
    object: str
    value: str
    timestamp: datetime

    class Config:
        orm_mode = True