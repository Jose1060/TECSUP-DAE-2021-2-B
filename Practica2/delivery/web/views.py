from django.shortcuts import render,get_object_or_404
from . models import Categoria, Plato
from web.carrito import Cart

# Create your views here.
def index(request):
    plato_list = Plato.objects.order_by('nombre')[:6]
    categorias = Categoria.objects.all()
    return render(request,'index.html', {'plato_list':plato_list,
        'categorias':categorias})

def plato(request,plato_id):
    meal = get_object_or_404(Plato, pk=plato_id)
    categorias = Categoria.objects.all()
    return render(request,'detalle.html',{'categorias':categorias, 'plato':meal})

def categoria(request,categoria_id):
    categorias = Categoria.objects.all()
    cate = get_object_or_404(Categoria, pk=categoria_id)
    platos = Plato.objects.filter(categoria_id=categoria_id)
    return render(request,'categoria.html',{'categorias':categorias, 'platos': platos, 'categoria' : cate})


def agregarCarrito(request,plato_id):
    objPlato = Plato.objects.get(id=plato_id)
    carritoPlato = Cart(request)
    print(objPlato)
    carritoPlato.add(objPlato,1)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def eliminarPlatoCarrito(request,plato_id):
    objPlato = Plato.objects.get(id=plato_id)
    carritoPlato = Cart(request)
    carritoPlato.remove(objPlato)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def limpiarCarrito(request):
    CarritoPlato = Cart(request)
    CarritoPlato.clear()
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def carrito(request):
    print(request.session.get("cart"))
    return render(request,'carrito.html')
