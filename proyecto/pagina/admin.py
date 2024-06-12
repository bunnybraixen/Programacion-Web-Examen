from django.contrib import admin
from .models import Producto, Accesorios, Categoria, Carro

# Register your models here.
admin.site.register(Producto)
admin.site.register(Accesorios)
admin.site.register(Categoria)
admin.site.register(Carro)