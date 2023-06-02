import dataclasses
from datetime import date
from django.urls import reverse_lazy ,reverse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import TemplateView

from .models import Colaboradores
from .forms import ColaboradorForm
# Create your views here.




class ListColaboradores(ListView):
    context_object_name= 'lista_colaboradores'
    template_name= 'home/colab.html'

    def get_queryset(self):
        return Colaboradores.objects.listar_colaboradores()
    
    def get_queryset(self):
        return Colaboradores.objects.filter(published=True)
    
class ListColaboradores_admin(ListView):
    context_object_name= 'lista_colaboradores'
    template_name= 'administracion/list_colab.html'

    def get_queryset(self):
        return Colaboradores.objects.listar_colaboradores()
    
class ListColaboradores2_admin(ListView):
    context_object_name= 'lista_colaboradores'
    template_name= 'administracion/list_colab.html'

    def get_queryset(self):
        return Colaboradores.objects.listar_colaboradores()
    

class AddColaboradores_admin(FormView):
    template_name= 'administracion/colaboradorCrear.html'
    form_class = ColaboradorForm
    success_url =reverse_lazy('admin_app:colaboradores_admin') 

    def form_valid(self, form):
        Colaboradores.objects.create(
            title=form.cleaned_data['title'],
            image=form.cleaned_data['image'],
            content=form.cleaned_data['content'],
            descuento=form.cleaned_data['descuento'],
            url=form.cleaned_data['url'],
            published=False,
            created=date.today(),
        )

        return super(AddColaboradores_admin, self).form_valid(form)
    
class ModificarColab_admin(UpdateView):
    model= Colaboradores
    form_class= ColaboradorForm 
    template_name='administracion/colaboradorModificar.html'
    success_url=reverse_lazy('admin_app:colaboradores_admin_s')

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('admin_app:colaboradores_admin_s',args=[self.object.id]) 


# def lista_colaboradores(request):
#     lista_colaboradores = Colaboradores.objects.all()

#     datos = {
#         'Colaborador': lista_colaboradores
#     }
#     return render(request, 'home/colab.html', datos)

# def lista_colaboradores_admin(request):
#     lista_colaboradores = Colaboradores.objects.all()

#     datos = {
#         'Colaborador': lista_colaboradores
#     }
#     return render(request, 'administracion/list_colab.html', datos)


# def colaboradorCrear(request):
#     if request.method=='POST': 
#         Colaborador_Form = ColaboradorForm(request.POST, files=request.FILES)
#         if Colaborador_Form.is_valid:
#             Colaborador_Form.save()
#             return redirect ('admin_app:colaboradores_admin') 
#     else:
#         Colaborador_Form = ColaboradorForm()
#     return render(request, 'administracion/colaboradorCrear.html', {'Colaborador_Form': ColaboradorForm})


# def colaborador_modificar(request, id): 
#     colaborador = Colaboradores.objects.get(id=id)
#     datos={
#         'Colaborador_Form': ColaboradorForm(instance=colaborador)
#     }
#     if request.method=='POST':
#         Colaborador_Form=ColaboradorForm(data=request.POST, instance=colaborador)
#         if Colaborador_Form.is_valid:
#             Colaborador_Form.save()
#             return redirect('admin_app:colaboradores_admin')
    
#     return render(request, 'administracion/colaboradorModificar.html', datos)



# def colaborador_eliminar(request, id):
#     colaborador = Colaboradores.objects.get(id=id)
#     colaborador.delete()
#     return redirect('admin_app:colaboradores_admin')


