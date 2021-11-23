import requests
from turismo_real_services.url_services import URL_LOGIN

def login_request(email, password):
    _headers = { 'Content-Type': 'application/json' }
    payload = {
        'email': email, 
        'password': password 
    }
    response = requests.post(URL_LOGIN, json=payload, headers=_headers)
    json = response.json()
    return json