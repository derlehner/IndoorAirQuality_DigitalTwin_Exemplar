import digital_twin_api
import urllib3
import json
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


interface_file_names = ["Room", "AirQualitySensor", "AirQualityController"]
twin_file_names = ["Raspberry1", "Raspberry2", "Raspberry3",
                    "Room101", "Room102", "Lobby100"]
delete_interface_ids = ["dtmi:com:example:Room;2", "dtmi:org:example:AirQualityController;2", "dtmi:org:example:cotwoSensor;2"]
delete_relationship_ids = [("Lobby100", "rel1"), ("Room101", "rel2"), ("Room102", "rel3"), ("Room102", "rel4")]
delete_dtids = ["Room101", "Room102", "Lobby100",
                    "Raspberry1", "Raspberry2", "Raspberry3"]

def create_schema():
    for file_name in interface_file_names:
        interface_to_create = None
        # with open("/home/hari/cdlmint_airqualityusecase/Digital Twin/AirRaspi/AirQuality/interface_models/{}.json".format(file_name)) as tc_file:
        print('current cwd'+ os.getcwd())
        with open("/home/hari/cdlmint_airqualityusecase/Digital Twin/AirRaspi/AirQuality/interface_models/" + file_name + ".json") as tc_file:
            interface_to_create = json.load(tc_file)
        digital_twin_api.create_interface(interface_to_create)

def create_instances():
    for file_name in twin_file_names:
        twin_to_create = None
        with open("/home/hari/cdlmint_airqualityusecase/Digital Twin/AirRaspi/AirQuality/twin_models/" + file_name + ".json") as tc_file:
            twin_to_create = json.load(tc_file)
        # create digital twin in azure
        digital_twin_api.create_twin(twin_to_create["dtid"], twin_to_create["content"])
        # create outgoing relationships in azure
        if "relationships" in twin_to_create.keys():
            for rel in twin_to_create["relationships"]:
                digital_twin_api.create_relationship(twin_to_create["dtid"], rel["id"], rel["content"])

def send_telemetry_data():
    # send telemetry data
    values = None
    with open("telemetry_data/" + "testdata" + ".json") as tc_file:
        values = json.load(tc_file)
    for telemetry_value in values:
        dtid = telemetry_value["dtid"]
        component_name = telemetry_value["componentId"]
        telemetry = telemetry_value["content"]
        digital_twin_api.send_telemetry_for_component(dtid, component_name, telemetry)


def cleanup():
    # cleanup
    for rel in delete_relationship_ids:
        digital_twin_api.delete_relationship(rel[0], rel[1])
    for dtid in delete_dtids: 
        digital_twin_api.delete_twin(dtid)
    for interface_id in delete_interface_ids:
        digital_twin_api.delete_interface(interface_id)

create_schema()
#create_instances()
#send_telemetry_data()
#cleanup()



