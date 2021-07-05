import requests
import json
import os
import codecs

base_url = "https://AzureDT.api.weu.digitaltwins.azure.net/" # url of dt service
auth_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiIwYjA3ZjQyOS05ZjRiLTQ3MTQtOTM5Mi1jYzVlOGU4MGM4YjAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC81ZDlkOWNiMS1mNWNkLTQzYTUtYWY4Ni04M2JiMWVmOWRjMmQvIiwiaWF0IjoxNjIzMjQzNzM0LCJuYmYiOjE2MjMyNDM3MzQsImV4cCI6MTYyMzI0NzYzNCwiYWNyIjoiMSIsImFpbyI6IkFXUUFtLzhUQUFBQVVtcjEzUmxVejBuZmhiMmRIWGJMMG42Mkw0akNCZVp2NUM3RGNJYUwvN2FwbjJ5cmZ0c0Y3QlF0eWFXRTgzVXJTc2tqaG1uOWwvS2t5R3R6N1JaZER0RVNraTV5WkppcE0yd1VLTlRHbUtsU25CbkwzMGFiUWowZlVxT2xPelQzIiwiYWx0c2VjaWQiOiIxOmxpdmUuY29tOjAwMDM3RkZFMTdBRjc5REYiLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcGlkIjoiMDRiMDc3OTUtOGRkYi00NjFhLWJiZWUtMDJmOWUxYmY3YjQ2IiwiYXBwaWRhY3IiOiIwIiwiZW1haWwiOiJyYW15YWNzZS5qa3VAZ21haWwuY29tIiwiZmFtaWx5X25hbWUiOiJKYXlhcmFtYW4iLCJnaXZlbl9uYW1lIjoiUmFteWEiLCJpZHAiOiJsaXZlLmNvbSIsImlwYWRkciI6IjE5My4xNzEuMzguNDEiLCJuYW1lIjoiUmFteWEgSmF5YXJhbWFuIiwib2lkIjoiNWZlMTBlMjAtNzFmYS00ZWM3LTgzNDAtZDk1NWJlYjk5YTU3IiwicHVpZCI6IjEwMDMyMDAxNDM4QjQwNTYiLCJyaCI6IjAuQVlFQXNaeWRYYzMxcFVPdmhvTzdIdm5jTFpWM3NBVGJqUnBHdS00Qy1lR19lMGFCQU9VLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6Ild5UnJmamdGNnkxcVRETzB6Sm02Qzk4WE9SLTNUWDFybDhTaFN6RDZaWmsiLCJ0aWQiOiI1ZDlkOWNiMS1mNWNkLTQzYTUtYWY4Ni04M2JiMWVmOWRjMmQiLCJ1bmlxdWVfbmFtZSI6ImxpdmUuY29tI3JhbXlhY3NlLmprdUBnbWFpbC5jb20iLCJ1dGkiOiJOb1pZSU95OURVR3czN2ktZlo1LUFBIiwidmVyIjoiMS4wIn0.Lz_tli_M7TZkEGmV9R54ecvd0zGQzC4d6QGRRTai9r3iRzmkT3KsTyY0Qrgwg8KfwcKfvTO4WIo9haZIN_jGtbzPkyU_XGPSVrpxx_LuchwGlZoQS2IYtPUQm1gCK3b7ua96PH_S7wKcYkBo0olpuV2jWxxFndAdX24GSwjSsnE71zVokPB4QSuyB3bKNjorAF-mcBGpT_2--Qaf-yYOFoqdrYpFgXnhzzq1UCAHSiCylThKSQcv9g2BU0Hr0jIQS1zvJcTri0RArf_h7Kvkobr7cQgRLQwI_334V_HoJO9bYdo0br0Z9OHW1I_lzv8JYOsfcRSu4TIx3l5RE3kh2g"
def create_twin(dtid, request):
    method_extension = "digitaltwins/" + dtid + "?api-version=2020-10-31"
    exec_put(method_extension, request)

def delete_twin(dtid):
    method_extension = "digitaltwins/" + dtid + "?api-version=2020-10-31"
    exec_delete(method_extension)

def create_relationship(source_dtid, rel_id, request):
    method_extension = "digitaltwins/" + source_dtid + "/relationships/" + rel_id + "?api-version=2020-10-31"
    exec_put(method_extension, request)

def delete_relationship(dtid, rel_id):
    method_extension = "digitaltwins/" + dtid + "/relationships/" + rel_id + "?api-version=2020-10-31"
    exec_delete(method_extension)

def create_interface(interface):
    method_extension = "models?api-version=2020-10-31"
    request = []
    request.append(interface)
    exec_post(method_extension, request)

def delete_interface(id):
    method_extension = "models/" + id + "?api-version=2020-10-31"
    exec_delete(method_extension)

def send_telemetry_for_twin(dtid, telemetry):
    method_extension = "digitaltwins/" + dtid + "/telemetry?api-version=2020-10-31"
    exec_post(method_extension, telemetry)

def send_telemetry_for_component(dtid, component_name, telemetry):
    method_extension = "digitaltwins/" + dtid + "/components/" + component_name + "/telemetry?api-version=2020-10-31"
    exec_post(method_extension, telemetry)

# generic REST methods
def exec_post(method_extension, json_request):
    headers = {'Message-Id': 'e5ca50dd-ca31-4fae-8d84-3af5a72b10c5'}
    response = requests.post(base_url + method_extension, json=json_request, verify=False, auth=BearerAuth(auth_token), headers = headers )
    print("####################### POST Request to " + method_extension + " #######################")
    print(json_request)
    process_response(response)

def exec_put(method_extension, json_request):
    response = requests.put(base_url + method_extension, json=json_request, verify=False, auth=BearerAuth(auth_token))
    print("####################### PUT Request to " + method_extension + " #######################")
    print(json_request)
    process_response(response)

def exec_delete(method_extension):
    response = requests.delete(base_url + method_extension, verify=False, auth=BearerAuth(auth_token))
    print("####################### DELETE Request to " + method_extension + " #######################")
    process_response(response)

def process_response(response):
    if str(response.status_code)[0] == "2":
        print("SUCCESS")
    else:
        print("Request FAILED with error message: " + str(response.content))


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
