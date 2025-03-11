from settings import *

class JsonPlaceholder():

    URL = 'https://jsonplaceholder.typicode.com'

    def __init__(self, url=URL):
        self.URL = url


    def getting_resource(self, endpoint, id):
        #https://jsonplaceholder.typicode.com/posts/1
        self.endpoint = f'/{endpoint}/{id}'
        self.response = requests.get(self.URL + self.endpoint)
        self.response_json = self.response.json()


    def listing_all_resources(self, endpoint):
        #https://jsonplaceholder.typicode.com/posts/
        self.endpoint = f'/{endpoint}/'
        self.response = requests.get(self.URL + self.endpoint)
        self.response_json = self.response.json() 


    def creating_resource(self, endpoint, payload):
        #https://jsonplaceholder.typicode.com/posts
        self.endpoint = f'/{endpoint}/'
        self.response = requests.post(self.URL + self.endpoint, data=payload)
        self.response_json = self.response.json()


    def updating_resource(self, endpoint, payload, id):
        #https://jsonplaceholder.typicode.com/posts/1
        self.endpoint = f'/{endpoint}/{id}'
        self.response = requests.put(self.URL + self.endpoint, data=payload)
        self.response_json = self.response.json()   


    def patching_resource(self, endpoint, payload, id):
        #https://jsonplaceholder.typicode.com/posts/1
        self.endpoint = f'/{endpoint}/{id}'
        self.response = requests.patch(self.URL + self.endpoint, data=payload)
        self.response_json = self.response.json()          


    def deleting_resource(self, endpoint, id):
        #https://jsonplaceholder.typicode.com/posts/1
        self.endpoint = f'/{endpoint}/{id}'
        self.response = requests.get(self.URL + self.endpoint)
        self.response_json = self.response.json() 
       
       
    def filtering_resource(self, endpoint, field, value):
        #https://jsonplaceholder.typicode.com/posts?userId=1
        self.endpoint = f'/{endpoint}?{field}={value}'
        self.response = requests.get(self.URL + self.endpoint)
        self.response_json = self.response.json() 

       
        