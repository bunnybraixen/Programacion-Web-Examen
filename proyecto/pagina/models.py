from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre      = models.CharField(max_length=40, unique=True)
    categoria   = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    descripcion  = models.CharField(max_length=500)
    consola   = models.CharField(max_length=50)
    precio   = models.CharField(max_length=50)
    stock      = models.IntegerField()
    
    def __str__(self):
        return self.nombre
# Create your models here.
class Accesorios(models.Model):
    nombre      = models.CharField(max_length=10, unique=True)
    categoria   = models.CharField(max_length=30)
    descripcion  = models.CharField(max_length=500)
    consola   = models.CharField(max_length=50)
    precio   = models.CharField(max_length=50)
    stock      = models.IntegerField()

class Carro(models.Model):
    nombre      = models.CharField(max_length=10, unique=True)
    categoria   = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    descripcion  = models.CharField(max_length=500)
    consola   = models.CharField(max_length=50)
    precio   = models.CharField(max_length=50)
    stock      = models.IntegerField()
    def __str__(self):
        return self.nombre
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre