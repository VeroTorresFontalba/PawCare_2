import dataclasses
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
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
    
class ListColaboradores_admin(LoginRequiredMixin,ListView):
    context_object_name= 'lista_colaboradores'
    template_name= 'administracion/list_colab.html'
    login_url = reverse_lazy('users_app:user_login')

    def get_queryset(self):
        return Colaboradores.objects.listar_colaboradores()
    
class ListColaboradores2_admin(LoginRequiredMixin,ListView):
    context_object_name= 'lista_colaboradores'
    template_name= 'administracion/list_colab.html'
    login_url = reverse_lazy('users_app:user_login')

    def get_queryset(self):
        return Colaboradores.objects.listar_colaboradores()
    

class AddColaboradores_admin(LoginRequiredMixin,FormView):
    template_name= 'administracion/colaboradorCrear.html'
    form_class = ColaboradorForm
    success_url =reverse_lazy('admin_app:colaboradores_admin') 
    login_url = reverse_lazy('users_app:user_login')

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
    
class ModificarColab_admin(LoginRequiredMixin,UpdateView):
    model= Colaboradores
    form_class= ColaboradorForm 
    template_name='administracion/colaboradorModificar.html'
    success_url=reverse_lazy('admin_app:colaboradores_admin_s')
    login_url = reverse_lazy('users_app:user_login')

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('admin_app:colaboradores_admin_s',args=[self.object.id]) 




