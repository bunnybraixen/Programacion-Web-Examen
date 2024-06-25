from django.shortcuts import render
from .models import Producto, Categoria, Carro, Usuario, TipoUsuario, FormaPago, Consola, UsuarioActual
# Create your views here.
def menuPrincipal(request):
    context={}
    context['cuenta'] = UsuarioActual.objects.all()
    context['cuentas'] = Usuario.objects.all()
    return render(request, 'menuPrincipal.html', context)

def Videojuegos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    if request.method == 'POST':
        print('HOLA')
        id = request.POST['txtId1']
        nombre = request.POST['txtNombre1']
        consola = request.POST['txtConsola1']
        precio = request.POST['txtPrecio1']
        imagen = request.POST['txtImagen1']
        item = Producto.objects.get(pk = id)
        item.stock = item.stock - 1
        item.save()
        if 'btnGuardar' in request.POST:
            Carro.objects.create(
                                    id2=id,
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
        id = request.POST['txtId1']
        nombre = request.POST['txtNombre1']
        consola = request.POST['txtConsola1']
        precio = request.POST['txtPrecio1']
        imagen = request.POST['txtImagen1']
        item = Producto.objects.get(pk = id)
        item.stock = item.stock - 1
        item.save()
        if 'btnGuardar' in request.POST:
            Carro.objects.create(
                                    id2=id,
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
    context['consola'] = Consola.objects.all()
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
        imagen1 = request.POST['txtImagen1']
        try: 
            imagen = request.FILES['txtImagen']
        except:
            imagen = ""
        
        
            
        if 'btnGuardar' in request.POST:
            consola = Consola.objects.get(nombre=consola) # buscar obj según id seleccionado
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
                if imagen == "":
                    item.imagen = imagen1
                else:
                    item.imagen = imagen
                item.save()
                context['exito'] = "Se edito correctamente"
    
    return render(request, 'admin.html', context)


def Registro(request):
    context = {}
    context['tipoUsuario'] = TipoUsuario.objects.all()
    return render(request, 'Registro.html', context)

def Contacto(request):
    return render(request, 'Contacto.html')



def carro(request):
    carro = Carro.objects.all()
    context = {'carro': carro}
    context['pago'] = FormaPago.objects.all()
    return render(request, 'carro.html', context)


def eliminarCarro(request, pk):
    carro = Carro.objects.all()
    context = {'carro': carro}
    context['pago'] = FormaPago.objects.all()
    try:
        item = Carro.objects.get(pk = pk)
        item.delete()
        id = item.id2
        item = Producto.objects.get(pk = id)
        item.stock = item.stock + 1
        item.save()
        context['exito'] = "El item fue eliminado"
    except:
        context['error'] = "El item NO fue eliminado"

    context['listado'] = Carro.objects.all()
    return render(request, 'carro.html', context)

def buscarProducto(request, pk):
    context = {}
    context['consola'] = Consola.objects.all()
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
    context['consola'] = Consola.objects.all()
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
    context['tipoUsuario'] = TipoUsuario.objects.all()
    for x in UsuarioActual.objects.all().iterator():
        x.delete()
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
            tipoUsuario = request.POST['txtTipo']
            imagen1 = request.POST['txtImagen1']
            try: 
                imagen = request.FILES['txtImagen']
            except:
                imagen = ""
            tipoUsuario = TipoUsuario.objects.get(nombre=tipoUsuario) # buscar obj según id seleccionado
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
                                        imagen=imagen,
                                        tipoUsuario=tipoUsuario)

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
                item.tipoUsuario=tipoUsuario
                if imagen == "":
                    item.imagen = imagen1
                else:
                    item.imagen = imagen
                item.save()
                context['exito'] = "Se edito correctamente"
    context['listado'] = Usuario.objects.all()
    return render(request, 'Registro.html', context)

def Login(request):
    context = {}
    context['tipoUsuario'] = TipoUsuario.objects.all()
    context['cuenta'] = UsuarioActual.objects.all()
    if request.method == 'POST':
        
            
        if 'btnGuardar1' in request.POST:
                correo = request.POST['loginCorreo']
                contraseña = request.POST['loginClave']
                categoria = Usuario.objects.get(correo=correo)
                if categoria.correo == correo:
                        if categoria.contraseña == contraseña:
                            
                            context['exito'] = 'Ha ingresado con exito'
                            correo = request.POST['loginCorreo']
                            context['item'] = Usuario.objects.get(correo=correo)
                            UsuarioActual.objects.create(
                                        correo=correo)
                            return render(request, 'login.html', context)
    

def buscarUsuario(request, pk):
    context = {}
    context['tipoUsuario'] = TipoUsuario.objects.all()
    try:
        context['item'] = Usuario.objects.get(pk=pk)
    except:
        context['error'] = 'Error al buscar el registro'
    context['id'] = pk    
    context['listado'] = Usuario.objects.all()
    return render(request, 'registro.html', context)

def eliminarUsuario(request, pk):
    context = {}
    context['tipoUsuario'] = TipoUsuario.objects.all()
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
    context['pago'] = FormaPago.objects.all()
    id = request.POST['txtId1']
    nombre = request.POST['txtNombre1']
    consola = request.POST['txtConsola1']
    precio = request.POST['txtPrecio1']
    imagen = request.POST['txtImagen1']
    item = Producto.objects.get(pk = id)
    item.stock = item.stock - 1
    item.save()
    Carro.objects.create(
                                    id2=id,
                                    nombre=nombre,
                                    consola=consola,
                                    precio=precio,
                                    imagen=imagen)

    
    carro = Carro.objects.all()
    context = {'carro': carro}
    return render(request, 'carro.html', context)


def eliminarCarroTodo(request):
    for x in Carro.objects.all().iterator():
        x.delete()
    context = {'carro': carro}
    context['pago'] = FormaPago.objects.all()
    context['exito'] = "La compra se ha hecho con exito!"
    
    context['listado'] = Carro.objects.all()
    return render(request, 'carro.html', context)

def producto(request, pk):
    context = {}
    
    if request.method == 'POST':
        print('HOLA')
        item = Producto.objects.get(pk = pk)
        id = item.id
        nombre = item.nombre
        consola = item.consola
        precio = item.precio
        imagen = item.imagen
        item = Producto.objects.get(pk = id)
        item.stock = item.stock - 1
        item.save()
        if 'btnGuardar' in request.POST:
            
            Carro.objects.create(
                                    id2=id,
                                    nombre=nombre,
                                    consola=consola,
                                    precio=precio,
                                    imagen=imagen)

            context['exito'] = "Se ha añadido al carrito!"
    
    context['productos'] = Producto.objects.all()
    try:
        context['item'] = Producto.objects.get(pk = pk)
    except:
        context['error'] = 'Error al buscar el registro'
    return render(request, 'producto.html', context)



def adminCategoria(request):
    context = {}
    context['productos'] = Categoria.objects.all()
    if request.method == 'POST':
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        activo = request.POST['txtStock']
        if 'btnGuardar' in request.POST:
            if id== "0":
                Categoria.objects.create(
                                        nombre=nombre,
                                        activo=activo)

                context['exito'] = "Los datos fueron guardados"
            else:
                item=Categoria()
                item.id = id
                item.nombre = nombre
                item.activo = activo
                item.save()
                context['exito'] = "Se edito correctamente"
    
    return render(request, 'adminCategorias.html', context)
def adminConsolas(request):
    context = {}
    context['productos'] = Consola.objects.all()
    if request.method == 'POST':
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        activo = request.POST['txtStock']
        if 'btnGuardar' in request.POST:
            if id== "0":
                Consola.objects.create(
                                        nombre=nombre,
                                        activo=activo)

                context['exito'] = "Los datos fueron guardados"
            else:
                item=Consola()
                item.id = id
                item.nombre = nombre
                item.activo = activo
                item.save()
                context['exito'] = "Se edito correctamente"
    
    return render(request, 'adminConsolas.html', context)
def adminUsuario(request):
    context = {}
    context['productos'] = TipoUsuario.objects.all()
    if request.method == 'POST':
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        activo = request.POST['txtStock']
        if 'btnGuardar' in request.POST:
            if id== "0":
                TipoUsuario.objects.create(
                                        nombre=nombre,
                                        activo=activo)

                context['exito'] = "Los datos fueron guardados"
            else:
                item=TipoUsuario()
                item.id = id
                item.nombre = nombre
                item.activo = activo
                item.save()
                context['exito'] = "Se edito correctamente"
    
    return render(request, 'adminUsuario.html', context)
def adminPago(request):
    context = {}
    context['productos'] = FormaPago.objects.all()
    if request.method == 'POST':
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        activo = request.POST['txtStock']
        if 'btnGuardar' in request.POST:
            if id== "0":
                FormaPago.objects.create(
                                        nombre=nombre,
                                        activo=activo)

                context['exito'] = "Los datos fueron guardados"
            else:
                item=FormaPago()
                item.id = id
                item.nombre = nombre
                item.activo = activo
                item.save()
                context['exito'] = "Se edito correctamente"
    
    return render(request, 'adminPago.html', context)

def buscarPago(request, pk):
    context = {}
    context['productos'] = FormaPago.objects.all()
    try:
        context['item'] = FormaPago.objects.get(pk = pk)
    except:
        context['error'] = 'Error al buscar el registro'

    return render(request, 'adminPago.html', context)

def buscarConsola(request, pk):
    context = {}
    context['productos'] = Consola.objects.all()
    try:
        context['item'] = Consola.objects.get(pk = pk)
    except:
        context['error'] = 'Error al buscar el registro'

    return render(request, 'adminConsolas.html', context)

def buscarTipoUsuario(request, pk):
    context = {}
    context['productos'] = Usuario.objects.all()
    try:
        context['item'] = FormaPago.objects.get(pk = pk)
    except:
        context['error'] = 'Error al buscar el registro'

    return render(request, 'adminUsuario.html', context)

def buscarCategoria(request, pk):
    context = {}
    context['productos'] = FormaPago.objects.all()
    try:
        context['item'] = FormaPago.objects.get(pk = pk)
    except:
        context['error'] = 'Error al buscar el registro'

    return render(request, 'adminCategorias.html', context)

def eliminarCategoria(request, pk):
    context = {}
    try:
        item = Categoria.objects.get(pk = pk)
        item.delete()
        context['exito'] = "El item fue eliminado"
    except:
        context['error'] = "El item NO fue eliminado"

    context['productos'] = Categoria.objects.all()
    return render(request, 'adminCategorias.html', context)
def eliminarConsola(request, pk):
    context = {}
    try:
        item = Consola.objects.get(pk = pk)
        item.delete()
        context['exito'] = "El item fue eliminado"
    except:
        context['error'] = "El item NO fue eliminado"

    context['productos'] = Consola.objects.all()
    return render(request, 'adminConsolas.html', context)
def eliminarPago(request, pk):
    context = {}
    try:
        item = FormaPago.objects.get(pk = pk)
        item.delete()
        context['exito'] = "El item fue eliminado"
    except:
        context['error'] = "El item NO fue eliminado"

    context['productos'] = FormaPago.objects.all()
    return render(request, 'adminPago.html', context)
def eliminarTipoUsuario(request, pk):
    context = {}
    try:
        item = TipoUsuario.objects.get(pk = pk)
        item.delete()
        context['exito'] = "El item fue eliminado"
    except:
        context['error'] = "El item NO fue eliminado"

    context['productos'] = TipoUsuario.objects.all()
    return render(request, 'adminUsuario.html', context)