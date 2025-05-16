Проект содержит автотесты для API сервиса "Яндекс.Самокат"
Документация API доступна по ссылке: https://qa-scooter.praktikum-services.ru/docs

Автотесты написаны с использованием библиотеки requests и фреймворка pytest
Сами автотесты находятся в директори tests и состоят из следующих файлов:
- test_courier_create.py - содержит класс TestCourierCreate для проверки создания курьера
  - test_courier_create_check_response_positive - проверка возвращаемого кода ответа и текста при успешном создании курьера
  - test_courier_create_for_two_equal_couriers - проверка невозможжости создания двух одинаковых курьеров
  - test_courier_create_for_existing_login - проверка невозможжости создания курьера с существующим логином
  - test_courier_create_for_incomplete_data - проверка невозможности создания курьера без передачи всех обязателных полей

- test_courier_login.py - содержит класс TestCourierLogin для проверки авторизации курьера
  - test_courier_login_check_response_positive - проверка возвращаемого кода ответа и идентификатора при успешной авторизации курьера
  - test_courier_login_for_incomplete_data - проверка невозможности авторизации курьера без передачи всех обязательных полей
  - test_courier_login_for_invalid_data - проверка невозможности авторизации курьера с невалидными/несушествующими данными

- test_order_create.py - содержит класс TestOrderCreate для проверки создания заказв
  - test_order_create_check_with_color - проверка возможности создания заказа с указанием цвета самоката
  - test_order_create_check_without_color - проверка возможности создания заказа без указания цвета самоката

- test_orders_list - содержит класс TestOrdersList для проверки получения списка заказов
  - test_orders_list_check_request_without_courier - проверка получения списка заказов без привязки к курьеру
  - test_orders_list_check_request_with_courier - проверка получения списка заказов c привязкой к курьеру

В директории methods находятся файлы с методами API для автотестов:
- courier_methods.py - содержит класс CourierMethods с методами для работы с курьером
- orders_methods.py - содержит класс OrdersMethods с методами для работы с заказами

В директории allure-report находится файл index.html с отчётом Allure о результатах запуска автотестов

Файл data.py содержит класс Data со статическими данными для автотестов
Файл helpers.py содержит класс Helpers со статическим методом генерации случайной строки
Файл conftest.py содержит pytest-фикстуры для создания/авторизации/удаления курьера и создания/завершения заказов
Файл requirements.txt содержит версии пакетов, необходимых для работы проекта
