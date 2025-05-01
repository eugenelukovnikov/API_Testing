from settings import *

from endpoints import create_object
from endpoints import get_object
from endpoints import put_object
from endpoints import delete_object

#CRUD - Create Read Update Delete

payload_post = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}

payload_put = {
    "name": "Apple MacBook Pro 20",
    "data": {
        "year": 2020,
        "price": 1999.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}


def test_post_object():
    
    new_object_endpoint = create_object.CreateObject()
    new_object_endpoint.new_object(payload=payload_post)
    assert new_object_endpoint.check_response_is_200()
    assert new_object_endpoint.check_response_name(payload_post['name'])


def test_get_object(obj_id):
    
    get_object_endpoint = get_object.GetObject()
    get_object_endpoint.get_by_id(obj_id)
    assert get_object_endpoint.check_response_is_200()
    # assert get_object_endpoint.check_status_code_is(200)
    assert get_object_endpoint.check_response_id(obj_id)

def test_put_object(obj_id):
    
    update_object_endpoint = put_object.PutObject()
    update_object_endpoint.update_by_id(obj_id, payload=payload_put)
    assert update_object_endpoint.check_response_is_200()
    assert update_object_endpoint.check_response_name(payload_put['name'])


def test_delete_object(obj_id):
    
    delete_object_endpoint = delete_object.DeleteObject()
    delete_object_endpoint.delete_by_id(obj_id)
    assert delete_object_endpoint.check_response_is_200()
    # get_object_endpoint = get_object.GetObject()
    # get_object_endpoint.check_response_id(obj_id)
    # get_object_endpoint.get_by_id(obj_id)
    # get_object_endpoint.check_response_is_404()
