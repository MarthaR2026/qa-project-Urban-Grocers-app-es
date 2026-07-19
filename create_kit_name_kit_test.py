import data
import sender_stand_request

def get_kit_body(kit_name):
    current_kit_body =data.kits_body.copy()
    current_kit_body["name"] = kit_name
    return current_kit_body

def get_new_user_token():
    response_token = sender_stand_request.post_new_user(data.user_body)
    return response_token.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body,get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

def test_1_kith_name_with_1_letter():
    new_kit_body = get_kit_body ("A")
    positive_assert(new_kit_body)

def test_2_kit_name_with_511_letter():
    new_kit_body = get_kit_body ("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(new_kit_body)

def test_3_kit_name_0_letter():
    new_kit_body = get_kit_body ("")
    negative_assert_code_400(new_kit_body)

def test_4_kit_name_512_letter():
    new_kit_body = get_kit_body ("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(new_kit_body)

def test_5_kit_name_special_letter():
    new_kit_body = get_kit_body ("\"№%@\",\"" )
    positive_assert(new_kit_body)

def test_6_kit_name_with_space():
    new_kit_body = get_kit_body ("A Aaa")
    positive_assert(new_kit_body)

def test_7_kit_name_with_numbers():
    new_kit_body = get_kit_body ("123")
    positive_assert(new_kit_body)

def test_8_no_name_on_request():
    new_kit_body =  data.kits_body.copy()
    new_kit_body.pop("name")
    negative_assert_code_400(new_kit_body)

def test_9_kit_name_with_number_type():
    new_kit_body = get_kit_body (123)
    negative_assert_code_400(new_kit_body)
