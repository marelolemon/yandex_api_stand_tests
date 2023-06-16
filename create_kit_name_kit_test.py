import sender_stand_request
import data


def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body



def positive_assert(name):
    response = sender_stand_request.post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name



def negative_assert(name):
    response = sender_stand_request.post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400
    assert response.json()["code"] == 400



def negative_assert_no_data(kit_body):
    response = sender_stand_request.post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400
    assert response.json()["code"] == 400



# Тест №1: Создание набора с допустимым количеством символов (1)
def test_1_create_kit_1_letter_success():
    positive_assert("a")

# Тест №2: Создание набора с допустимым количеством символов (511)
def test_2_create_kit_511_success():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabC")



# Тест №3: Создание набора с недопустимым количеством символов (0)
def test_3_create_kit_0_failed():
    negative_assert("")



# Тест №4: Создание набора с недопустимым количеством символов (512)
def test_4_create_kit_512_failed():
    negative_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")



# Тест №5: Создание набора с английкими буквами в поле "Имя"
def test_5_create_kit_english_success():
    positive_assert("QWErty")



# Тест №6:Создание набора с русскими буквами в поле "Имя"
def test_6_create_kit_rus_success():
    positive_assert("Мария")



# Тест №7: Создание набора со спецсимволами в поле "Имя"
def test_7_create_kit_symbol_success():
    positive_assert("\"№%@\",")



# Тест №8: Создание набора с пробелами в поле "Имя"
def test_8_create_kit_space_success():
    positive_assert("Человек и КО")



# Тест №9: Создание набора с цифрами в поле "Имя"
def test_9_create_kit_numbers_success():
    positive_assert("123")



# Тест №10: Создание набора, когда параметр не передан в запросе
def test_10_create_kit_no_name_failed():
    response = sender_stand_request.post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    kit_body = {}
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)  # передаем информацию на сервер
    assert kit_response.status_code == 400



# Тест №11: Создание набора передан другой тип параметра (число)
def test_11_create_kit_wrong_type_failed():
    negative_assert(123)
