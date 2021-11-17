from datetime import datetime
from config import db, ma


class Sensordata(db.Model):
    __tablename__ = 'sensordata'
    id = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True,)
    sensorname = db.Column(db.String(32))
    roomnumber = db.Column(db.String(32))
    time = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    co2 = db.Column(db.Float)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)


class SensorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sensordata
        load_instance = True
