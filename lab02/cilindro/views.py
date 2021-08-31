from django.shortcuts import render
import math

# Create your views here.
def index(request):
    context = {
        'titulo' : "Volumen de un cilindro",
    }
    return render(request, 'cilindro/formulario.html', context)

def volumen(request):
    h = int(request.POST['h'])
    r = int(request.POST['r'])
    unidad = request.POST['unidad']

    vol = math.pi * r**2 * h

    titulo = "Volumen de un cilindro en " + unidad

    context = {
        'titulo' : titulo,
        'h' : h,
        'r' : r,
        'v' : vol,
        'unidad' : unidad,
    }
    return render(request, 'cilindro/respuesta.html', context)