from django.db import models
c1
# Create your models here.

from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    ingredientes = models.TextField(help_text='Redacta los intgredientes')
    preparacion = models.TextField()
    tiempo_registrado = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Autor,on_delete=CASCADE)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    receta = models.ForeignKey(Receta,on_delete=CASCADE)
    texto = models.TextField(help_text=u'tu comentario',verbose_name='Comentario')

    def __str__(self):
        return self.texto