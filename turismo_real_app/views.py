from django.http import HttpResponse
from django.http.response import HttpResponseGone
from django.shortcuts import render, redirect
from turismo_real_services.login_service import login_request
from django.contrib import messages

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
def contact(request):
    return render(request, 'contact.html')
def login(request):
    correo = request.POST['correo']
    passwd = request.POST['hashedPassword']
    response = login_request(correo, passwd)

    if response['login']:
        tipo = response['tipo'].upper()
        if tipo == 'CLIENTE':
            messages.success(request, 'Logueado Correctamente')
            login_response = redirect('cliente')
        elif tipo == 'FUNCIONARIO':
            messages.success(request, 'Logueado Correctamente')
            login_response = redirect('funcionario')
        return login_response
    messages.error(request, "Usuario Incorrecto")
    return render(request, 'index.html')