import configuration
import requests
import data

# Создание заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=data.order_body)

# Получение информации о заказе по трек-номеру
def get_orders_track(track_id):
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVING_ORDER_BY_ID + "?t=" + str(track_id))

