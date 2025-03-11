from settings import *
class Assertions():
    
    @staticmethod
    def check_status_code(response, expected_code):
        """Проверить статус-код ответа."""
        assert response.status_code == expected_code, \
        f"Expected status code {expected_code}, but got {response.status_code}"


    @staticmethod
    def check_response_name(response_json, name):
        """Проверяет, что имя в ответе соответствует ожидаемому."""
        assert response_json['name'] == name, \
        f"Expected name '{name}', but got '{response_json['name']}'"


    @staticmethod
    def is_field_in_response(response_json, field):
        """Проверяет, что в ответе есть нужное поле."""
        assert field in response_json['message'], \
        f"Expected field '{field}', but it not in response"


    @staticmethod
    def is_response_structure_correct(response_json, expected_keys):
        
        """Проверяем, что все ожидаемые ключи присутствуют в каждом элементе"""
        for brewery in response_json:
            assert expected_keys.issubset(brewery.keys()), f"Missing keys in brewery: {brewery}"


    @staticmethod
    def is_field_in_response_correct(response_json, field, expected_value):
        for brewery in response_json:
            # Проверяем, что поле существует
            assert field in brewery, f"Missing '{field}' key in brewery: {brewery}"
            # Проверяем, что значение поля соответствует ожидаемому
            assert expected_value in brewery[field], f"Expected {field} with '{expected_value}', but got '{brewery[field]}' in brewery: {brewery}"

    @staticmethod
    def coordinates_is_in_normal_range(response_json, x, y):
        for brewery in response_json:
            longitude = float(brewery["longitude"])
            latitude = float(brewery["latitude"])
            assert abs(latitude - x) < 10, f"Latitude {latitude} is too far from {x}"
            assert abs(longitude - y) < 10, f"Longitude {longitude} is too far from {y}"

