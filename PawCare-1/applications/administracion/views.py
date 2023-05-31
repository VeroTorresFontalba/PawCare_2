from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from .models import Colaboradores
from .forms import ColaboradorForm
# Create your views here.


# class ListColaboradores(ListView):
#     model= Colaboradores
#     context_object_name= 'lista_colaboradores'
#     template_name= 'home/colab.html'

#     def get_queryset(self):
#         return Colaboradores.objects.listar_colaboradores()


def lista_colaboradores(request):
    lista_colaboradores = Colaboradores.objects.all()

    datos = {
        'Colaborador': lista_colaboradores
    }
    return render(request, 'home/colab.html', datos)

def lista_colaboradores_admin(request):
    lista_colaboradores = Colaboradores.objects.all()

    datos = {
        'Colaborador': lista_colaboradores
    }
    return render(request, 'administracion/list_colab.html', datos)


def colaboradorCrear(request):
    if request.method=='POST': 
        Colaborador_Form = ColaboradorForm(request.POST, files=request.FILES)
        if Colaborador_Form.is_valid:
            Colaborador_Form.save()
            return redirect ('admin_app:colaboradores_admin') 
    else:
        Colaborador_Form = ColaboradorForm()
    return render(request, 'administracion/colaboradorCrear.html', {'Colaborador_Form': ColaboradorForm})





def colaborador_eliminar(request, id):
    colaborador = Colaboradores.objects.get(id=id)
    colaborador.delete()
    return redirect('admin_app:colaboradores_admin')


