import sender_stand_request

# эта функция для позитивной проверки
def test_positive_assert():
    track_number = sender_stand_request.response.json()["track"]
    order_info_response = sender_stand_request.get_order_information(track_number)

    assert order_info_response.status_code == 200
