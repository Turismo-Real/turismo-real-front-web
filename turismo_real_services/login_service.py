import requests

def login_request(email, password):
    URL_LOGIN = 'http://localhost:5000/api/v1/login'
    _headers = { 'Content-Type': 'application/json' }
    payload = {
        'email': email, 
        'password': password 
    }
    response = requests.post(URL_LOGIN, json=payload, headers=_headers)
    json = response.json()
    return json