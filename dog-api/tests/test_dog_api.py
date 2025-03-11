from settings import *

from endpoints import dog_api
from utils.assertions import Assertions


def test_get_all_breeds():
    
    get_object = dog_api.DogApi()
    get_object.get_all_breeds()
    Assertions.check_status_code(get_object.response, 200)
    Assertions.check_response_status(get_object.response_json, 'success')


@pytest.mark.parametrize('field', [('affenpinscher'), ('newfoundland'), ('wolfhound')])
def test_check_fields_in_all_breeds(field):
    
    get_object = dog_api.DogApi()
    get_object.get_all_breeds()
    Assertions.check_status_code(get_object.response, 200)
    Assertions.check_response_status(get_object.response_json, 'success')
    Assertions.is_field_in_response(get_object.response_json, field)



@pytest.mark.parametrize('num', [1, 50, 99])
def test_get_multiple_random_images_random_breed(num, request):
    if num > 50:
        request.node.add_marker(pytest.mark.xfail(reason="Ожидаемо падающий тест для num > 50"))
    get_object = dog_api.DogApi()
    get_object.get_multiple_random_images_random_breed(num)
    Assertions.check_status_code(get_object.response, 200)
    Assertions.check_response_status(get_object.response_json, 'success')
    Assertions.is_field_amount_in_response_correct(get_object.response_json, num)


@pytest.mark.parametrize('breed, num', [('cattledog', 18), ('wolfhound', 135), ('terrier', 1000)])
def test_get_some_breed_all_images(breed, num):
    get_object = dog_api.DogApi()
    get_object.get_some_breed_all_images(breed)
    Assertions.check_status_code(get_object.response, 200)
    Assertions.check_response_status(get_object.response_json, 'success')
    Assertions.is_field_amount_in_response_correct(get_object.response_json, num)


@pytest.mark.parametrize('breed, num', [('hound', 3), ('hound', 250), ('hound', 808)])
def test_get_multiple_random_images_some_breed(breed, num):
    get_object = dog_api.DogApi()
    get_object.get_multiple_random_images_some_breed(breed, num)
    Assertions.check_status_code(get_object.response, 200)
    Assertions.check_response_status(get_object.response_json, 'success')
    Assertions.is_field_amount_in_response_correct(get_object.response_json, num)


@pytest.mark.parametrize('breed, expected_data', [
    ('hound', ["afghan", "basset", "blood", "english", "ibizan", "plott", "walker"]), 
    ('husky', []), 
    ('bulldog', ["boston","english","french"])])
def test_get_subbreeds_from_breed(breed, expected_data):
    get_object = dog_api.DogApi()
    get_object.get_subbreeds_from_breed(breed)
    Assertions.check_status_code(get_object.response, 200)
    Assertions.check_response_status(get_object.response_json, 'success')
    Assertions.is_expected_data_in_response_message(get_object.response_json, expected_data)


def test_negative_get_some_breed_all_images():
    get_object = dog_api.DogApi()
    get_object.get_some_breed_all_images('negative')
    Assertions.check_status_code(get_object.response, 404)


def test_negative_get_subbreeds_from_breed():
    get_object = dog_api.DogApi()
    get_object.get_subbreeds_from_breed('negative')
    Assertions.check_status_code(get_object.response, 404)