from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('vista departamento', views.department_view, name='department_view'),
    path('vista reserva', views.department_reservation, name='department_reservation'),
    path('vista registro usuario', views.register_user, name='register_user'),
]