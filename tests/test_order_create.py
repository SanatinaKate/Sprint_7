import allure
import pytest
from data import Data
from methods.orders_methods import OrdersMethods


class TestOrderCreate:

    @allure.title("Проверка возможности создания заказа с указанием цвета самоката")
    @pytest.mark.parametrize("color", [[], ["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    def test_order_create_check_with_color(self, color):
        orders_methods = OrdersMethods()
        order_data = Data.ORDERS_LIST[0]
        order_data['color'] = color
        track, response = orders_methods.order_create(data=order_data)
        assert (response.status_code == 201) and \
               (response.text == f'{{"track":{track}}}'), \
               f"status_code = {response.status_code}, text = {response.text}"

    @allure.title("Проверка возможности создания заказа без указания цвета самоката")
    def test_order_create_check_without_color(self):
        orders_methods = OrdersMethods()
        order_data = Data.ORDERS_LIST[1]
        del order_data['color']
        track, response = orders_methods.order_create(data=order_data)
        assert (response.status_code == 201) and \
               (response.text == f'{{"track":{track}}}'), \
               f"status_code = {response.status_code}, text = {response.text}"
