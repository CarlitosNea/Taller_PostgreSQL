from django.template import Template, Context
from django.shortcuts import render
from django.http import HttpResponse as HR
from App3.models import *


#Metodo para mostrar todos los datos
def mostrarM(request):
    plantilla=open("C:/Users/ljavi/OneDrive/Desktop/Carlos/PYTHON/DJANGO/TallerPSQL/Proyecto3/Proyecto3/plantillas/index.html")
    template=Template(plantilla.read())
    plantilla.close()
    listar=Mascotas.objects.all()
    context=Context({"listar":listar})
    documento=template.render(context)
    return HR(documento)