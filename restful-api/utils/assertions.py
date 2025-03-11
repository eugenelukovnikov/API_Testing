from settings import *
class Assertions():
    
    @staticmethod
    def check_status_code(response, expected_code):
        """Проверить статус-код ответа."""
        assert response.status_code == expected_code, \
        f"Expected status code {expected_code}, but got {response.status_code}"

    @staticmethod
    def check_response_id(response_json, object_id):
        """Проверяет, что ID в ответе соответствует ожидаемому."""
        assert response_json['id'] == object_id, \
        f"Expected ID {object_id}, but got {response_json['id']}"


    @staticmethod
    def check_response_name(response_json, name):
        """Проверяет, что имя в ответе соответствует ожидаемому."""
        assert response_json['name'] == name, \
        f"Expected name '{name}', but got '{response_json['name']}'"