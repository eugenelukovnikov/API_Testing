from settings import *

class BreweryApi():

    URL = 'https://api.openbrewerydb.org/v1'

    def __init__(self, url=URL):
        self.URL = url


    def get_all_breweries(self):
        #https://api.openbrewerydb.org/v1/breweries
        self.endpoint = '/breweries'
        self.response = requests.get(self.URL + self.endpoint)
        self.response_json = self.response.json()


    def get_breweries_by_city(self, city):
        #https://api.openbrewerydb.org/v1/breweries?by_city=Portland&per_page=200
        self.endpoint = f'/breweries?by_city={city}&per_page=200'
        self.response = requests.get(self.URL + self.endpoint)
        self.response_json = self.response.json()


    def get_breweries_by_dict(self, x, y):
        #https://api.openbrewerydb.org/v1/breweries?by_dist={32.88313237},-117.1649842&per_page=3
        self.endpoint = f'/breweries?by_dist={x},{y}&per_page=3'
        self.response = requests.get(self.URL + self.endpoint)
        self.response_json = self.response.json()


    def get_breweries_by_country(self, county):
        #https://api.openbrewerydb.org/v1/breweries?by_country=south%20korea&per_page=200
        self.endpoint = f'/breweries?by_country={county}&per_page=200'
        self.response = requests.get(self.URL + self.endpoint)
        self.response_json = self.response.json()  


    def get_breweries_by_state(self, state):
        #https://api.openbrewerydb.org/v1/breweries?by_state=california&sort=type,name:desc&per_page=3
        self.endpoint = f'//breweries?by_state={state}&sort=type,name:desc&per_page=3'
        self.response = requests.get(self.URL + self.endpoint)
        self.response_json = self.response.json()  
       
        