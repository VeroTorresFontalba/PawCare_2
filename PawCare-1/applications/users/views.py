from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect

from django.views.generic import (
    View,
    ListView,
    CreateView
)
from django.views.generic.edit import (
    FormView
)



from .forms import UserRegisterForm, LoginForm

from .models import User
from .managers import UserManager
# Create your views here.
class UserRegisterView(FormView):
    template_name='users/registro.html'
    form_class=UserRegisterForm
    success_url='/'

    def form_valid(self, form):

        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            categoria = form.cleaned_data['categoria'],
        )
        return super(UserRegisterView, self).form_valid(form)
    
class LoginUser(FormView):
    template_name='users/login.html'
    form_class=LoginForm
    success_url=reverse_lazy('home_app:home')

    def form_valid(self, form):
        user = authenticate(
           username=form.cleaned_data['username'],
           password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('home_app:home')
            )
    
class ListCuidadores(ListView):
    #model= User
    context_object_name= 'lista_cuidadores'
    template_name= 'home/servicios.html'

    def get_queryset(self):
        return User.objects.listar_cuidadores()