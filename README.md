## Автотест для тестирования API приложения Яндекс Самокат

### Тест проверяет, что по треку заказа можно получить данные о заказе

### Для создания заказа отправляется запрос: 
#### POST _url/api/v1/orders_
### Для получения информации о заказе отправляется запрос:
#### GET _url/api/v1/orders/track?t=******* (вместо звёздочек номер заказа)
Подробно с документацией по API приложения Яндекс Самокат можно ознакомиться, введя в адресную строку браузера  адрес _url/docs/_
### Для запуска автотестов необходимо:
#### 1. Запустить сервер и получить ссылку на приложение Яндекс Самокат
#### 2. Установить в PyCharm пакеты: requests и pytest