import requests

URL_LOGIN = 'http://localhost:5000/api/v1/login'

def loginRequest(email, password):
    payload = { email, password }
    response = requests.post(URL_LOGIN, json=payload)
    json = response.json()
    return json