from django.template import Template, Context
from django.shortcuts import render
from django.http import HttpResponse as HR
from App5.models import *


#Metodo para mostrar todos los datos
def mostrarP(request):
    plantilla=open("C:/Users/ljavi/OneDrive/Desktop/Carlos/PYTHON/DJANGO/TallerPSQL/Proyecto5/Proyecto5/plantillas/index.html")
    template=Template(plantilla.read())
    plantilla.close()
    listar=Profesores.objects.all()
    context=Context({"listar":listar})
    documento=template.render(context)
    return HR(documento)