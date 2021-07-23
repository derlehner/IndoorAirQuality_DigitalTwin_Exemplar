import requests
import json
import os
import codecs
import urllib3
urllib3.disable_warnings()


base_url = "https://HariDT.api.weu.digitaltwins.azure.net/" # url of dt service
auth_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiIwYjA3ZjQyOS05ZjRiLTQ3MTQtOTM5Mi1jYzVlOGU4MGM4YjAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC81ZDlkOWNiMS1mNWNkLTQzYTUtYWY4Ni04M2JiMWVmOWRjMmQvIiwiaWF0IjoxNjIyMDM4Mjk3LCJuYmYiOjE2MjIwMzgyOTcsImV4cCI6MTYyMjA0MjE5NywiYWNyIjoiMSIsImFpbyI6IkFXUUFtLzhUQUFBQUVNN1RvVXJXVk1ZYlAxcEZRem5KcDF6ZWVMUzdpN05xU3J5aXRyRkpzeE5YUm4wY0haNEZqNE5vNGxtZmZncyt4b2pkdFZyOFJXUno0b2J3TW1RNjRVTjg5ZStXaWxVV0M2Y2lTTTIxdThjNi9oOU1LS1BiUHBLMklqTTFkWmlHIiwiYWx0c2VjaWQiOiIxOmxpdmUuY29tOjAwMDNCRkZEM0ExMzQ2QjAiLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcGlkIjoiMDRiMDc3OTUtOGRkYi00NjFhLWJiZWUtMDJmOWUxYmY3YjQ2IiwiYXBwaWRhY3IiOiIwIiwiZW1haWwiOiJoYXJpLmdvdmluZGFzYW15QG91dGxvb2suY29tIiwiZmFtaWx5X25hbWUiOiJHb3ZpbmRhc2FteSIsImdpdmVuX25hbWUiOiJIYXJpIiwiaWRwIjoibGl2ZS5jb20iLCJpcGFkZHIiOiIxNDAuNzguNS4xMDUiLCJuYW1lIjoiSGFyaSBHb3ZpbmRhc2FteSIsIm9pZCI6IjU0ZjkxYTI1LWRjNzMtNDI0OS05ZjliLTAyNWY1ZTc5ZGQwZCIsInB1aWQiOiIxMDAzMjAwMTJFNzQ1NUE5IiwicmgiOiIwLkFZRUFzWnlkWGMzMXBVT3Zob083SHZuY0xaVjNzQVRialJwR3UtNEMtZUdfZTBhQkFFSS4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiJuXzE0NDVIZ3UyN0xyM2l5TkpHRFRrdVlLVEl6QnIyWEt6Y25FVERCT3hJIiwidGlkIjoiNWQ5ZDljYjEtZjVjZC00M2E1LWFmODYtODNiYjFlZjlkYzJkIiwidW5pcXVlX25hbWUiOiJsaXZlLmNvbSNoYXJpLmdvdmluZGFzYW15QG91dGxvb2suY29tIiwidXRpIjoibjVYZDRsZndoVVNDWXdqXzdXTTZBZyIsInZlciI6IjEuMCJ9.gtgPXU3xHWdj0kLMZkkhOKlAoQVSs0hDNx4QHIbJTKxSS5roginyvEc87SIbIP6LaP1uNgbtMpWvY8ZBSjNFFn3T1WyXUuOyoYFAJMYunEEjC3o82UVTwRb31xXNbgu5nTrVx-_jRWzqGGZorqeuESx8iNGVV6YlgoTxrGW7LLW_-xvbAys6euzetzsP1YZUr8bzvAeCZIUyB8vX4flg35N2dee2-A4GAoFxikv3Y5IAwF9q9Exu3wXGkQ9yYF9PBl5bAFL4fAQOfVxkwJyJMfCqRxLBICNCe9bqyLv5-UFwYr9vS5u5K7r6Bz96QYvtx2ZM4bBWVj8UYAjdFRKP6A'

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