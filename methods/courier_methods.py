import allure
import requests
from data import Data
from helpers import Helpers


class CourierMethods:

    @allure.step("Создать курьера")
    def courier_create(self, data=None, raise_error=False):
        courier = {}
        if data is None:
            data = {
                'login': Helpers.generate_random_string(7),
                'password': Helpers.generate_random_string(7),
                'firstName': Helpers.generate_random_string(7)
            }
        response = requests.post(url=Data.COURIER_URL, data=data)
        if response.status_code == 201:
            courier = dict(data)
        elif raise_error:
            raise AssertionError("Не удалось создать курьера")
        return courier, response

    @allure.step("Авторизовать курьера")
    def courier_login(self, data, raise_error=False):
        courier_id = -1
        response = requests.post(url=f"{Data.COURIER_URL}/login", data=data)
        if response.status_code == 200:
            courier_id = response.json()['id']
        elif raise_error:
            raise AssertionError("Не удалось авторизовать курьера")
        return courier_id, response

    @allure.step("Удалить курьера")
    def courier_delete(self, courier_id):
        response = requests.delete(url=f"{Data.COURIER_URL}/{courier_id}")
        return response
