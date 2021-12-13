
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKeyConstraint, UniqueConstraint
from datetime import datetime

from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

class Types(Base):
    __tablename__ = "Types"

   
    name=Column(String(32),unique=True,
                 nullable=False,  primary_key=True)
    
    UniqueConstraint('name')
    
class Instances(Base):
    __tablename__ = "Instances"
 
    name=Column(String(32),
                 nullable=False,  primary_key=True)
    typename=Column(String(32), nullable=False)
  
    UniqueConstraint('name'),
    ForeignKeyConstraint(['typename'],
                                ['Types.name'])

class Properties(Base):
    __tablename__ = "Properties"
 
    name=Column(String(32),
                 nullable=False,  primary_key=True) # does the primary_key attribute work for combined keys?
    type=Column(String(32),
                 nullable=False,  primary_key=True)
    UniqueConstraint('name'),
    ForeignKeyConstraint(['type'],
                                ['Types.name'])

class Values(Base):
    __tablename__ = "Values"
 

    propertyname=Column(String(32),
                 nullable=False,  primary_key=True) # does the primary_key attribute work for combined keys?
    instancename=Column(String(32), nullable=False,  primary_key=True) # i changed this from type to instance
    value=Column(String(32), nullable=False)
    time=Column(DateTime, default=datetime.utcnow,
                     onupdate=datetime.utcnow, primary_key=True)
    UniqueConstraint('propertyname', 'instancename'),
    ForeignKeyConstraint(['propertyname','instancename'],
                                ['Properties.name','Instances.name'])

