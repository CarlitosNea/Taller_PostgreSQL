from django.db import models

# Create your models here.

class Mascotas(models.Model):
    codigo=models.TextField(max_length=5)
    nombre=models.TextField(max_length=20)
    animal=models.TextField(max_length=20)
    raza=models.TextField(max_length=20)
    genero=models.TextField(max_length=20)
    color=models.TextField(max_length=20)
    edad = models.DecimalField(max_digits=2, decimal_places=1)
    nombre_dueno=models.TextField(max_length=20)
    telefono=models.TextField(max_length=10)
    correo=models.EmailField(max_length=254)
    
    
    
    
