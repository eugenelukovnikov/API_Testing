from settings import *

class DogApi():

    URL = 'https://dog.ceo/api'

    def __init__(self, url=URL):
        self.URL = url


    def get_all_breeds(self):
        #https://dog.ceo/api/breeds/list/all
        self.endpoint = '/breeds/list/all'
        self.response = requests.get(self.URL + self.endpoint)
        self.response_json = self.response.json()

    def get_multiple_random_images_random_breed(self, num):
        #https://dog.ceo/api/breeds/image/random/3
        self.endpoint = f'/breeds/image/random/{num}'
        self.response = requests.get(self.URL + self.endpoint)
        self.response_json = self.response.json()

    def get_some_breed_all_images(self, breed):
        #https://dog.ceo/api/breed/cattledog/images
        self.endpoint = f'/breed/{breed}/images'
        self.response = requests.get(self.URL + self.endpoint)
        self.response_json = self.response.json()

    def get_multiple_random_images_some_breed(self, breed, num):
        #https://dog.ceo/api/breed/hound/images/random/3
        self.endpoint = f'/breed/{breed}/images/random/{num}'
        self.response = requests.get(self.URL + self.endpoint)
        self.response_json = self.response.json()    
   
    def get_subbreeds_from_breed(self, breed):
        #https://dog.ceo/api/breed/hound/list
        self.endpoint = f'/breed/{breed}/list'
        self.response = requests.get(self.URL + self.endpoint)
        self.response_json = self.response.json() 