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
    def check_response_status(response_json, status):
        """Проверяет, что статус в ответе соответствует ожидаемому."""
        assert response_json['status'] == status, \
        f"Expected status '{status}', but got '{response_json['status']}'"

    @staticmethod
    def is_field_in_response(response_json, field):
        """Проверяет, что в ответе есть нужное поле."""
        assert field in response_json['message'], \
        f"Expected field '{field}', but it not in response"
    
    @staticmethod
    def is_field_amount_in_response_correct(response_json, num):
        extensions=(".jpg", ".jpeg", ".png")
        image_links = [link for link in response_json["message"] if link.lower().endswith(extensions)]
        amount = len(image_links)

        """Проверяет, что количество изображений в ответе соответствует ожидаемому."""
        assert num == amount, \
        f"Expected fields amount = '{num}', but it is {amount}"

    @staticmethod
    def is_expected_data_in_response_message(response_json, expected_data):
        assert response_json["message"] == expected_data, \
        f"Ожидаемые данные: {expected_data}, полученные данные: {response_json['message']}"