from settings import *

from endpoints import restful_api
from utils.assertions import Assertions
from payloads import payloads

post_payload = payloads.Payload.post()
put_payload = payloads.Payload.put()
patch_payload = payloads.Payload.patch()


def test_post_object():
    
    new_object = restful_api.RestfulApi()
    new_object.post_object(payload=post_payload)
    Assertions.check_status_code(new_object.response, 200)
    Assertions.check_response_name(new_object.response_json, post_payload['name'])


def test_get_object(obj_id):
    
    get_object = restful_api.RestfulApi()
    get_object.get_object(obj_id)
    Assertions.check_status_code(get_object.response, 200)
    Assertions.check_response_id(get_object.response_json, obj_id)


def test_put_object(obj_id):
    
    put_object = restful_api.RestfulApi()
    put_object.put_object(obj_id, payload=put_payload)
    Assertions.check_status_code(put_object.response, 200)
    Assertions.check_response_name(put_object.response_json, put_payload['name'])


def test_delete_object(obj_id):
    
    delete_object = restful_api.RestfulApi()
    delete_object.delete_object(obj_id)
    Assertions.check_status_code(delete_object.response, 200)
    # get_object_endpoint = get_object.GetObject()
    # get_object_endpoint.check_response_id(obj_id)
    # get_object_endpoint.get_by_id(obj_id)
    # get_object_endpoint.check_response_is_404()
