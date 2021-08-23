from django.urls import path
from . import views

urlpatterns = [
    # ex: localhost:8080/app/
    path('', views.index, name='index'),
    # ex: localhost:8080/app/sumar/18/19
    path('sumar/<int:num1>/<int:num2>/', views.sumar, name='sumar'),
    # ex: localhost:8080/app/restar/18/19
    path('restar/<int:num1>/<int:num2>/', views.restar, name='restar'),
    # ex: localhost:8080/app/sumar/18/19
    path('multiplicar/<int:num1>/<int:num2>/', views.multiplicar, name='multiplicar'),
    # ex: localhost:8080/app/sumar/18/19
    path('dividir/<int:num1>/<int:num2>/', views.dividir, name='dividir'),


]