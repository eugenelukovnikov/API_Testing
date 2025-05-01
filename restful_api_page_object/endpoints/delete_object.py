from settings import *
from endpoints.base_endpoint import Endpoint

class DeleteObject(Endpoint):
    
    endpoint = '/objects'

    def delete_by_id(self, id):
        
        self.response = requests.delete(self.URL + self.endpoint + f'/{id}')
        self.response_json = self.response.json()


