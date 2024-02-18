Юрченко Виктория, 13 поток. Диплом,  Инженер по тестированию плюс
import request
import data

def test_getOrderInfoByTrack():
    track = request.create_order(data.order_body).json()['track']
    response = request.get_order_info_by_track(track)
    assert response.status_code == 200
