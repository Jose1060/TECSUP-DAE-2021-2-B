from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Prestamos
from .serializers import PrestamoSerializer

# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({'message': 'Bienvenido a la API de la biblioteca'})

@api_view(['GET', 'POST'])
def prestamos(request):
    if request.method == 'GET':
        lstPrestamos = Prestamos.objects.all()
        serializer = PrestamoSerializer(lstPrestamos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PrestamoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def prestamosDetalle(request, id):
    try:
        prestamo = Prestamos.objects.get(id=id)
    except Prestamos.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = PrestamoSerializer(prestamo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PrestamoSerializer(prestamo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        prestamo.delete()
        return Response(status=204)