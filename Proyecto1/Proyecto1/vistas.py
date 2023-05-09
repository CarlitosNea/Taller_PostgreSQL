from django.template import Template, Context
from django.shortcuts import render
from django.http import HttpResponse as HR
from App1.models import Clientes


#Metodo para mostrar todos los datos
def mostrarC(request):
    plantilla=open("C:/Users/ljavi/OneDrive/Desktop/Carlos/PYTHON/DJANGO/TallerPSQL/Proyecto1/Proyecto1/plantillas/index.html")
    template=Template(plantilla.read())
    plantilla.close()
    listar=Clientes.objects.all()
    context=Context({"listar":listar})
    documento=template.render(context)
    return HR(documento)