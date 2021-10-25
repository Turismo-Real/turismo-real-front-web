from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def department_view(request):
    return render(request, 'department_view.html')

def department_reservation(request):
    return render(request, 'department_reservation.html')

def register_user(request):
    return render(request, 'register_user.html')
