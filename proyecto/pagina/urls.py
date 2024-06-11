from django.urls import path
from . import views


urlpatterns = [    
    path('menuPrincipal', views.menuPrincipal, name='menuPrincipal'), 
    path('Videojuegos', views.Videojuegos, name='Videojuegos'), 
    path('Accesorios', views.Accesorios, name='Accesorios'), 
    path('Registro', views.Registro, name='Registro'), 
    path('Contacto', views.Contacto, name='Contacto'), 
    path('carro', views.carro, name='carro'), 
    path('Admin', views.Admin, name='Admin')
    ]