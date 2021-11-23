from django.http import HttpResponse
from django.http.response import HttpResponseGone
from django.shortcuts import render
import requests

def index(request):
    return render(request, 'index.html')

def department_view(request):
    return render(request, 'department_view.html')

def department_reservation(request):
    return render(request, 'department_reservation.html')

def register_user(request):
    return render(request, 'register_user.html')

def cliente(request):
    return render(request, 'client.html')
    
def funcionario(request):
    return render(request, 'funcionario.html')

async def login(request):
    correo = request.POST['correo']
    passwd = request.POST['hashedPassword']
    response = login_request(correo, passwd)

    if response['login']:
        tipo = response['tipo'].upper()
        if tipo == 'CLIENTE':
            return render(request, 'client.html')
        elif tipo == 'FUNCIONARIO':
            return render(request, 'funcionario.html')
    return render(request, 'index.html')

# LLAMADAS A APIs
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