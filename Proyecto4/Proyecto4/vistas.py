from django.template import Template, Context
from django.shortcuts import render
from django.http import HttpResponse as HR
from App4.models import *


#Metodo para mostrar todos los datos
def mostrarE(request):
    plantilla=open("C:/Users/ljavi/OneDrive/Desktop/Carlos/PYTHON/DJANGO/TallerPSQL/Proyecto4/Proyecto4/plantillas/index.html")
    template=Template(plantilla.read())
    plantilla.close()
    listar=Estudiantes.objects.all()
    context=Context({"listar":listar})
    documento=template.render(context)
    return HR(documento)