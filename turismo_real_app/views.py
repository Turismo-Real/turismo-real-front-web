from django.http import HttpResponse
from django.http.response import HttpResponseGone
from django.shortcuts import render


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
    # response = loginRequest(correo, passwd)
    
    print(correo)
    print(passwd)

    # if response['login']:
    #     tipo = response['tipo'].upper()
    #     if tipo == 'CLIENTE':
    #         return render(request, 'client.html')
    #     elif tipo == 'FUNCIONARIO':
    #         return render(request, 'funcionario.html')
    # return render(request, 'index.html')
    return render(request, 'index.html')
