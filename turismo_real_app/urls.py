from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('vista departamento', views.department_view, name='department_view'),
    path('vista reserva', views.department_reservation, name='department_reservation'),
    path('cancelar reserva', views.cancerlar_reserva, name='cancerlar_reserva'),
    path('vista registro usuario', views.register_user, name='register_user'),
    path('modificar usuario', views.modificar_usuario, name='modificar_usuario'),
    path('cliente', views.cliente, name='cliente'),
    path('funcionario', views.funcionario, name='funcionario'),
    path('Estado Departamento', views.funcionario_estado, name='funcionario_estado'),
    path('checkin', views.funcionario_checkin, name='funcionario_checkin'),
    path('contacto', views.contact, name='contact'),
    path('login', views.login, name='login'),
]