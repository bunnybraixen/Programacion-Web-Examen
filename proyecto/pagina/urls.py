from django.urls import path
from . import views


urlpatterns = [    
    path('admin', views.admin, name='admin'), 
    path('menuPrincipal', views.menuPrincipal, name='menuPrincipal'), 
    path('Videojuegos', views.Videojuegos, name='Videojuegos'), 
    path('Accesorios', views.Accesorios, name='Accesorios'), 
    path('Registro', views.Registro, name='Registro'), 
    path('Login', views.Login, name='Login'), 
    path('Contacto', views.Contacto, name='Contacto'), 
    path('carro', views.carro, name='carro'),
    path('carro <str:pk>', views.eliminarCarro, name='eliminarCarro'), 
    path('eliminarProducto <str:pk>', views.eliminarProducto, name='eliminarProducto'), 
    path('buscarProducto <str:pk>', views.buscarProducto, name='buscarProducto'),
    path('eliminarUsuario <str:pk>', views.eliminarUsuario, name='eliminarUsuario'), 
    path('buscarUsuario <str:pk>', views.buscarUsuario, name='buscarUsuario'),
    path('busqueda', views.busqueda, name='busqueda'),
    path('busquedaCarro', views.busquedaCarro, name='busquedaCarro'),
    path('eliminarCarroTodo', views.eliminarCarroTodo, name='eliminarCarroTodo'),
    path('producto <str:pk>', views.producto, name='producto')
    ]