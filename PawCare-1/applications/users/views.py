import dataclasses
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy, reverse

from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect,JsonResponse

from django.views.generic import (
    View,
    CreateView,
    TemplateView,
    ListView
)
from django.views.generic.edit import (
    FormView
)



from .forms import UserRegisterForm, LoginForm, ServiciosForm ,PerfilForm,EditarProfileForm

from .models import User, Servicio ,Profile


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
    
# class UserProfileView(TemplateView):
#     template_name = 'perfil/perfil.html'

class PerfilView(TemplateView):
    template_name='perfil/perfil.html'
    
class UserProfileView(View):

    def get(self, request, username,*args, **kwargs):
        user = get_object_or_404(User, username=username)
        profile = Profile.objects.get(user=user)

        context={
            'user':user,
            'profile':profile
        }
        return render(request, 'users/detail.html', context)


@login_required    
def EditProfile(request):
    user = request.user.id
    profile =Profile.objects.get(user__id=user)
    user_basic_info= User.objects.get(id=user)

    if request.method == 'POST':
        form=EditarProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            user_basic_info.email=form.cleaned_data.get('email')
            user_basic_info.telefono=form.cleaned_data.get('telefono')

            profile.picture = form.cleaned_data.get('picture')
            profile.descripcion = form.cleaned_data.get('descripcion')
            profile.servicios = form.cleaned_data.get('servicios')

            profile.save()
            user_basic_info.save()
            return redirect('users:profile',username=request.user.username)
        
    else:
        form=EditarProfileForm(instance=profile)

    context={
        'form':form,
    }

    return render(request, 'users/edit.html', context)


# @login_required    
# def EditProfile(request):
#     user = request.user.id
#     profile =Profile.objects.get(user__id=user)
#     user_basic_info= User.objects.get(id=user)

#     datos = {
#         'form': EditarProfileForm(instance=profile)
#     }

#     if request.method == 'POST':
#         form=EditarProfileForm(data = request.POST,file=request.FILES,instance=profile)
#         if form.is_valid():
#             user_basic_info.email=form.cleaned_data.get('email')
#             user_basic_info.telefono=form.cleaned_data.get('telefono')

#             profile.picture = form.cleaned_data.get('picture')
#             profile.descripcion = form.cleaned_data.get('descripcion')
#             profile.servicios = form.cleaned_data.get('servicios')
            
#             profile.save()
#             user_basic_info.save()
#             form.save()
#             dataclasses['form'] = EditarProfileForm(instance=profile.objects.get(id=id))
#             return redirect('users:profile',username=request.user.username)
        
#     else:
#         form=EditarProfileForm(instance=profile)

#     context={
#         'form':form,
#     }

#     return render(request, 'users/edit.html', datos,context)

# def EditProfile(request, id): 
#     user = request.user.id
#     profile = Profile.objects.get(user__id=user)
#     datos = {
#         'form': EditarProfileForm(instance=profile)
#     }
#     if request.method=='POST':
#         formulario = EditarProfileForm(data = request.POST, instance=profile, files=request.FILES)
#         if formulario.is_valid: 
#             formulario.save()
#             dataclasses['form'] = EditarProfileForm(instance=profile.objects.get(id=id))
#             return redirect ('users:profile',username=request.user.username)
#     return render (request, 'users/edit.html', datos )
# administracion

# class ListadoServicios(ListView):
#     model = Servicio
#     template_name='administrador/listar_servicio.html'
#     context_object_name = 'servicios'
#     queryset = Servicio.objects.filter(estado=True)


# class CrearServicio( CreateView):
#     model = Servicio
#     form_class = ServiciosForm
#     template_name = 'administrador/crear_servicio.html'


#     def post(self, request, *args, **kwargs):
#         if request.is_ajax():
#             form = self.form_class(request.POST)
#             if form.is_valid():
#                 nuevo_autor = Servicio(
#                     nombre=form.cleaned_data.get('nombre'),
#                     informacion=form.cleaned_data.get('informacion'),
#                 )
#                 nuevo_autor.save()
#                 mensaje = f'{self.model.__name__} registrado correctamente!'
#                 error = 'No hay error!'
#                 response = JsonResponse({'mensaje': mensaje, 'error': error})
#                 response.status_code = 201
#                 return response
#             else:
#                 mensaje = f'{self.model.__name__} no se ha podido registrar!'
#                 error = form.errors
#                 response = JsonResponse({'mensaje': mensaje, 'error': error})
#                 response.status_code = 400
#                 return response
#         else:
#             return redirect('administrador/listar_servicio.html')

def listar_servicio(request):
    servicios = Servicio.objects.all()

    datos = {
        'servicios': servicios
    }
    return render(request, 'administrador/listar_servicio.html', datos)


def crear_servicio(request):
    if request.method=='POST': 
        servicio_form = ServiciosForm(request.POST)
        if servicio_form.is_valid:
            servicio_form.save()
            return redirect ('/administrador/listar_servicio')
    else:
        servicio_form =ServiciosForm()
    return render(request, 'administrador/crear_servicio.html', {'servicio_form': servicio_form})



def modificar_servicio(request,id):
    servicio = Servicio.objects.get(id=id)
    datos={
        'form': ServiciosForm(instance=servicio)
    }
    if request.method=='POST':
        formulario=ServiciosForm(data=request.POST, instance=servicio)
        if formulario.is_valid:
            formulario.save()
            return redirect('/administrador/listar_servicio')
    
    return render(request, 'administrador/modificar_servicio.html', datos)



def eliminar_servicio(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.delete()
    return redirect('/administrador/listar_servicio')



def listar_perfiles(request):
    perfile = Profile.objects.all()

    datos = {
        'perfile': perfile
    }
    return render(request, 'administrador/perfiles.html', datos)



def modificar_perfil(request,id):
    perfile = Profile.objects.get(id=id)
    datos={
        'form': PerfilForm(instance=perfile)
    }
    if request.method=='POST':
        formulario=PerfilForm(data=request.POST, instance=perfile)
        if formulario.is_valid:
            formulario.save()
            return redirect('/administrador/perfiles')
    
    return render(request, '/administrador/modificar_perfiles.html', datos)