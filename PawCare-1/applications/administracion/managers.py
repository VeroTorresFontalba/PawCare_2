from django.shortcuts import render
from django.db import models
from django.db.models import Q

from applications.administracion.models import Colaboradores



# def lista_colaboradores(request):
#     lista_colaboradores = Colaboradores.objects.all()

#     datos = {
#         'Colaborador': lista_colaboradores
#     }
#     return render(request, 'home/colab.html', datos)