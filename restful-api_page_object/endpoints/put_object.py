from settings import *
from endpoints.base_endpoint import Endpoint

class PutObject(Endpoint):
    
    endpoint = '/objects'

    def update_by_id(self, id, payload):
       
       self.response = requests.put(self.URL + self.endpoint + f'/{id}', json = payload)
       self.response_json = self.response.json()

