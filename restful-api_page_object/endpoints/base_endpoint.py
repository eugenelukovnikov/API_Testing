from settings import *
class Endpoint():
    
    response = None
    response_json = None
    URL = 'https://api.restful-api.dev'

    def check_status_code_is(self, status):
        return self.response.status_code == status, f'status code is not {status}, but should'

    def check_response_id(self, object_id):
        return self.response_json['id'] == object_id, 'response id and object_id is not match'

    def check_response_is_200(self):
        return self.response.status_code == 200, 'Status code is not 200, but should'

    def check_response_is_404(self):
        return self.response.status_code == 404, 'Status code is not 404, but should'

    def check_response_name(self, name):
        return self.response_json['name'] == name, 'response name and object_name is not match'