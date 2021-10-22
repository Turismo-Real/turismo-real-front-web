from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def department_view(request):
    return render(request, 'department_view.html')
