"""
This is the Sensordata module and supports all the REST actions for the
Snesordata collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort
from config import db
from models import (
    ActualSensorData,
    ActualSensorDataSchema
)


def read_all():
    """
    This function responds to a request for /api/sensordata
    with the complete lists of people

    :return:        json string of list of sensordata
    """
    # Create the list of sensor values from our data
    sensordata = ActualSensorData.query.all()
    sensor_schema = ActualSensorDataSchema(many=True)
    data = sensor_schema.dump(sensordata)
    return data


def read_one(container):
    """
    This function responds to a request for /api/sensordata/{container}
    with one matching person from people

    :param container:   container of entry to find
    :return:        entry matching container name
    """
    # Get the entry requested
    entry = ActualSensorData.query \
        .filter(ActualSensorData.container == container) \
        .one_or_none()

    # Did we find a entry?
    if entry is not None:

        # Serialize the data for the response
        sensor_schema = ActualSensorDataSchema(many=True)
        data = sensor_schema.dump(entry)
        return data
    # otherwise, nope, not found
    else:
        abort(
            404, "Entry with container name  {container} not found".format(
                container=container)
        )


def create(sensordata):
    """
    This function creates a new entry in the sensordata structure
    based on the passed  sensordata

    :param entry:  entry to create in sensordata structure
    :return:        201 on success, 406 on person exists
    """
    entry = sensordata
    #id = entry.get("id", None)

    existing_entry = ActualSensorData.query \
        .one_or_none()
    # .filter(ActualSensorData.id == id) \

    # Does the person exist already?
    if existing_entry is None:
        schema = ActualSensorDataSchema()
        new_entry = schema.load(entry, session=db.session)
        db.session.add(new_entry)
        db.session.commit()
        data = schema.dump(new_entry)

        return data, 201

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Entry already exists",
        )


def update(container, entry):
    """
    This function updates an existing entry in the sensordata structure

    :param id:   id of entry to update in the sensordata structure
    :param entry:  entry to update
    :return:        updated sensordata structure
    """

    existing_entry = (
        ActualSensorData.query .filter(
            ActualSensorData.container == container).one_or_none()
    )

    if existing_entry is None:

        abort(
            404, "Entry with container not found".format(container=container)
        )
    else:
        schema = ActualSensorDataSchema()
        update = schema.load(entry, session=db.session)
        update.container = existing_entry.container
        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated entry in the response
        data = schema.dump(existing_entry)

        return data, 200


def delete(container):
    """
    This function deletes an entry from the sensordata structure

    :param id:   id of entry to delete
    :return:        200 on successful delete, 404 if not found
    """
    existing_entry = (
        ActualSensorData.query.filter(
            ActualSensorData.container == container).one_or_none()
    )

    # Does the entry to delete exist?
    if existing_entry is None:
        abort(
            404, "Entry with container not found".format(container=container)
        )
    else:
        db.session.delete(existing_entry)
        db.session.commit()
        return make_response(
            "Entry container deleted", 200
        )
