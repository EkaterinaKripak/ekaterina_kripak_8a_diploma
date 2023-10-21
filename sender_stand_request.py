import configuration
import requests
import data

# создадим новый заказ в системе
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=data.order_body)
response = post_new_order()
print(response.status_code)
print(response.json())

# выведем параметр track из тела ответа при создании нового заказа
def post_track():
    track_number = post_new_order().json()["track"]
    return track_number
print(response.json()["track"])

def get_order_information(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO + str(track_number))

