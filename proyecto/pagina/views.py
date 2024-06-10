from django.shortcuts import render
from .models import Producto
# Create your views here.
def menuPrincipal(request):
    return render(request, 'menuPrincipal.html')

def Videojuegos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'Videojuegos.html', context)

def Accesorios(request):
    return render(request, 'Accesorios.html')

def Registro(request):
    return render(request, 'Registro.html')

def Contacto(request):
    return render(request, 'Contacto.html')

def Admin(request):
    return render(request, 'admin.html')

def carro(request):
    return render(request, 'carro.html')

