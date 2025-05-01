from settings import *
from endpoints.base_endpoint import Endpoint

class GetObject(Endpoint):
    
    endpoint = '/objects'

    def get_by_id(self, id):

        self.response = requests.get(self.URL + self.endpoint + f'/{id}')
        self.response_json = self.response.json()
        print('Your id =', self.response_json['id'])

    
    