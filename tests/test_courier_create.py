import allure
import pytest
from data import Data
from helpers import Helpers
from methods.courier_methods import CourierMethods


class TestCourierCreate:

    @allure.title("Проверка возвращаемого кода ответа и текста при успешном создании курьера")
    def test_courier_create_check_response_positive(self):
        courier_methods = CourierMethods()
        _, response = courier_methods.courier_create()
        assert (response.status_code == 201) and \
               (response.text == Data.CODE_2XX_TEXT), \
               f"status_code = {response.status_code}, text = {response.text}"

    @allure.title("Проверка невозможжости создания двух одинаковых курьеров")
    def test_courier_create_for_two_equal_couriers(self):
        courier_methods = CourierMethods()
        courier_data, _ = courier_methods.courier_create()
        _, response = courier_methods.courier_create(data=courier_data)
        assert (response.status_code == 409) and \
               (response.text == Data.CODE_409_TEXT_FOT_COURIER_CREATE), \
               f"status_code = {response.status_code}, text = {response.text}"

    @allure.title("Проверка невозможжости создания курьера с существующим логином")
    def test_courier_create_for_existing_login(self):
        courier_methods = CourierMethods()
        courier_data, _ = courier_methods.courier_create()
        courier_data_2 = {
            'login': courier_data['login'],
            'password': Helpers.generate_random_string(8),
            'firstName': Helpers.generate_random_string(8)
        }
        _, response = courier_methods.courier_create(data=courier_data_2)
        assert (response.status_code == 409) and \
               (response.text == Data.CODE_409_TEXT_FOT_COURIER_CREATE), \
               f"status_code = {response.status_code}, text = {response.text}"

    @allure.title("Проверка невозможности создания курьера без передачи всех обязателных полей")
    @pytest.mark.parametrize("courier_data", [
        {'password': Helpers.generate_random_string(8),'firstName': Helpers.generate_random_string(8)},
        {'login': Helpers.generate_random_string(8),'firstName': Helpers.generate_random_string(8)}
    ])
    def test_courier_create_for_incomplete_data(self, courier_data):
        courier_methods = CourierMethods()
        _, response = courier_methods.courier_create(data=courier_data)
        assert (response.status_code == 400) and \
               (response.text == Data.CODE_400_TEXT_FOT_COURIER_CREATE), \
               f"status_code = {response.status_code}, text = {response.text}"
