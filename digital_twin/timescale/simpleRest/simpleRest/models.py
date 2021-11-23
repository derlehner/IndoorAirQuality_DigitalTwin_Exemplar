from datetime import datetime
from config import db, ma


""" class Sensordata(db.Model):
    __tablename__ = 'sensordata'
    id = db.Column(db.BigInteger, primary_key=True)
    sensorname = db.Column(db.String(32))
    deviceid = db.Column(db.String(32))
    time = db.Column(db.DateTime, default=datetime.utcnow,
                     onupdate=datetime.utcnow)
    co2 = db.Column(db.Float)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
     """


class Types(db.Model):
    __tablename__ = 'types'

    name = db.Column(db.String(32), unique=True,
                     nullable=False, primary_key=True)
    container = db.Column(db.String(32), nullable=False, primary_key=True)

    __table_args__ = (
        db.UniqueConstraint('name', 'container'),
    )


class Instances(db.Model):
    __tablename__ = 'instances'

    name = db.Column(db.String(32), unique=True,
                     nullable=False, primary_key=True)
    container = db.Column(db.String(32),
                          nullable=False, primary_key=True)
    type_name = db.Column(db.String(32), db.ForeignKey(
        'types.name'), nullable=False)
    type_container = db.Column(db.String(32), db.ForeignKey(
        'types.container'), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('name', 'container'),
        db.ForeignKeyConstraint(['type_name', 'type_container'],
                                ['types.name', 'types.container']),
    )


class ActualSensorData(db.Model):
    __tablename__ = 'actualsensordata'

    container = db.Column(db.String(32), db.ForeignKey(
        'instances.container'), nullable=False)
    instance = db.Column(db.String(32), db.ForeignKey(
        'instances.name'), nullable=False)
    property = db.Column(db.String(32), primary_key=True)
    time = db.Column(db.DateTime, default=datetime.utcnow,
                     onupdate=datetime.utcnow, primary_key=True)
    value = db.Column(db.String(32))
    __table_args__ = (
        db.UniqueConstraint('property', 'time'),
        db.ForeignKeyConstraint(['container', 'instance'],
                                ['instances.container', 'instances.name']),
    )


class Relationships(db.Model):
    __tablename__ = 'relationships'

    relation_Id = db.Column(db.BigInteger, primary_key=True)
    source_name = db.Column(db.String(32), db.ForeignKey(
        'types.name'), nullable=False)
    source_container = db.Column(db.String(32), db.ForeignKey(
        'types.container'), nullable=False)
    target_name = db.Column(db.String(32), db.ForeignKey(
        'types.name'), nullable=False)
    target_container = db.Column(db.String(32), db.ForeignKey(
        'types.container'), nullable=False)
    connection_Type = db.Column(db.String(32), nullable=False)
    __table_args__ = (
        db.ForeignKeyConstraint(['source_name', 'source_container', 'target_name', 'target_container'],
                                ['types.name', 'types.container', 'types.name', 'types.container']),
    )


class Links(db.Model):
    __tablename__ = 'links'

    link_Id = db.Column(db.BigInteger, primary_key=True)
    source_name = db.Column(db.String(32), db.ForeignKey(
        'instances.name'), nullable=False)
    source_container = db.Column(db.String(32), db.ForeignKey(
        'instances.container'), nullable=False)
    target_name = db.Column(db.String(32), db.ForeignKey(
        'instances.name'), nullable=False)
    target_container = db.Column(db.String(32), db.ForeignKey(
        'instances.container'), nullable=False)
    relation_Id = db.Column(db.Integer, db.ForeignKey(
        'relationships.relation_Id'), nullable=False)
    __table_args__ = (
        db.ForeignKeyConstraint(['source_name', 'source_container', 'target_name', 'target_container', 'relation_Id'],
                                ['instances.name', 'instances.container', 'instances.name', 'instances.container', 'relationships.relation_Id']),
    )


class Property(db.Model):
    __tablename__ = 'property'

    property_Id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(32), primary_key=True)
    type_name = db.Column(db.String(32), db.ForeignKey(
        'types.name'), nullable=False)
    type_container = db.Column(db.String(32), db.ForeignKey(
        'types.container'), nullable=False)
    data_Type = db.Column(db.String(32), nullable=False)
    __table_args__ = (
        db.UniqueConstraint('property_Id', 'name'),
        db.ForeignKeyConstraint(['type_name', 'type_container'],
                                ['types.name', 'types.container']),
    )


class TypesSchema(ma.SQLAlchemyAutoSchema):
    class TypesTable:
        TypesModel = Types
        load_instance = True


class InstancesSchema(ma.SQLAlchemyAutoSchema):
    class InstancesTable:
        InstancesModel = Instances
        load_instance = True


class ActualSensorDataSchema(ma.SQLAlchemyAutoSchema):
    class ActualSensorDataTable:
        ActualSensorDataModel = ActualSensorData
        load_instance = True


class RelationshipsSchema(ma.SQLAlchemyAutoSchema):
    class RelationshipsTable:
        RelationshipsModel = Relationships
        load_instance = True


class LinksSchema(ma.SQLAlchemyAutoSchema):
    class LinksTable:
        LinksModel = Links
        load_instance = True


class PropertySchema(ma.SQLAlchemyAutoSchema):
    class PropertyTable:
        PropertyModel = Property
        load_instance = True
