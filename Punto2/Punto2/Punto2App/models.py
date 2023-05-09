from django.db import models

# Create your models here.


class Usuario(models.Model):
    documento=models.TextField(max_length=10)
    nombre_usu=models.TextField(max_length=50)
    clave=models.TextField(max_length=20)


class Cliente(models.Model):
    documento=models.TextField(max_length=10)
    nombre=models.TextField(max_length=20)
    apellido=models.TextField(max_length=20)
    correo=models.EmailField(max_length=254)
    telefono=models.TextField(max_length=20)
    direccion=models.TextField(max_length=20)
    genero=models.TextField(max_length=10)


class Lineas_de_credito(models.Model):
    codigo=models.TextField(max_length=10)
    nombre_credito=models.TextField(max_length=20)
    monto_maximo = models.DecimalField(max_digits=10, decimal_places=2)
    plazo_maximo=models.DateField()


class Creditos(models.Model):
    documento_cliente=models.TextField(max_length=10)
    cod_lineacredito=models.TextField(max_length=10)
    monto_prestado = models.DecimalField(max_digits=10, decimal_places=2)
    plazo=models.DateField()
    fecha_desembolso=models.DateField()


