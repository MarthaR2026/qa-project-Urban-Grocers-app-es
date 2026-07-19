import requests
import configuration
import data

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json= user_body,
                         headers= data.headers)


def post_new_client_kit(kits_body, auth_token):
    current_header= data.headers.copy()
    current_header["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json = kits_body,
                         headers = current_header)
