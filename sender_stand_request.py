import requests
import configuration
import data

# Создание заказа
def post_creat_new_order():
    response = requests.post(configuration.URL_SERVICE + configuration.CREAT_ORDERS, json=data.order_body)
    return response