from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos', blank=True, null=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre
        
class Pedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos', blank=True, null=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre

class Pedido_Realizado(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    #usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)         Si tuvieramos nuestro modelo usuario 
    pub_date = models.DateTimeField('date published')
    nombre_usuario = models.CharField(max_length=200)                       # Por que no tenemos nuestro modelo usuario
