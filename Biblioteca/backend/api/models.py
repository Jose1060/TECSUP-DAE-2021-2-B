from django.db import models

# Create your models here.
'''
class Libro(models.Model):
    codigo = models.IntegerField()
    titulo = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=80)
    editorial = models.CharField(max_length=255)
    numPage = models.IntegerField()

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    numUsuario = models.IntegerField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    NIF = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
'''

class Prestamos(models.Model):
    libro = models.CharField(max_length=255)
    usuario = models.CharField(max_length=255)
    fecPrestamo = models.DateTimeField(auto_now=True)
    fecDevolucion = models.DateField(auto_now=False)

    def __str__(self):
        return self.usuario




