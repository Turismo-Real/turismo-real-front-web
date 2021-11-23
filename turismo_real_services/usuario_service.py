import requests
from turismo_real_services.url_services import URL_USUARIO

_headers = { 'Content-Type': 'application/json' }

def nuevo_usuario(usuario):
    response = requests.post(URL_USUARIO, json=usuario, headers=_headers)
    json = response.json()
    return json