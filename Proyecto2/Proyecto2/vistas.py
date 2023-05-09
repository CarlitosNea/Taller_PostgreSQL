from django.template import Template, Context
from django.shortcuts import render
from django.http import HttpResponse as HR
from App2.models import Productos


#Metodo para mostrar todos los datos
def mostrarP(request):
    plantilla=open("C:/Users/ljavi/OneDrive/Desktop/Carlos/PYTHON/DJANGO/TallerPSQL/Proyecto2/Proyecto2/plantillas/index.html")
    template=Template(plantilla.read())
    plantilla.close()
    listar=Productos.objects.all()
    context=Context({"listar":listar})
    documento=template.render(context)
    return HR(documento)