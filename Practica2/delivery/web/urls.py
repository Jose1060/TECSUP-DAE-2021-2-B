from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('plato/<int:plato_id>',views.plato,name='plato'),
    path('categoria/<int:categoria_id>',views.categoria,name='categoria'),

    
    path('agregarCarrito/<int:plato_id>',views.agregarCarrito,name='agregarCarrito'),
    path('carrito',views.carrito,name='carrito'),
    path('eliminarPlatoCarrito/<int:plato_id>',views.eliminarPlatoCarrito,name="eliminarPlatoCarrito"),
    path('limpiarCarrito',views.limpiarCarrito,name='limpiarCarrito')

]