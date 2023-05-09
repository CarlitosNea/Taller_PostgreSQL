from django.db import models

# Create your models here.

class Estudiantes(models.Model):
    documento=models.TextField(max_length=10)
    nombre=models.TextField(max_length=20)
    apellido=models.TextField(max_length=20)
    edad = models.DecimalField(max_digits=3, decimal_places=1)
    correo=models.EmailField(max_length=254)
    contrasena=models.TextField(max_length=20)
    sede=models.TextField(max_length=20)
    carrera=models.TextField(max_length=20)
    materias = models.DecimalField(max_digits=3, decimal_places=1)
    promedio = models.DecimalField(max_digits=3, decimal_places=2)