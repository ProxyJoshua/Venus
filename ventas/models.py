from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre=models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=200)
    descripcion=models.CharField(max_length=200, blank=True, null=True)
    imagen=models.ImageField(upload_to='ventas/productos',blank=True,null=True)
    valor=models.IntegerField()
    stock=models.IntegerField()
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.nombre

class Carro(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    total = models.IntegerField(default=0)
