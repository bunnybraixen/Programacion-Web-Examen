from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre      = models.CharField(max_length=10, unique=True)
    categoria   = models.CharField(max_length=30)
    descripcion  = models.CharField(max_length=500)
    consola   = models.CharField(max_length=50)
    precio   = models.CharField(max_length=50)
    stock      = models.IntegerField()

# Create your models here.
class Accesorios(models.Model):
    nombre      = models.CharField(max_length=10, unique=True)
    categoria   = models.CharField(max_length=30)
    descripcion  = models.CharField(max_length=500)
    consola   = models.CharField(max_length=50)
    precio   = models.CharField(max_length=50)
    stock      = models.IntegerField()