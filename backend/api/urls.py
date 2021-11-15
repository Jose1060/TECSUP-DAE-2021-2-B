from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prestamos', views.prestamos),
    path('prestamos/<int:id>', views.prestamosDetalle)
]