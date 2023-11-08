import requests
import configuration
import sender_stand_request

#Создание заказа и получение трека
def create_order_and_get_track():
    response = sender_stand_request.post_creat_new_order()
    track_number = response.json()["track"]
    return track_number

#Получение заказа по номеру трекера
def get_order_by_track(track):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track}"
    response = requests.get(get_order_url)
    return response

#Тест
def test_order_creation_and_retrieval():
    track_number = create_order_and_get_track()
    print("Заказ создан. Номер трека:", track_number)
