from django.urls import path
from . import views


urlpatterns = [    
    path('admin', views.admin, name='admin'), 
    path('menuPrincipal', views.menuPrincipal, name='menuPrincipal'), 
    path('Videojuegos', views.Videojuegos, name='Videojuegos'), 
    path('Accesorios', views.Accesorios, name='Accesorios'), 
    path('Registro', views.Registro, name='Registro'), 
    path('Contacto', views.Contacto, name='Contacto'), 
    path('carro', views.carro, name='carro'),
    path('carro <str:pk>', views.eliminarCarro, name='eliminarCarro'), 
    
    ]