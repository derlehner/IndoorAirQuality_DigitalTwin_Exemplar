import os
from config import db
from models import Sensordata

# Data to initialize database with
SENSORDATA = [
    {
        "id": 1919,
        "sensorname": "scd30",
        "roomnumber": "s30076",
        "co2": 547.96,
        "temperature": 27.02,
        "humidity": 44.41
    },
     {
        "id": 1920,
        "sensorname": "scd30",
        "roomnumber": "s30076",
        "co2": 548.13,
        "temperature": 27.0,
        "humidity": 44.44
    },
    {
        "id": 1921,
        "sensorname": "scd30",
        "roomnumber": "s30076",
        "co2": 548.77,
        "temperature": 27.0,
        "humidity": 44.5
    },
]

# Delete database file if it exists currently
if os.path.exists('sensordata.db'):
    os.remove('sensordata.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for sensor in SENSORDATA:
    p = Sensordata(id=sensor['id'],sensorname=sensor['sensorname'],roomnumber=sensor['roomnumber'],
                   co2=sensor['co2'],temperature=sensor['temperature'], humidity=sensor['humidity'])
    db.session.add(p)

db.session.commit()
