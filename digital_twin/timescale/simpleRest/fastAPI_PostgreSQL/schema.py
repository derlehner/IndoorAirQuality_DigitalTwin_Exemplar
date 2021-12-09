from pydantic import BaseModel

class TypesRequest(BaseModel):
    name: str

class TypesResponse(BaseModel):
   
    name: str

class PropertiesRequest(BaseModel):
    name: str
    type: str


class PropertiesResponse(BaseModel):
    name: str
    type: str

class InstancesRequest(BaseModel):
    name: str
    typename: str
   
class InstancesResponse(BaseModel):
    name: str
    typename:  str
    
class ValuesRequest(BaseModel):
    propertyname : str
    instancename : str
    value: str
    time: datetime
    
class ValuesResponse(BaseModel):
    propertyname : str
    instancename : str
    value: str
    time: datetime
