from django.shortcuts import render
from .models import Producto, Categoria, Carro
# Create your views here.
def menuPrincipal(request):
    return render(request, 'menuPrincipal.html')

def Videojuegos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    if request.method == 'POST':
        print('HOLA')
        nombre = request.POST['txtNombre1']
        consola = request.POST['txtConsola1']
        precio = request.POST['txtPrecio1']

        if 'btnGuardar' in request.POST:
            Carro.objects.create(
                                    nombre=nombre,
                                    consola=consola,
                                    precio=precio)

            context['exito'] = "Se ha añadido al carrito!"
    
    return render(request, 'Videojuegos.html', context)

def Accesorios(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'Accesorios.html', context)


def admin(request):
    context = {}
    context['productos'] = Producto.objects.all()
    context['categoria'] = Categoria.objects.all()
    if request.method == 'POST':
        context['exito'] = "Hola!"
        print('HOLA')
        id = request.POST['txtId']
        idCategoria =  request.POST['cmbCategoria']
        nombre = request.POST['txtNombre']
        descripcion = request.POST['txtDescripcion']
        consola = request.POST['txtConsola']
        precio = request.POST['txtPrecio']
        stock = request.POST['txtStock']
        
            
        if 'btnGuardar' in request.POST:
            categoria = Categoria.objects.get(pk=idCategoria) # buscar obj según id seleccionado
            if id== "0":
                
                Producto.objects.create(
                                        nombre=nombre,
                                        categoria=categoria,
                                        descripcion=descripcion,
                                        consola=consola,
                                        precio=precio,
                                        stock=stock)

                context['exito'] = "Los datos fueron guardados"
            else:
                item=Producto()
                item.id = id
                item.nombre = nombre
                item.categoria = categoria
                item.descripcion = descripcion
                item.consola = consola
                item.precio = precio
                item.stock = stock
                item.save()
                context['exito'] = "Se edito correctamente"
    
    return render(request, 'admin.html', context)


def Registro(request):
    return render(request, 'Registro.html')

def Contacto(request):
    return render(request, 'Contacto.html')



def carro(request):
    carro = Carro.objects.all()
    context = {'carro': carro}
    return render(request, 'carro.html', context)


def eliminarCarro(request, pk):
    carro = Carro.objects.all()
    context = {'carro': carro}
    try:
        item = Carro.objects.get(pk = pk)
        item.delete()
        context['exito'] = "El item fue eliminado"
    except:
        context['error'] = "El item NO fue eliminado"

    context['listado'] = Carro.objects.all()
    return render(request, 'carro.html', context)

def buscarProducto(request, pk):
    context = {}
    context['productos'] = Producto.objects.all()
    context['categoria'] = Categoria.objects.all()
    try:
        context['categorias2'] = Categoria.objects.all()
        context['item'] = Producto.objects.get(pk = pk)
    except:
        context['error'] = 'Error al buscar el registro'

    return render(request, 'admin.html', context)

def eliminarProducto(request, pk):
    productos = Producto.objects.all()
    context = {'producto': productos}
    try:
        item = Producto.objects.get(pk = pk)
        item.delete()
        context['exito'] = "El item fue eliminado"
    except:
        context['error'] = "El item NO fue eliminado"

    context['productos'] = Producto.objects.all()
    return render(request, 'admin.html', context)