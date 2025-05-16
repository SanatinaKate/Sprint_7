import pytest
from data import Data
from methods.courier_methods import CourierMethods
from methods.orders_methods import OrdersMethods


# Фикстура для создания куоьера
@pytest.fixture
def courier_prepare_1():
    courier_methods = CourierMethods()
    courier_data, _ = courier_methods.courier_create(raise_error=True)
    del courier_data['firstName']
    return courier_data

# Фикстура для создания и авторизации/удаления курьера
@pytest.fixture
def courier_prepare_2():
    courier_methods = CourierMethods()
    courier_data, _ = courier_methods.courier_create(raise_error=True)
    del courier_data['firstName']
    courier_id, _ = courier_methods.courier_login(data=courier_data, raise_error=True)
    yield courier_id
    courier_methods.courier_delete(courier_id=courier_id)

# Фикстура для создания/завершения заказов
@pytest.fixture
def orders_prepare():
    orders_id = []
    orders_methods = OrdersMethods()
    for order_data in Data.ORDERS_LIST:
            track, _ = orders_methods.order_create(data=order_data, raise_error=True)
            order_id, _ = orders_methods.order_get_id(track=track, raise_error=True)
            orders_id.append(order_id)
    yield orders_id
    for order_id in orders_id:
        orders_methods.order_finish(order_id=order_id)
