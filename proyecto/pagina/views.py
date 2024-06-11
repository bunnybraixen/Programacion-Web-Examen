from django.shortcuts import render
from .models import Producto, Categoria
# Create your views here.
def menuPrincipal(request):
    return render(request, 'menuPrincipal.html')

def Videojuegos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'Videojuegos.html', context)

def Accesorios(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'Accesorios.html', context)


def Admin(request):
    categorias = Categoria.objects.all()
    context = {'categoria': categorias}
    print('hola')

    if request.method == 'POST':
        print('HOLA')
        categoria =  request.POST['cmbCategoria']
        nombre = request.POST['txtNombre']
        descripcion = request.POST['txtDescripcion']
        consola = request.POST['txtConsola']
        precio = request.POST['txtPrecio']
        stock = request.POST['txtStock']


        if 'btnGuardar' in request.POST:
            categoria = categoria.objects.get(categoria= categoria) # buscar obj según id seleccionado
            Producto.objects.create(
                                    nombre=nombre,
                                    categoria=categoria,
                                    descripcion=descripcion,
                                    consola=consola,
                                    precio=precio,
                                    stock=stock)

            context['exito'] = "Los datos fueron guardados"

    return render(request, 'admin.html', context)

def Registro(request):
    return render(request, 'Registro.html')

def Contacto(request):
    return render(request, 'Contacto.html')



def carro(request):
    return render(request, 'carro.html')

