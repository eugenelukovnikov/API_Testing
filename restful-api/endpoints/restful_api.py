from settings import *

class RestfulApi():

    URL = 'https://api.restful-api.dev'

    def __init__(self, url=URL):
        self.URL = url


    def post_object(self, payload):
        self.endpoint = '/objects'
        self.response = requests.post(self.URL + self.endpoint, json = payload)
        self.response_json = self.response.json()

    
    def get_object(self, id):
        self.endpoint = '/objects'
        self.response = requests.get(self.URL + self.endpoint + f'/{id}')
        self.response_json = self.response.json()
        print('Your id =', self.response_json['id'])

   
    def put_object(self, id, payload):
        self.endpoint = '/objects'
        self.response = requests.put(self.URL + self.endpoint + f'/{id}', json = payload)
        self.response_json = self.response.json()    


    def delete_object(self, id):
        self.endpoint = '/objects'
        self.response = requests.delete(self.URL + self.endpoint + f'/{id}')
        self.response_json = self.response.json()