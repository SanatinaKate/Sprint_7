import allure
import json
import requests
from data import Data


class OrdersMethods:

    @allure.step("Создать заказ")
    def order_create(self, data, raise_error=False):
        track = -1
        response = requests.post(url=Data.ORDERS_URL, json=data)
        if response.status_code == 201:
            track = response.json()['track']
        elif raise_error:
            raise AssertionError("Не удалось создать заказ")
        return track, response

    @allure.step("Получить идентификатор заказа")
    def order_get_id(self, track, raise_error=False):
        order_id = -1
        response = requests.get(url=f"{Data.ORDERS_URL}/track?t={track}")
        if response.status_code == 200:
            order_id = response.json()['order']['id']
        elif raise_error:
            raise AssertionError("Не удалось получить идентификатор заказа")
        return order_id, response

    @allure.step("Принять заказ")
    def order_accept(self, order_id, courier_id, raise_error=False):
        response = requests.put(url=f"{Data.ORDERS_URL}/accept/{order_id}?courierId={courier_id}")
        if raise_error and (response.status_code != 200):
            raise AssertionError("Не удалось принять заказ")
        return response

    @allure.step("Завершить заказ")
    def order_finish(self, order_id):
        response = requests.put(url=f"{Data.ORDERS_URL}/finish/{order_id}")
        return response

    @allure.step("Получить список заказов")
    def orders_get_list(self, filters=None):
        orders = []
        params = ""
        if filters is not None:
            for key, value in filters.items():
                params += "&" if len(params) > 0 else ""
                params += f"{key}={json.dumps(value)}"
        url = f"{Data.ORDERS_URL}?{params}" if len(params) > 0 else f"{Data.ORDERS_URL}"
        response = requests.get(url=url)
        if response.status_code == 200:
            orders = response.json()['orders']
        return orders, response
