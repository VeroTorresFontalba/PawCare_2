from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView,
    CreateView
) 
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/home.html'

class ColaboradoresView(TemplateView):
    template_name = 'home/colab.html'

class ServicioView(LoginRequiredMixin,TemplateView):
    template_name = 'home/servicios.html'
    # login_url = reverse_lazy('users_app:user_login')

class SomosView(TemplateView):
    template_name = 'home/somos.html'

class BaseView(CreateView):
    template_name='base.html'


