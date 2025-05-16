class Data:

    BASE_API_URL = "https://qa-scooter.praktikum-services.ru/api/v1"
    COURIER_URL = f"{BASE_API_URL}/courier"
    ORDERS_URL = f"{BASE_API_URL}/orders"

    CODE_2XX_TEXT= '{"ok":true}'
    CODE_400_TEXT_FOT_COURIER_CREATE = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
    CODE_409_TEXT_FOT_COURIER_CREATE = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    CODE_400_TEXT_FOT_COURIER_LOGIN = '{"code":400,"message":"Недостаточно данных для входа"}'
    CODE_404_TEXT_FOT_COURIER_LOGIN = '{"code":404,"message":"Учетная запись не найдена"}'
    CODE_504_TEXT = 'Service unavailable'

    ORDERS_LIST = [
        {
            "firstName": "Вася",
            "lastName": "Петров",
            "address": "г. Москва, возле станции метро",
            "metroStation": 10,
            "phone": "+79991234567",
            "rentTime": 3,
            "deliveryDate": "2025-05-15",
            "comment": "Позвонить перед доставкой"
        },
        {
            "firstName": "Петя",
            "lastName": "Васечкин",
            "address": "г. Москва, у метро",
            "metroStation": 20,
            "phone": "+79997654321",
            "rentTime": 2,
            "deliveryDate": "2025-05-16",
            "comment": "Уточнить детали встречи по телефону",
            "color": []
        },
        {
            "firstName": "Маша",
            "lastName": "Старцева",
            "address": "г. Москва",
            "metroStation": 30,
            "phone": "+79995555555",
            "rentTime": 1,
            "deliveryDate": "2025-05-17",
            "comment": "Буду ждать в 15:00 на выходе из метро",
            "color": ["BLACK", "GREY"]
        }
    ]
