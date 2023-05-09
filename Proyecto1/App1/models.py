from django.db import models

# Create your models here.

class Clientes(models.Model):
    documento=models.TextField(max_length=10)
    nombre=models.TextField(max_length=20)
    apellido=models.TextField(max_length=20)
    apodo=models.TextField(max_length=20)
    correo=models.EmailField(max_length=254)
    contrasena=models.TextField(max_length=20)
    genero=models.TextField(max_length=10)
    ciudad=models.TextField(max_length=20)
    telefono1=models.TextField(max_length=20)
    telefono2=models.TextField(max_length=20)
    
