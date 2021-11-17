import os
from config import db
# from models import Sensordata

from models import Types,  Instances, ActualSensorData, Relationships, Links, Property
# Data to initialize database with

TYPES = [
    {
        "name": "Room",
        "container": "null",

    },
    {
        "name": "Controller",
        "container": "null",
    },
    {
        "name": "Sensor",
        "container": "Controller",
    },
    {
        "name": "LED",
        "container": "Controller",
    },
]

INSTANCES = [
    {

        "name": "SCD-30",
        "container": "Raspi_01",
        "type_name": "Sensor",
        "type_container": "Controller"

    },
    {

        "name": "SCD-30",
        "container": "Raspi_02",
        "type_name": "Sensor",
        "type_container": "Controller"

    },
    {

        "name": "SCD-30",
        "container": "Arduino_01",
        "type_name": "Sensor",
        "type_container": "Controller"

    },
    {

        "name": "Raspi_01",
        "container": "S3_0076",
        "type_name": "Controller",
        "type_container": "null"

    },
    {

        "name": "Raspi_02",
        "container": "S3_0086",
        "type_name": "Controller",
        "type_container": "null"

    },
    {

        "name": "Arduino_01",
        "container": "S3_0080",
        "type_name": "Controller",
        "type_container": "null"

    },
    {

        "name": "S3_0076",
        "container": "null",
        "type_name": "Room",
        "type_container": "null"

    },
    {

        "name": "S3_0086",
        "container": "null",
        "type_name": "Room",
        "type_container": "null"

    },
    {

        "name": "S3_0080",
        "container": "null",
        "type_name": "Room",
        "type_container": "null"

    },
]
ACTUALSENSORDATA = [
    {

        "container": "Raspi_01",
        "instance": "SCD-30",
        "property": "co2",
        "value": "550.41"
    },
    {

        "container": "Raspi_01",
        "instance": "SCD-30",
        "property": "temperature",
        "value": "14.0"
    },
    {

        "container": "Raspi_01",
        "instance": "SCD-30",
        "property": "humidity",
        "value": "60.5"
    },
    {

        "container": "Raspi_01",
        "instance": "SCD-30",
        "property": "LED_Activated",
        "value": "False"
    },
]
RELATIONSHIPS = [
    {
        "relation_Id": 1,
        "source_name": "Room",
        "source_container": "null",
        "target_name": "Controller",
        "target_container": "null",
        "connection_Type": "Relation"
    },
    {
        "relation_Id": 2,
        "source_name": "Controller",
        "source_container": "null",
        "target_name": "Sensor",
        "target_container": "Controller",
        "connection_Type": "Composition"
    },
    {
        "relation_Id": 3,
        "source_name": "Controller",
        "source_container": "null",
        "target_name": "LED",
        "target_container": "Controller",
        "connection_Type": "Composition"
    },
]
LINKS = [
    {
        "link_Id": 1,
        "source_name": "S3_0076",
        "source_container": "null",
        "target_name": "Raspi_01",
        "target_container": "S3_0076",
        "relation_Id": 1
    },
    {
        "link_Id": 2,
        "source_name": "S3_0086",
        "source_container": "null",
        "target_name": "Raspi_02",
        "target_container": "S3_0086",
        "relation_Id": 1
    },
    {
        "link_Id": 3,
        "source_name": "S3_0080",
        "source_container": "null",
        "target_name": "Arduino_01",
        "target_container": "S3_0080",
        "relation_Id": 1
    },
]
PROPERTY = [
    {
        "property_Id": 1,
        "name": "co2",
        "type_name": "Sensor",
        "type_container": "Controller",
        "data_Type": "float",

    },
    {
        "property_Id": 2,
        "name": "temperature",
        "type_name": "Sensor",
        "type_container": "Controller",
        "data_Type": "float",

    },
    {
        "property_Id": 3,
        "name": "humidity",
        "type_name": "Sensor",
        "type_container": "Controller",
        "data_Type": "float",

    },
    {
        "property_Id": 4,
        "name": "LED_Activated",
        "type_name": "LED",
        "type_container": "Controller",
        "data_Type": "bool",

    },
]

# Delete database file if it exists currently
if os.path.exists('actualsensordata.db'):
    os.remove('actualsensordata.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database

for types in TYPES:
    t = Types(name=types['name'], container=types['container'])

for instance in INSTANCES:
    i = Instances(
        name=instance['name'], container=instance['container'], type_name=instance['type_name'], type_container=instance['type_container'])

for actualsensordata in ACTUALSENSORDATA:
    s = ActualSensorData(container=actualsensordata['container'], instance=actualsensordata['instance'],
                         property=actualsensordata['property'], value=actualsensordata['value'])

for relation in RELATIONSHIPS:
    r = Relationships(relation_Id=relation['relation_Id'], source_name=relation['source_name'], source_container=relation['source_container'],
                      target_name=relation['target_name'], target_container=relation['target_container'], connection_Type=relation['connection_Type'])
for link in LINKS:
    l = Links(link_Id=link['link_Id'], source_name=link['source_name'], source_container=link['source_container'],
              target_name=link['target_name'], target_container=link['target_container'],  relation_Id=link['relation_Id'])

for properties in PROPERTY:
    p = Property(property_Id=properties['property_Id'], name=properties['name'], type_name=properties['type_name'], type_container=properties['type_container'],
                 data_Type=properties['data_Type'])

db.session.add(t)
db.session.add(i)
db.session.add(s)
db.session.add(r)
db.session.add(l)
db.session.add(p)

db.session.commit()
