import configuration
import requests
import data
import sender_stand_request


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"]="Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,  # подставляем полный url
                         json=kit_body,  # тут тело
                         headers=headers) # а здесь заголовки


