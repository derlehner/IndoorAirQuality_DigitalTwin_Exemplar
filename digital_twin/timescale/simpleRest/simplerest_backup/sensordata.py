"""
This is the Sensordata module and supports all the ReST actions for the
Snesordata collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort
from config import db, oidc
from sqlalchemy import exc
from models import (
    Sensordata,
    SensorSchema,
)


def read_all(length=0):
    """
    This function responds to a request for /api/sensordata
    with the complete lists of people
    :param length: optional prameter to limit results returned
    :return:        json string of list of sensordata
    """
    # Create the list of people from our data
    if length > 0:
        sensordata = Sensordata.query.order_by(Sensordata.time.desc()).limit(length).all()
    else:
        sensordata = Sensordata.query.order_by(Sensordata.time.desc()).all()
    sensor_schema = SensorSchema(many=True)
    data = sensor_schema.dump(sensordata)
    return data


def read_one(id):
    """
    This function responds to a request for /api/sensordata/{id}
    with one matching person from people

    :param id:   id of entry to find
    :return:        entry matching id
    """
    # Get the entry requested
    entry = Sensordata.query \
        .filter(Sensordata.id == id) \
        .one_or_none()

    # Did we find a entry?
    if entry is not None:

        # Serialize the data for the response
        sensor_schema = SensorSchema()
        data = sensor_schema.dump(entry)
        return data
    # otherwise, nope, not found
    else:
        abort(
            404, "Entry with id {id} not found".format(id=id)
        )

# Please uncomment this line for server deployment
@oidc.accept_token(require_token=True)
def create(sensordata):
    """
    This function creates a new entry in the sensordata structure
    based on the passed  sensordata

    :param entry:  entry to create in sensordata structure
    :return:        201 on success, 406 on person exists
    """

    entry = sensordata

    # Does the person exist already?
    try:
        schema = SensorSchema()
        new_entry = schema.load(entry, session=db.session)
        db.session.add(new_entry)
        db.session.commit()
        data = schema.dump(new_entry)
        return data, 201
    except exc.SQLAlchemyError as e:
        print(e)
        abort(
            400, "There was a Problem!"
        )

# Please uncomment this line for server deployment
@oidc.accept_token(require_token=True)
def update(id, entry):
    """
    This function updates an existing entry in the sensordata structure

    :param id:   id of entry to update in the sensordata structure
    :param entry:  entry to update
    :return:        updated sensordata structure
    """

    existing_entry = (
        Sensordata.query .filter(Sensordata.id == id).one_or_none()
    )

    if existing_entry is None:

        abort(
            404, "Entry with id {id} not found".format(id=id)
        )
    else:
        schema = SensorSchema()
        update = schema.load(entry, session=db.session)
        update.id = existing_entry.id
        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated entry in the response
        data = schema.dump(existing_entry)

        return data, 200


#@oidc.accept_token(require_token=True)
def delete(id):
    """
    This function deletes an entry from the sensordata structure

    :param id:   id of entry to delete
    :return:        200 on successful delete, 404 if not found
    """
    existing_entry = (
        Sensordata.query.filter(Sensordata.id == id).one_or_none()
    )

    # Does the entry to delete exist?
    if existing_entry is None:
        abort(
            404, "Entry with id {id} not found".format(id=id)
        )
    else:
        db.session.delete(existing_entry)
        db.session.commit()
        return make_response(
            "Entry {id} deleted".format(id=id), 200
        )
