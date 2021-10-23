from django.contrib import admin
from .models import Categoria
from .models import Plato

# Register your models here.


admin.site.register(Categoria)
admin.site.register(Plato)

class PlatoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'nombre', 'precio', 'stock')