from settings import *
from endpoints.base_endpoint import Endpoint

class CreateObject(Endpoint):
    
    endpoint = '/objects'
    
    def new_object(self, payload):
      
        self.response = requests.post(self.URL + self.endpoint, json = payload)
        self.response_json = self.response.json()
