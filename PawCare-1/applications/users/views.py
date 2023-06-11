import dataclasses
from django.forms.models import BaseModelForm
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages

from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse

from django.views.generic import (
    View,
    CreateView,
    TemplateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.views.generic.edit import (
    FormView
)



from .forms import MascotaForm, UserRegisterForm, LoginForm,PerfilForm
# , ServiciosForm ,PerfilForm,EditarProfileForm

from .models import User,Profile ,Mascota,DiaReserva
#, Servicio ,



# Create your views here.
class UserRegisterView(FormView):
    template_name='users/registro.html'
    form_class=UserRegisterForm
    success_url=reverse_lazy('users_app:user_login')

    def form_valid(self, form ):

        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            telefono = form.cleaned_data['telefono'],
            rut = form.cleaned_data['rut'],
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
    model= User
    context_object_name= 'lista_cuidadores'
    template_name= 'home/servicios.html'

    def get_queryset(self):
        return User.objects.listar_cuidadores()
    

class PerfilDetailView(DetailView):
    model = Profile
    template_name = 'users/detail.html'
    def get(self, request, username,*args, **kwargs):
        user = get_object_or_404(User, username=username)
        profile = Profile.objects.get(user=user)

        context={
            'user':user,
            'profile':profile
        }
        return render(request, 'users/detail.html', context)


class PerfilUpdateView(UpdateView):
    model= Profile
    form_class= PerfilForm 
    template_name='users/perfil_update_forms.html'
    success_url=reverse_lazy('users_app:home')

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('users_app:update',args=[self.object.id]) + '?ok'
    

class CalendarioView(ListView):
    context_object_name= 'calendario'
    template_name = 'users/calendario.html'
    def get_queryset(self):
        return DiaReserva.objects.all()
        # return DiaReserva.objects.listar_horas()


    


class ListMascotas(ListView):
    context_object_name= 'lista_mascota'
    template_name= 'users/list_mascota.html'


    def get_queryset(self):
        return Mascota.objects.all()
        # return Mascota.objects.listar_mascotas()
    

class ListMascotas2(ListView):
    context_object_name= 'lista_mascota'
    template_name= 'users/list_mascota.html'


    def get_queryset(self):
        return Mascota.objects.all()
        return Mascota.objects.listar_mascotas()
    
class AddMascota(FormView):
    template_name= 'users/mascotaCrear.html'
    form_class = MascotaForm
    success_url =reverse_lazy('users_app:mascota') 

    def form_valid(self, form):
        Mascota.objects.create(

            nombre_de_mascota=form.cleaned_data['nombre_de_mascota'],
            chip=form.cleaned_data['chip'],
            n_chip=form.cleaned_data['n_chip'],
            image=form.cleaned_data['image'],
            descripccion=form.cleaned_data['descripccion'],
            especies=form.cleaned_data['especies'],
        )
        return super(AddMascota, self).form_valid(form)
    
class ModificarMascota(UpdateView):
    model= Mascota
    form_class= MascotaForm 
    template_name='users/mascotaModificar.html'
    # template_name='users/mascota.html'
    success_url=reverse_lazy('users_app:mascota')

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('users_app:mascota',args=[self.object.id]) 
    

class MascotaDeleteView(DeleteView):
    model = Mascota
    success_url=reverse_lazy('users_app:mascota')
