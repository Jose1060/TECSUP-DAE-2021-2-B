from django.urls import path

from . import views

app_name = 'cilindro'

urlpatterns = [
    path('', views.index, name='index'),
    path('volumen', views.volumen, name='volumen')
]
