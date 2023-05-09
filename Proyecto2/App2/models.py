from django.db import models

# Create your models here.

class Productos(models.Model):
    codigo=models.TextField(max_length=10)
    nombre=models.TextField(max_length=20)
    categoria=models.TextField(max_length=20)
    color=models.TextField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor=models.TextField(max_length=20)
    telefono_prov=models.TextField(max_length=20)
    fecha_llegada=models.DateField()
    fecha_vencimiento=models.DateField()
    
