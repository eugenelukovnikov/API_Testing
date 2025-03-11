from settings import *

from endpoints import brewery_api
from utils.assertions import Assertions


def test_structure_get_all_breweries():
    expected_keys = {
        "id", "name", "brewery_type", "address_1", "address_2", "address_3",
        "city", "state_province", "postal_code", "country", "longitude",
        "latitude", "phone", "website_url", "state", "street"
    }
    get_object = brewery_api.BreweryApi()
    get_object.get_all_breweries()
    Assertions.check_status_code(get_object.response, 200)
    Assertions.is_response_structure_correct(get_object.response_json, expected_keys)


@pytest.mark.parametrize("expected_city", ["Norman", "Austin", "Portland"])
def test_get_breweries_by_city(expected_city):
    get_object = brewery_api.BreweryApi()
    get_object.get_breweries_by_city(expected_city)
    Assertions.check_status_code(get_object.response, 200)
    Assertions.is_field_in_response_correct(get_object.response_json, 'city', expected_city)


@pytest.mark.parametrize("expected_country", ["Germany", "South Korea", "United States"])
def test_get_breweries_by_country(expected_country):
    get_object = brewery_api.BreweryApi()
    get_object.get_breweries_by_country(expected_country)
    Assertions.check_status_code(get_object.response, 200)
    Assertions.is_field_in_response_correct(get_object.response_json, 'country', expected_country)


@pytest.mark.parametrize("expected_state", ["California", "Oklahoma", "Texas"])
def test_get_breweries_by_state(expected_state):
    get_object = brewery_api.BreweryApi()
    get_object.get_breweries_by_state(expected_state)
    Assertions.check_status_code(get_object.response, 200)
    Assertions.is_field_in_response_correct(get_object.response_json, 'state_province', expected_state)


@pytest.mark.parametrize("x, y", [(32.88313237, -117.1649842), (25.883, -90.164)])
def test_get_breweries_by_dict(x, y):
    get_object = brewery_api.BreweryApi()
    get_object.get_breweries_by_dict(x,y)
    Assertions.check_status_code(get_object.response, 200)
    Assertions.coordinates_is_in_normal_range(get_object.response_json, x, y)