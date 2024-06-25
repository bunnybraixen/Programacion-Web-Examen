from django.urls import path
from . import views


urlpatterns = [    
    path('admin', views.admin, name='admin'), 
    path('adminCategoria', views.adminCategoria, name='adminCategoria'), 
    path('adminConsolas', views.adminConsolas, name='adminConsolas'), 
    path('adminPago', views.adminPago, name='adminPago'), 
    path('adminUsuario', views.adminUsuario, name='adminUsuario'), 
    path('menuPrincipal', views.menuPrincipal, name='menuPrincipal'), 
    path('Videojuegos', views.Videojuegos, name='Videojuegos'), 
    path('Accesorios', views.Accesorios, name='Accesorios'), 
    path('Registro', views.Registro, name='Registro'), 
    path('Login', views.Login, name='Login'), 
    path('Contacto', views.Contacto, name='Contacto'), 
    path('carro', views.carro, name='carro'),
    path('carro <str:pk>', views.eliminarCarro, name='eliminarCarro'), 
    path('eliminarProducto <str:pk>', views.eliminarProducto, name='eliminarProducto'), 
    path('eliminarPago <str:pk>', views.eliminarPago, name='eliminarPago'),
    path('eliminarConsola <str:pk>', views.eliminarConsola, name='eliminarConsola'),
    path('eliminarCategoria <str:pk>', views.eliminarCategoria, name='eliminarCategoria'),
    path('eliminarTipoUsuario <str:pk>', views.eliminarTipoUsuario, name='eliminarTipoUsuario'),
    path('buscarProducto <str:pk>', views.buscarProducto, name='buscarProducto'),
    path('buscarPago <str:pk>', views.buscarPago, name='buscarPago'),
    path('buscarConsola <str:pk>', views.buscarConsola, name='buscarConsola'),
    path('buscarCategoria <str:pk>', views.buscarCategoria, name='buscarCategoria'),
    path('buscarTipoUsuario <str:pk>', views.buscarTipoUsuario, name='buscarTipoUsuario'),
    path('eliminarUsuario <str:pk>', views.eliminarUsuario, name='eliminarUsuario'), 
    path('buscarUsuario <str:pk>', views.buscarUsuario, name='buscarUsuario'),
    path('busqueda', views.busqueda, name='busqueda'),
    path('busquedaCarro', views.busquedaCarro, name='busquedaCarro'),
    path('eliminarCarroTodo', views.eliminarCarroTodo, name='eliminarCarroTodo'),
    path('producto <str:pk>', views.producto, name='producto')
    ]