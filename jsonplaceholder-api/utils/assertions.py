from settings import *
class Assertions():
    
    @staticmethod
    def check_status_code(response, expected_code):
        """Проверить статус-код ответа."""
        assert response.status_code == expected_code, \
        f"Expected status code {expected_code}, but got {response.status_code}"


    @staticmethod
    def check_response_id(response_json, id):
        """Проверяет, что ID в ответе соответствует ожидаемому."""
        assert response_json['id'] == id, \
        f"Expected name '{id}', but got '{response_json['id']}'"


    @staticmethod
    def check_field_value_in_all_elements(response_json, field, expected_value):
        """Проверяет, что значение интересующего поля во всех элементах соответствует ожидаемому."""
        for elem in response_json:
            assert elem[field] == expected_value, \
            f"Expected name '{expected_value}', but got '{elem[field]}'"


    @staticmethod
    def check_number_of_elements_in_response(response_json, expected_number):
        assert len(response_json) == expected_number, f"Ожидалось {expected_number} элементов, но получено {len(response_json)}"


    @staticmethod
    def check_response_value(response_json, field, value):
        """Проверяет, что значение поля в ответе соответствует ожидаемому."""
        assert response_json[field] == value, \
        f"Expected '{value}', but got '{response_json[{field}]}'"
 