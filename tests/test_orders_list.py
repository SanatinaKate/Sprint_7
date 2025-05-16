import allure
import pytest
from methods.orders_methods import OrdersMethods


class TestOrdersList:

    @allure.title("Проверка получения списка заказов без привязки к курьеру")
    @pytest.mark.parametrize("filters", [
        {},
        {'nearestStation': ['10', '20', '30']},
        {'limit': 2},
        {'page': 0},
        {'nearestStation': ['10', '20', '30'], 'limit': 2},
        {'nearestStation': ['10', '20', '30'], 'page': 0},
        {'limit': 2, 'page': 1},
        {'nearestStation': ['10', '20', '30'], 'limit': 2, 'page': 1}
    ])
    def test_orders_list_check_request_without_courier(self, orders_prepare, filters):
        orders_methods = OrdersMethods()
        orders, response = orders_methods.orders_get_list(filters=filters)
        assert (response.status_code == 200) and \
               ('{"orders":' in response.text) and \
               (len(orders) > 0), \
               f"status_code = {response.status_code}, text = {response.text}"

    @allure.title("Проверка получения списка заказов c привязкой к курьеру")
    @pytest.mark.parametrize("filters", [
        {},
        {'nearestStation': ['10', '20', '30']},
        {'limit': 2},
        {'page': 0},
        {'nearestStation': ['10', '20', '30'], 'limit': 2},
        {'nearestStation': ['10', '20', '30'], 'page': 0},
        {'limit': 2, 'page': 1},
        {'nearestStation': ['10', '20', '30'], 'limit': 2, 'page': 1}
    ])
    def test_orders_list_check_request_with_courier(self, courier_prepare_2, orders_prepare, filters):
        filters['courierId'] = courier_prepare_2
        orders_methods = OrdersMethods()
        for order_id in orders_prepare:
            orders_methods.order_accept(order_id=order_id, courier_id=courier_prepare_2, raise_error=True)
        orders, response = orders_methods.orders_get_list(filters=filters)
        assert (response.status_code == 200) and \
               ('{"orders":' in response.text) and \
               (len(orders) > 0), \
               f"status_code = {response.status_code}, text = {response.text}"
