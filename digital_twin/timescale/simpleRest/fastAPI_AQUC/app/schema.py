# coding: utf-8

from sqlalchemy import Column,Float, String,Integer,DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Room(Base):
    __tablename__ = 'room'

    room_id = Column(String, primary_key=True)
    room_size = Column(Integer, nullable=False)
    measurement_unit = Column(String, nullable=False)


class Airqualityproperty(Base):
    __tablename__ = 'airqualityproperties'

    room_id = Column(ForeignKey('room.room_id'), nullable=False)
    ventilator = Column(String, nullable=False)
    totalnumberofpeople = Column(Integer, nullable=False)
    co2 = Column(Float(53), nullable=False)
    co2measurementunit = Column(String, nullable=False)
    temperature = Column(Float(53), nullable=False)
    temperaturemeasurementunit = Column(String, nullable=False)
    humidity = Column(Float(53), nullable=False)
    humiditymeasurementunit = Column(String, nullable=False)
    time = Column(DateTime, primary_key=True)

    room = relationship('Room')
