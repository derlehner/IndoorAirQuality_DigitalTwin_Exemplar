# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Class(Base):
    __tablename__ = 'classes'

    name = Column(Text, primary_key=True)


class Object(Base):
    __tablename__ = 'objects'

    name = Column(Text, primary_key=True)


class Objectstoclassrelation(Base):
    __tablename__ = 'objectstoclassrelations'

    object = Column(ForeignKey('objects.name'), primary_key=True, nullable=False)
    _class = Column('class', ForeignKey('classes.name'), primary_key=True, nullable=False)
    valid_from = Column(DateTime, primary_key=True, nullable=False)
    valid_to = Column(DateTime, primary_key=True, nullable=False)

    _class1 = relationship('Class')
    object1 = relationship('Object')


class Slot(Base):
    __tablename__ = 'slots'

    name = Column(Text, primary_key=True)
    _class = Column('class', ForeignKey('classes.name'))

    _class1 = relationship('Class')


class Datapoint(Base):
    __tablename__ = 'datapoints'

    type = Column(ForeignKey('slots.name'), primary_key=True, nullable=False)
    object = Column(ForeignKey('objects.name'), primary_key=True, nullable=False)
    value = Column(Text)
    timestamp = Column(DateTime, primary_key=True, nullable=False)

    object1 = relationship('Object')
    slot = relationship('Slot')
