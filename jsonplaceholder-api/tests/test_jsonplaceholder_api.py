from settings import *

from endpoints import jsonplaceholder_api
from utils.assertions import Assertions
from payloads.payloads import *


def test_listing_all_resources_posts():
    get_object = jsonplaceholder_api.JsonPlaceholder()
    get_object.listing_all_resources('posts')
    Assertions.check_status_code(get_object.response, 200)
    Assertions.check_number_of_elements_in_response(get_object.response_json, 100)


@pytest.mark.parametrize('id, expected_id', [(1, 1), (50, 50)])
def test_getting_resource_posts(id, expected_id):
    get_object = jsonplaceholder_api.JsonPlaceholder()
    get_object.getting_resource('posts', id)
    Assertions.check_status_code(get_object.response, 200)
    Assertions.check_response_id(get_object.response_json, expected_id)


@pytest.mark.parametrize('value, expected_value', [(1, 1), (10, 10)])
def test_filtering_resource_post_by_userId(value, expected_value):
    field = 'userId'
    get_object = jsonplaceholder_api.JsonPlaceholder()
    get_object.filtering_resource('posts', field, value)
    Assertions.check_status_code(get_object.response, 200)
    Assertions.check_field_value_in_all_elements(get_object.response_json, field, expected_value)


def test_creating_resource():
    get_object = jsonplaceholder_api.JsonPlaceholder()
    get_object.creating_resource('posts', Payload.post())
    Assertions.check_status_code(get_object.response, 201)


def test_updating_resource():
    get_object = jsonplaceholder_api.JsonPlaceholder()
    get_object.updating_resource('posts', Payload.put(), 1)
    Assertions.check_status_code(get_object.response, 200)
    Assertions.check_response_value(get_object.response_json, 'title', 'putted_title')


def test_patching_resource():
    get_object = jsonplaceholder_api.JsonPlaceholder()
    get_object.patching_resource('posts', Payload.patch(), 1)
    Assertions.check_status_code(get_object.response, 200)
    Assertions.check_response_value(get_object.response_json, 'title', 'patched_title')


def test_deleting_resources_posts():
    get_object = jsonplaceholder_api.JsonPlaceholder()
    get_object.deleting_resource('posts', 1)
    Assertions.check_status_code(get_object.response, 200)
