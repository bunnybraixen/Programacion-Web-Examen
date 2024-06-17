from django.shortcuts import render
from .models import Producto, Categoria, Carro, Usuario
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
        imagen = request.POST['txtImagen1']
        if 'btnGuardar' in request.POST:
            Carro.objects.create(
                                    nombre=nombre,
                                    consola=consola,
                                    precio=precio,
                                    imagen=imagen)

            context['exito'] = "Se ha añadido al carrito!"
    
    return render(request, 'videojuegos.html', context)

def Accesorios(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    if request.method == 'POST':
        print('HOLA')
        nombre = request.POST['txtNombre1']
        consola = request.POST['txtConsola1']
        precio = request.POST['txtPrecio1']
        imagen = request.POST['txtImagen1']
        if 'btnGuardar' in request.POST:
            Carro.objects.create(
                                    nombre=nombre,
                                    consola=consola,
                                    precio=precio,
                                    imagen=imagen)

            context['exito'] = "Se ha añadido al carrito!"
    
    return render(request, 'accesorios.html', context)


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
        imagen = request.FILES['txtImagen']
        
            
        if 'btnGuardar' in request.POST:
            categoria = Categoria.objects.get(pk=idCategoria) # buscar obj según id seleccionado
            if id== "0":
                
                Producto.objects.create(
                                        nombre=nombre,
                                        categoria=categoria,
                                        descripcion=descripcion,
                                        consola=consola,
                                        precio=precio,
                                        stock=stock,
                                        imagen=imagen)

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
                item.imagen = imagen
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


def Registro(request):
    context = {}
    if request.method == 'POST':
        if 'btnGuardar' in request.POST:
            context['exito'] = "Hola!"
            print('HOLA')
            id = request.POST['txtId']
            nombre = request.POST['txtNombre']
            rut =  request.POST['txtRut']
            correo = request.POST['txtCorreo']
            telefono = request.POST['txtTelefono']
            nacimiento = request.POST['txtNacimiento']
            direccion = request.POST['txtDireccion']
            contraseña = request.POST['txtContraseña']
            region = request.POST['cmbRegion']
            imagen = request.FILES['txtImagen']
            if id== "0":
                
                Usuario.objects.create(
                                        nombre=nombre,
                                        rut=rut,
                                        correo=correo,
                                        telefono=telefono,
                                        nacimiento=nacimiento,
                                        direccion=direccion,
                                        contraseña=contraseña,
                                        region=region,
                                        imagen=imagen)

                context['exito'] = "La cuenta ha sido registrada"
            else:
                item=Usuario()
                item.id = id
                item.nombre = nombre
                item.rut = rut
                item.correo = correo
                item.telefono = telefono
                item.nacimiento = nacimiento
                item.direccion = direccion
                item.contraseña = contraseña
                item.region=region
                item.imagen=imagen
                item.save()
                context['exito'] = "Se edito correctamente"
    context['listado'] = Usuario.objects.all()
    return render(request, 'Registro.html', context)

def Login(request):
    context = {}
    if request.method == 'POST':
        
            
        if 'btnGuardar1' in request.POST:
                correo = request.POST['loginCorreo']
                contraseña = request.POST['loginClave']
                try: 
                    categoria = Usuario.objects.get(correo=correo)
                    if categoria.correo == correo:
                        if categoria.contraseña == contraseña:
                            context['item'] = Usuario.objects.get(correo=correo)
                            context['exito'] = 'Ha ingresado con exito'
                            return render(request, 'login.html', context)
                        else:
                            context['error'] = 'La contraseña ingresada no coincide con la registrada'
                            return render(request, 'Registro.html', context)
                    else:
                        context['error'] = 'El usuario ingresado no coincide con ninguno en la base de datos'
                        return render(request, 'Registro.html', context)
                except:
                    context['error'] = 'El usuario ingresado no coincide con ninguno en la base de datos'
                    context['listado'] = Usuario.objects.all()
                    return render(request, 'Registro.html', context)
    

def buscarUsuario(request, pk):
    context = {}
    try:
        context['item'] = Usuario.objects.get(pk=pk)
    except:
        context['error'] = 'Error al buscar el registro'
    context['id'] = pk    
    context['listado'] = Usuario.objects.all()
    return render(request, 'registro.html', context)

def eliminarUsuario(request, pk):
    context = {}
    try:
        item = Usuario.objects.get(pk = pk)
        item.delete()
        context['exito'] = "El item fue eliminado"
    except:
        context['error'] = "El item NO fue eliminado"

    context['listado'] = Usuario.objects.all()
    return render(request, 'registro.html', context)

def busqueda(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    context['nombre'] = request.POST['txtBusqueda']
    
    return render(request, 'busqueda.html', context)


def busquedaCarro(request):
    
    productos = Producto.objects.all()
    context = {'productos': productos}
    nombre = request.POST['txtNombre1']
    consola = request.POST['txtConsola1']
    precio = request.POST['txtPrecio1']
    imagen = request.POST['txtImagen1']
    Carro.objects.create(
                                    nombre=nombre,
                                    consola=consola,
                                    precio=precio,
                                    imagen=imagen)

    context['exito'] = "Se ha añadido al carrito!"
    carro = Carro.objects.all()
    context = {'carro': carro}
    return render(request, 'carro.html', context)