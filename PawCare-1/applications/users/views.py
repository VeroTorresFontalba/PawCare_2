import dataclasses
from django.forms.models import BaseModelForm

from rest_framework.generics import (
    ListAPIView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages

from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse

from django.core.mail import send_mail

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

from .serializers import MascotaSerializers

from .forms import CronogramaForm, MascotaForm, UserRegisterForm, LoginForm,PerfilForm,ServiciosForm ,EspeciesForm
# , ServiciosForm ,PerfilForm,EditarProfileForm,

from .models import User,Profile,Cronograma ,Mascota ,Servicio,ReservaCliente,Hora, Especies
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
            # tipodeusuario = form.cleaned_data['tipodeusuario'],
            
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
     
    
class ListCuidadores(LoginRequiredMixin,ListView):
    model= User
    context_object_name= 'lista_cuidadores'
    template_name= 'home/servicios.html'
    login_url = reverse_lazy('users_app:user_login')

    def get_queryset(self):
        return User.objects.listar_cuidadores()
    

class PerfilDetailView(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'users/detail.html'
    login_url = reverse_lazy('users_app:user_login')

    def get(self, request, username,*args, **kwargs):
        user = get_object_or_404(User, username=username)
        profile = Profile.objects.get(user=user)

        context={
            'user':user,
            'profile':profile
        }
        return render(request, 'users/detail.html', context)


class PerfilUpdateView(LoginRequiredMixin,UpdateView):
    model= Profile
    form_class= PerfilForm 
    template_name='users/perfil_update_forms.html'
    success_url=reverse_lazy('users_app:home')
    login_url = reverse_lazy('users_app:user_login')

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('users_app:update',args=[self.object.id]) + '?ok'

#Cronograma    

    
class CalendarioView(LoginRequiredMixin,ListView):
    context_object_name= 'calendario'
    template_name = 'users/calendario.html'
    login_url = reverse_lazy('users_app:user_login')
    def get_queryset(self):
        usuario= self.request.user
        return Cronograma.objects.horas_por_user(usuario)

class Addhoras(LoginRequiredMixin,FormView):
    template_name='users/horas.html'
    form_class = CronogramaForm
    success_url=reverse_lazy('users_app:calendario')
    login_url = reverse_lazy('users_app:user_login')
    def form_valid(self, form):

        Cronograma.objects.create(
            user = self.request.user,
            fechaReserva=form.cleaned_data['fechaReserva'],
            horas=form.cleaned_data['horas'],
            
        )
        return super(Addhoras, self).form_valid(form)
        

#Macota
class ListMascotas(LoginRequiredMixin,ListView):
    context_object_name= 'lista_mascota'
    template_name= 'users/list_mascota.html'
    login_url = reverse_lazy('users_app:user_login')


    def get_queryset(self):
        usuario= self.request.user
        return Mascota.objects.mascota_por_user(usuario)
        # return Mascota.objects.listar_mascotas()
    

class ListMascotas2(LoginRequiredMixin,ListView):
    context_object_name= 'lista_mascota'
    template_name= 'users/list_mascota.html'
    login_url = reverse_lazy('users_app:user_login')

    def get_queryset(self):
        usuario= self.request.user
        return Mascota.objects.mascota_por_user(usuario)
        # return Mascota.objects.listar_mascotas()
    
class AddMascota(LoginRequiredMixin,FormView):
    template_name= 'users/mascotaCrear.html'
    form_class = MascotaForm
    success_url =reverse_lazy('users_app:mascota') 
    login_url = reverse_lazy('users_app:user_login')

    def form_valid(self, form):
        Mascota.objects.create(
            user = self.request.user,
            nombre_de_mascota=form.cleaned_data['nombre_de_mascota'],
            chip=False,
            n_chip=form.cleaned_data['n_chip'],
            image=form.cleaned_data['image'],
            descripccion=form.cleaned_data['descripccion'],
            especies=form.cleaned_data['especies'],
        )
        return super(AddMascota, self).form_valid(form)
    

    
class ModificarMascota(LoginRequiredMixin,UpdateView):
    model= Mascota
    form_class= MascotaForm 
    template_name='users/mascota_modificar.html'
    # template_name='users/mascota.html'
    success_url=reverse_lazy('users_app:mascota')
    login_url = reverse_lazy('users_app:user_login')

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('users_app:mascota',args=[self.object.id]) 
    
class MascotaDeleteView(LoginRequiredMixin,DeleteView):
    model = Mascota
    success_url=reverse_lazy('users_app:mascota')
    login_url = reverse_lazy('users_app:user_login')

class ClienteResevarView(LoginRequiredMixin,ListView):
    context_object_name= 'reserva'
    template_name='users/vista_reserva.html'
    login_url = reverse_lazy('users_app:user_login')
    def get_queryset(self):
        return Cronograma.objects.all()


#api de mascota

class ListMascotaUser(ListAPIView):
    serializer_class= MascotaSerializers

    def get_queryset(self):
        print('para recuperar el usuer')
        print(self.request.user)
        return Mascota.objects.all()
    
class ListUser(LoginRequiredMixin,ListView):
    context_object_name= 'lista_user'
    template_name= 'administracion/user.html'
    login_url = reverse_lazy('users_app:user_login')

    def get_queryset(self):
        return User.objects.all()
    
class ListUser2(LoginRequiredMixin,ListView):
    context_object_name= 'lista_user'
    template_name= 'administracion/user.html'
    login_url = reverse_lazy('users_app:user_login')

    def get_queryset(self):
        return User.objects.all()
    
class ModificarUser_admin(LoginRequiredMixin,UpdateView):
    model= User
    form_class= UserRegisterForm 
    template_name='administracion/user_mod.html'
    success_url=reverse_lazy('users_app:usuarios_admin_s')
    login_url = reverse_lazy('users_app:user_login')

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('users_app:usuarios_admin_s',args=[self.object.id]) 

#admin servicios
class ListServicios(LoginRequiredMixin,ListView):
    context_object_name= 'lista_servicios'
    template_name= 'administracion/list_servicios.html'
    login_url = reverse_lazy('users_app:user_login')

    def get_queryset(self):
        return Servicio.objects.all()
    
class ListServicios2_admin(LoginRequiredMixin,ListView):
    context_object_name= 'lista_servicios'
    template_name= 'administracion/list_servicios.html'
    login_url = reverse_lazy('users_app:user_login')

    def get_queryset(self):
        return Servicio.objects.all()
    

class AddServicios_admin(LoginRequiredMixin,FormView):
    template_name= 'administracion/servicioCrear.html'
    form_class = ServiciosForm
    success_url =reverse_lazy('users_app:servicios_admin') 
    login_url = reverse_lazy('users_app:user_login')

    def form_valid(self, form):
        Servicio.objects.create(
            id=form.cleaned_data['id'],
            nombre=form.cleaned_data['nombre'],
            informacion=form.cleaned_data['informacion'],
        )

        return super(AddServicios_admin, self).form_valid(form)
    
class ModificarServicio_admin(LoginRequiredMixin,UpdateView):
    model= Servicio
    form_class= ServiciosForm 
    template_name='administracion/servicioModificar.html'
    success_url =reverse_lazy('users_app:servicios_admin_s') 
    login_url = reverse_lazy('users_app:user_login')

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('users_app:servicios_admin_s',args=[self.object.id]) 


class ServicioDeleteView(LoginRequiredMixin,DeleteView):
    model = Servicio
    success_url=reverse_lazy('users_app:servicios_admin')
    login_url = reverse_lazy('users_app:user_login')


# admin especies
class ListEspecies(LoginRequiredMixin,ListView):
    context_object_name= 'lista_especies'
    template_name= 'administracion/list_especies.html'
    login_url = reverse_lazy('users_app:user_login')

    def get_queryset(self):
        return Especies.objects.all()
    
class ListEspecies2_admin(LoginRequiredMixin,ListView):
    context_object_name= 'lista_especies'
    template_name= 'administracion/list_especies.html'
    login_url = reverse_lazy('users_app:user_login')

    def get_queryset(self):
        return Servicio.objects.all()
    

class AddEspecies_admin(LoginRequiredMixin,FormView):
    template_name= 'administracion/especiesCrear.html'
    form_class = EspeciesForm
    success_url =reverse_lazy('users_app:especie_admin') 
    login_url = reverse_lazy('users_app:user_login')

    def form_valid(self, form):
        Especies.objects.create(
            id=form.cleaned_data['id'],
            nombre=form.cleaned_data['nombre'],
        )

        return super(AddEspecies_admin, self).form_valid(form)
    
class ModificarEspecie_admin(LoginRequiredMixin,UpdateView):
    model= Especies
    form_class= EspeciesForm 
    template_name='administracion/especieModificar.html'
    success_url =reverse_lazy('users_app:especie_admin_s') 
    login_url = reverse_lazy('users_app:user_login')

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('users_app:especie_admin_s',args=[self.object.id]) 


class EspecieDeleteView(LoginRequiredMixin,DeleteView):
    model = Especies
    success_url=reverse_lazy('users_app:especie_admin')
    login_url = reverse_lazy('users_app:user_login')


def send_email_cuidador(request):
    subject = "Confirmación Reserva"
    message = "Su hora con fecha:.... ha sido reservada con exito por:...."
    from_email = "pawcare3@gmail.com"

    user = request.user
    recipient_list = [ user.email ]
    
    send_mail (subject , message, from_email, recipient_list)


def send_email_cliente(request):
    subject = "Confirmación Reserva"
    message = "Su hora con fecha:.... , con:... ha sido reservada con exito."
    from_email = "pawcare3@gmail.com"
    
    user = get_user_model(User, username=username)
    recipient_list = [ user.email ]
    
    send_mail (subject , message, from_email, recipient_list)

    return HttpResponse("Notificación fue enviada con exito")