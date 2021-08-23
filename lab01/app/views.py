from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Esta aplicacion te permite sumar, restar, multiplicar y dividir :D")

def sumar(request, num1, num2):
    respuesta = num1 + num2
    return HttpResponse("La respuesta de la suma de %s + %s = %s" % (num1, num2, respuesta))

def restar(request, num1, num2):
    respuesta = num1 - num2
    return HttpResponse("La respuesta de la resta de %s - %s = %s" % (num1, num2, respuesta))

def dividir(request, num1, num2):
    respuesta = num1 / num2
    return HttpResponse("La respuesta de la division de %s / %s = %s" % (num1, num2, respuesta))

def multiplicar(request, num1, num2):
    respuesta = num1 * num2
    return HttpResponse("La respuesta de la multiplicacion de %s * %s = %s" % (num1, num2, respuesta))