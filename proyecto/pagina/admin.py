from django.contrib import admin
from .models import Producto, Accesorios, Categoria, Carro, Usuario

# Register your models here.
admin.site.register(Producto)
admin.site.register(Accesorios)
admin.site.register(Categoria)
admin.site.register(Carro)
admin.site.register(Usuario)