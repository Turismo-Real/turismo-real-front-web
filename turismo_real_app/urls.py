from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vista departamento', views.department_view, name='department_view')
]