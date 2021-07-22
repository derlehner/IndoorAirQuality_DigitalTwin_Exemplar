import requests
import json
import os
import codecs

base_url = "https://5099d72a-08e4-416b-8cc6-173009801d45.env.timeseries.azure.com/timeseries" # url of dt service
auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiIxMjBkNjg4ZC0xNTE4LTRjZjctYmQzOC0xODJmMTU4ODUwYjYiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9iY2M3NmFhNy1iYmI1LTQxZjQtYmY1Ny0zMTIwNDJlMzE2ZTUvIiwiaWF0IjoxNjE3OTUyMTUzLCJuYmYiOjE2MTc5NTIxNTMsImV4cCI6MTYxNzk1NjA1MywiYWNyIjoiMSIsImFpbyI6IkFVUUF1LzhUQUFBQUh3ZEhaZk5SN3ZNS3FzSGNNTXBLWk1vdW5ZS0Jlc0phSEtPaVRQWS9rR0d1a01hazl5Yzc5cG1TaEQxL0hRTkVUY3VPdndKOCt0RTBYaDBaUC9zTEhRPT0iLCJhbHRzZWNpZCI6IjE6bGl2ZS5jb206MDAwM0JGRkRBREE3NzBCNSIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiIwNGIwNzc5NS04ZGRiLTQ2MWEtYmJlZS0wMmY5ZTFiZjdiNDYiLCJhcHBpZGFjciI6IjAiLCJlbWFpbCI6ImRhbmllbGdvdHRAbGl2ZS5hdCIsImZhbWlseV9uYW1lIjoiTGVobmVyIiwiZ2l2ZW5fbmFtZSI6IkRhbmllbCIsImdyb3VwcyI6WyJjYjQ3MmNmYi1iY2NkLTQ2YzctYjVjYy05YTcwM2Q4YTA4NWUiXSwiaWRwIjoibGl2ZS5jb20iLCJpcGFkZHIiOiI5MS4xMTUuMTA4LjUiLCJuYW1lIjoiRGFuaWVsIExlaG5lciIsIm9pZCI6IjJlMmI3NjJmLTVkMmQtNDBkOC1hYjg0LTk1ZWE1Njc1MWViNSIsInB1aWQiOiIxMDAzN0ZGRTkzNUUwNkIxIiwicmgiOiIwLkFSRUFwMnJIdkxXNzlFR19WekVnUXVNVzVaVjNzQVRialJwR3UtNEMtZUdfZTBZUkFQRS4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiJtOFh0TUJ0WHNCWk1QYUNwUFQ3MFRwN0cyek9tdlNjSXMxdHVoS0ozc3RBIiwidGlkIjoiYmNjNzZhYTctYmJiNS00MWY0LWJmNTctMzEyMDQyZTMxNmU1IiwidW5pcXVlX25hbWUiOiJsaXZlLmNvbSNkYW5pZWxnb3R0QGxpdmUuYXQiLCJ1dGkiOiIzNHBOSlUtVkYwT3h2NVRmSUtUZEFBIiwidmVyIjoiMS4wIn0.n61I66S8uba5Se6HDw-1_ZRhj7paZx34W3rBwZ2osOVEgZ39O7EuhBnz25fJZlQcgM_WXgtHAPt31sxAJm8Zmh4ICDB8rL8MdyA86KrxpYth5znestKL5rfdTHTP5uF-s_rsMANoOZEKgU6vYt-DBXDsKiXb6fIb6-3CD4uQ9LbVNybfqxi19GHz1KWnzB4Wtg2efjDPWX8cvSqse0yOVhkoofqkxstfvfJGub6vcMlk0EqLuh5tmbMpeRw9FbUrYrLCZEokcCNN6dC2kuFiHQsxMFtrhODj74P_mBBsoRMndbVmGYcZcI6ev6OhKl6PitMXhPR0X4HK__-Ev6W-oA"

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
    method_extension = "/types/$batch?api-version=2020-07-31"
    request = {"put":[interface]}
    exec_post(method_extension, request)
    return

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
    response = requests.post(base_url + method_extension, json=json_request, verify=False, auth=BearerAuth(auth_token))
    print("####################### POST Request to " + method_extension + " #######################")
    print(json_request)
    process_response(response)

def exec_put(method_extension, json_request):
    response = requests.put(base_url + method_extension, json=json_request, verify=False, auth=BearerAuth(auth_token))
    print("####################### PUT Request to " + method_extension + " #######################")
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