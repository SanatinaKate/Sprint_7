import allure
import pytest
from data import Data
from methods.courier_methods import CourierMethods


class TestCourierLogin:

    @allure.title("Проверка возвращаемого кода ответа и идентификатора при успешной авторизации курьера")
    def test_courier_login_check_response_positive(self, courier_prepare_1):
        courier_methods = CourierMethods()
        courier_id, response = courier_methods.courier_login(data=courier_prepare_1)
        assert (response.status_code == 200) and \
               (response.text == f'{{"id":{courier_id}}}'), \
               f"status_code = {response.status_code}, text = {response.text}"

    @allure.title("Проверка невозможности авторизации курьера без передачи всех обязательных полей")
    @pytest.mark.parametrize("key_present, status_code, text", [
        ('login', 504, Data.CODE_504_TEXT),
        ('password', 400, Data.CODE_400_TEXT_FOT_COURIER_LOGIN)
    ])
    def test_courier_login_for_incomplete_data(self, courier_prepare_1, key_present, status_code, text):
        courier_methods = CourierMethods()
        courier_data = {key_present: courier_prepare_1[key_present]}
        _, response = courier_methods.courier_login(data=courier_data)
        assert (response.status_code == status_code) and \
               (response.text == text), \
               f"status_code = {response.status_code}, text = {response.text}"

    @allure.title("Проверка невозможности авторизации курьера с невалидными/несушествующими данными")
    @pytest.mark.parametrize("key_invalid", ['login', 'password'])
    def test_courier_login_for_invalid_data(self, courier_prepare_1, key_invalid):
        courier_methods = CourierMethods()
        courier_data = dict(courier_prepare_1)
        courier_data[key_invalid] += " "
        _, response = courier_methods.courier_login(data=courier_data)
        assert (response.status_code == 404) and \
               (response.text == Data.CODE_404_TEXT_FOT_COURIER_LOGIN), \
               f"status_code = {response.status_code}, text = {response.text}"
