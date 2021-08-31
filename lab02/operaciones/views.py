from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'titulo' : "Operaciones Aritmeticas :D",
    }
    return render(request, 'operaciones/formulario.html', context)

def enviar(request):

    op = request.POST.get('operation')
    num1 = int(request.POST.get('num1')) 
    num2 = int(request.POST.get('num2'))
    result = 0

    if op == "addition":
        result = num1 + num2
        op = "Suma"
    if op == "substraction":
        result = num1 - num2
        op = "Menos"
    if op == "multiplication":
        result = num1 * num2
        op = "Multiplicacion"
    if op == "division":
        result = num1 / num2
        op = "Division"

    context = {
        'titulo' : "Operaciones Aritmeticas :D",
        'num1' : num1,
        'num2' : num2,
        'op' : op,
        'result': result,
    }
    return render(request, 'operaciones/respuesta.html', context)