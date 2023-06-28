import dataclasses, json
from django.forms.models import BaseModelForm

from rest_framework.generics import (
    ListAPIView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render,get_object_or_404,redirect
#, render
from django.urls import reverse_lazy, reverse
from django.contrib import messages

from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.db.models import Q
from django.db.models import Subquery, Avg
from django.core.mail import send_mail
from django.template.loader import render_to_string
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
from django.http import JsonResponse
from django.contrib import messages

from .serializers import MascotaSerializers

from .forms import CronogramaForm, MascotaForm, UserRegisterForm, LoginForm,PerfilForm,ServiciosForm ,EspeciesForm ,ReservaForm
# , ServiciosForm ,PerfilForm,EditarProfileForm, 

from .models import User,Profile,Cronograma ,Mascota ,Servicio,ReservaCliente,Hora, Especies, EstadoReserva
#, Servicio , 

#para la solicitud ajax de guardarcalificacion
from django.views.decorators.csrf import csrf_exempt


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
            region = form.cleaned_data['region'],
            comuna = form.cleaned_data['comuna'],
            direccion = form.cleaned_data['direccion'],
            # tipodeusuario = form.cleaned_data['tipodeusuario'],
            
        )

        return super(UserRegisterView, self).form_valid(form) 
    # def get_success_url(self):
    #     return reverse_lazy('users_app:user_register',args=[self.object.id]) + '?ok'

# class UserRegisterView(FormView):
#     template_name = 'users/registro.html'
#     form_class = UserRegisterForm
#     success_url = reverse_lazy('users_app:user_login')

#     def form_valid(self, form):
#         # Crear un nuevo usuario
#         user = User.objects.create_user(
#             form.cleaned_data['username'],
#             form.cleaned_data['email'],
#             form.cleaned_data['password1'],
#             nombres=form.cleaned_data['nombres'],
#             apellidos=form.cleaned_data['apellidos'],
#             telefono=form.cleaned_data['telefono'],
#             rut=form.cleaned_data['rut'],
#             categoria=form.cleaned_data['categoria'],
#         )

#         # Mostrar mensaje de éxito utilizando SweetAlert
#         data = {
#             'title': '¡Éxito!',
#             'text': 'Bienvenido!!!.',
#             'icon': 'success'
#         }
#         return JsonResponse(data)

#     def form_invalid(self, form):
#         # Mostrar mensaje de error utilizando SweetAlert
#         data = {
#             'title': 'Error',
#             'text': 'Hubo un problema al registrar el usuario.',
#             'icon': 'error'
#         }
#         return JsonResponse(data)  

class ReservaRegisterView(FormView):
    template_name='users/prueba.html'
    form_class=ReservaForm
    success_url=reverse_lazy('users_app:cuidadores')

    def form_valid(self, form ):

        ReservaCliente.objects.create_user(
            correocuidaor=form.cleaned_data['correocuidaor'],
            correocliente=form.cleaned_data['correocliente'],
            idCuidador=form.cleaned_data['idCuidador'],
            idCliente = form.cleaned_data['idCliente'],
            nombreCliente = form.cleaned_data['nombreCliente'],
            nombreCuidador = form.cleaned_data['nombreCuidador'],
            fechareserva = form.cleaned_data['fechareserva'],
            horasInicio = form.cleaned_data['horasInicio'],
            horasFin = form.cleaned_data['horasFin'],
            
        )

        return super(ReservaRegisterView, self).form_valid(form)
    
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
        kword = self.request.GET.get('kword', '')  # Obtener el valor ingresado en el input de búsqueda
        palabra_clave = self.request.GET.get('nombre', '') 
        return User.objects.listar_cuidadores(kword,palabra_clave)
    

    
    # def get_queryset(self):
    #     palabra_clave= self.request.GET.get("kword",'')
    #     return Servicio.objects.buscar_servicios(palabra_clave)
    

# class ListCuidadores2(LoginRequiredMixin,ListView):
#     model= User
#     context_object_name= 'lista_cuidadores'
#     template_name= 'users/vista_reserva.html'
#     login_url = reverse_lazy('users_app:user_login')

#     def get_queryset(self):
     
#         return User.objects.listar_cuidadores()
    
class ListCuidadores3(LoginRequiredMixin,ListView):
    
    context_object_name= 'lista_cuidadores'
    template_name= 'users/prueba.html'
    login_url = reverse_lazy('users_app:user_login')

    def get_queryset(self):
        id = self.kwargs['id']
    #   kword = self.request.GET.get('kword', '')

        f1 = self.request.GET.get("fecha1", '')
        f2 = self.request.GET.get("fecha2", '')

        if f1 and f2 :
            return Cronograma.objects.listar_cuidadores_horas(id,f1,f2) 
        else:
            return Cronograma.objects.listar_cuidadores_horas2(id)


# class ListCuidadores3(LoginRequiredMixin,ListView):
    
#     context_object_name= 'lista_cuidadores'
#     template_name= 'users/prueba.html'
#     login_url = reverse_lazy('users_app:user_login')

#     def get_queryset(self):
#         id = self.kwargs['id']

#         return Cronograma.objects.listar_cuidadores_horas(id) 
  


  


    

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
        #estado_disponible = EstadoReserva.objects.get(pk=1)
        #reservas = Cronograma.objects.filter(
        #    user = usuario,
        #    estado = estado_disponible
        #).values('horas__pk')

        #horas_reservadas = [reserva['horas__pk'] for reserva in reservas]
        #return Hora.objects.exclude(pk__in = horas_reservadas)
        

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
            # horas= Hora.objects.all['horas'],
            
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
            chip=form.cleaned_data['chip'],
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
        return reverse_lazy('users_app:mascota',args=[self.object.id]) + '?ok'
    
class MascotaDeleteView(LoginRequiredMixin,DeleteView):
    model = Mascota
    success_url=reverse_lazy('users_app:mascota') 
    login_url = reverse_lazy('users_app:user_login')

    #def delete(self, request, *args, **kwargs):
        # Resto del código
        
        #return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('users_app:mascota') + '?deleted'

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
    success_url =reverse_lazy('users_app:especie_modificar') 
    login_url = reverse_lazy('users_app:user_login')

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('users_app:especie_modificar',args=[self.object.id]) + '?ok'


class EspecieDeleteView(LoginRequiredMixin,DeleteView):
    model = Especies
    success_url=reverse_lazy('users_app:especie_admin')
    login_url = reverse_lazy('users_app:user_login')

# def mi_funcion(pk):
#     # Obtener objeto del PrimerModelo usando la clave primaria (pk)
#     primer_objeto = get_object_or_404(PrimerModelo, pk=pk)
    
#     # Obtener la clave primaria del objeto
#     clave_primaria = primer_objeto.pk
    
#     # Crear un nuevo objeto del SegundoModelo
#     segundo_objeto = SegundoModelo()
    
#     # Establecer la clave primaria en el nuevo objeto del SegundoModelo
#     segundo_objeto.clave_foranea = clave_primaria
    
#     # Guardar el nuevo objeto del SegundoModelo
#     segundo_objeto.save()    

def obtener_mascotas_por_usuario(usuario_id):
    mascotas = Mascota.objects.filter(user_id=usuario_id)
    return mascotas

def reservar_cuidador(request, cronograma_id):

    cronograma = Cronograma.objects.get(id=cronograma_id)
    
    

    estado_reservada = EstadoReserva.objects.get(pk=2) #reservada id 2
    cronograma.estado = estado_reservada

    
    servicios = cronograma.user.profile.servicios.all()
    


    cronograma.save()

    reserva = ReservaCliente()
    
    reserva.clienteusername=request.user
    reserva.idCronograma = cronograma
    reserva.idCliente = request.user.id
    reserva.idCuidador = cronograma.user.id
    reserva.correocliente = cronograma.user.email
    reserva.correocuidaor = request.user.email
    reserva.nombreCliente = request.user.get_full_name()
    reserva.nombreCuidador = cronograma.user.get_full_name()
    reserva.fechareserva = cronograma.fechaReserva
    reserva.horasInicio = cronograma.horas.horaInicio
    reserva.horasFin = cronograma.horas.horaFin
    # reserva.servicios = cronograma.user.profile.servicios.nombre()
    # reserva.servicios = [servicio.nombre for servicio in servicios]
    reserva.servicios = ', '.join([servicio.nombre for servicio in servicios])



    reserva.save()
    print(reserva.idCronograma)

    usuario_id = request.user.id
    mascotas = obtener_mascotas_por_usuario(usuario_id)

    correo_enviado = True
    
    subject = "Confirmación Reserva"
    from_email = "pawcare3@gmail.com"
    message='Hola'
    recipient_list = [reserva.correocliente] #cuidador
    context={'subject': subject,
        'from_email': from_email,
        'message': message,
        'reserva': reserva,
        'mascotas':mascotas}
    html_message= render_to_string('users/email_confirmacion_cuidador.html', context=context)

    send_mail (subject ,message, from_email, recipient_list, html_message=html_message)

    subject = "Confirmación Reserva"
    from_email = "pawcare3@gmail.com" 
    recipient_list = [reserva.correocuidaor] #cliente
    context={'subject': subject,
        'from_email': from_email,
        'message': message,
        'reserva': reserva}
    html_message= render_to_string('users/email_confirmacion_cliente.html', context=context)

    send_mail (subject ,message, from_email, recipient_list,html_message=html_message)

    context = {
        'correo_enviado': correo_enviado,
    }

    return render(request, 'users/prueba.html', context)


    #return redirect(request.META.get('HTTP_REFERER', ''))
   # return redirect('users_app:reservar_cuidador', cronograma_id)

# def reservar_cuidador(request, cronograma_id):
#     cronograma = Cronograma.objects.get(id=cronograma_id)
    
#     estado_reservada = EstadoReserva.objects.get(pk=2)  # reservada id 2
#     cronograma.estado = estado_reservada
#     servicios = cronograma.user.profile.servicios.all()
    
#     cronograma.save()

#     if request.method == 'POST':
#         servicios_seleccionados = request.POST.getlist('servicios')

#         reserva = ReservaCliente()
#         reserva.clienteusername = request.user
#         reserva.idCronograma = cronograma
#         reserva.idCliente = request.user.id
#         reserva.idCuidador = cronograma.user.id
#         reserva.correocliente = cronograma.user.email
#         reserva.correocuidaor = request.user.email
#         reserva.nombreCliente = request.user.get_full_name()
#         reserva.nombreCuidador = cronograma.user.get_full_name()
#         reserva.fechareserva = cronograma.fechaReserva
#         reserva.horasInicio = cronograma.horas.horaInicio
#         reserva.horasFin = cronograma.horas.horaFin

#         servicios_seleccionados = servicios.filter(id__in=servicios_seleccionados)
#         reserva.servicios = ', '.join([servicio.nombre for servicio in servicios_seleccionados])

#         reserva.save()

#     return redirect(request.META.get('HTTP_REFERER', ''))

class HorasporUserList(LoginRequiredMixin,ListView):
    context_object_name='horas_por_user'
    template_name='users/listaHorasUser.html'
    login_url = reverse_lazy('users_app:user_login')
    def get_queryset(self):
        usuario= self.request.user
        return ReservaCliente.objects.horas_por_user_solicitadas(usuario)
    


class HorasRealizadasporUserList(LoginRequiredMixin,ListView):
    context_object_name='horas_realizadas_por_user'
    template_name='users/listaHorasRealizadasUser.html'
    login_url = reverse_lazy('users_app:user_login')
    def get_queryset(self):
        usuario= self.request.user
        return ReservaCliente.objects.horas_por_user_realizadas(usuario)

# class HorasRealizadasporUserList(ListView):
#     context_object_name='horas_realizadas_por_user'
#     template_name='users/listaHorasUser.html'
#     def get_queryset(self):
#         usuario= self.request.user
#         return ReservaCliente.objects.horas_por_user_realizadas(usuario)
    



def cancelar_cuidador(request, idReserva):
    try:
        reserva = ReservaCliente.objects.get(id=idReserva)
    except ReservaCliente.DoesNotExist:
        return HttpResponse("La reserva de cliente no existe.")

    cronograma = reserva.idCronograma  # Accede al objeto de cronograma asociado a la reserva

    estado_cancelado = EstadoReserva.objects.get(pk=1)  # Cancelado id 3 , tambien esta la opcion que de cancelado pase de inmediato a disponible con la pk =1
    cronograma.estado = estado_cancelado
    cronograma.save()

    correo_enviado = True
    
    subject = "Cancelación Reserva"
    from_email = "pawcare3@gmail.com"
    message='Hola'
    recipient_list = [reserva.correocliente] #cuidador
    context={'subject': subject,
        'from_email': from_email,
        'message': message,
        'reserva': reserva}
    html_message= render_to_string('users/email_cancelacion_cuidador.html', context=context)

    send_mail (subject ,message, from_email, recipient_list, html_message=html_message)

    subject = "Cancelación Reserva"
    from_email = "pawcare3@gmail.com" 
    recipient_list = [reserva.correocuidaor] #cliente
    context={'subject': subject,
        'from_email': from_email,
        'message': message,
        'reserva': reserva}
    html_message= render_to_string('users/email_cancelacion_cliente.html', context=context)

    send_mail (subject ,message, from_email, recipient_list,html_message=html_message)

    context = {
        'correo_enviado': correo_enviado,
    }
    #return render(request, 'users/listarHorasUser.html', context)
    #return redirect(request.META.get('HTTP_REFERER', ''), context)
    redirect_url = request.META.get('HTTP_REFERER', '')

    redirect_url += '?correo_enviado={}'.format(correo_enviado)

    return redirect(redirect_url)


#def rating_modal(request):
   # if request.method == 'POST':
    #    rating = request.POST.get('rating')
        # Aquí puedes realizar la lógica para guardar la calificación en tu modelo
        # Por ejemplo, guardarla en un objeto Rating asociado al usuario actual

        # Retornar una respuesta JSON indicando que la calificación se ha guardado exitosamente
       # return JsonResponse({'message': 'Calificación guardada exitosamente'})

    # En caso de que la petición no sea de tipo POST, puedes realizar alguna acción adicional
    # como renderizar una plantilla para el modal de calificación
   # return JsonResponse({'message': 'Método no permitido'})
   #pass

def rating_modal(request):
    if request.method == 'POST':
        # Aquí puedes procesar la calificación enviada por el usuario
        # y realizar cualquier otra acción necesaria
        print('Calificación guardada:', request.POST.get('rating'))
        print('Estoy en views')
    return HttpResponse()  # Devuelve una respuesta vacía

class Calificacion(CreateView):
    model= ReservaCliente
    form_class= ReservaForm 
    template_name='users/rating_modal.html'
    # template_name='users/mascota.html'
    success_url=reverse_lazy('users_app:profile')
    login_url = reverse_lazy('users_app:user_login')

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('users_app:profile',args=[self.object.id]) 
    

def actualizar_promedio_calificacion(id_cuidador):
    # Obtener todas las reservas del cuidador
    reservas = ReservaCliente.objects.filter(idCuidador=id_cuidador, calificacion__isnull=False)
    
    # Calcular el promedio de las calificaciones
    promedio = reservas.aggregate(promedio=Avg('calificacion'))['promedio']
    
    # Actualizar el promedio de calificación en el modelo User
    try:
        user = User.objects.get(id=id_cuidador)
        user.promediocalificacion = promedio
        user.save()
    except User.DoesNotExist:
        pass  # Manejar el caso en el que el usuario no existe
  



@csrf_exempt
def guardar_calificacion(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.method == 'POST':
            data = json.loads(request.body)
            reserva_id = data.get('reserva_id')
            calificacion = data.get('calificacion')
            
            # Guardar la calificación en la reserva correspondiente
            try:
                reserva = ReservaCliente.objects.get(id=reserva_id)
                reserva.calificacion = calificacion
                reserva.save()

                # Obtener el id del cuidador asociado a la reserva
                id_cuidador = reserva.idCuidador

                # Actualizar el promedio de calificación
                actualizar_promedio_calificacion(id_cuidador)
                
                return JsonResponse({'success': True})
            except ReservaCliente.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'La reserva no existe.'})
    
    return JsonResponse({'success': False, 'message': 'Solicitud inválida.'})

@csrf_exempt
def finalizar_reserva(request, idReserva):
    try:
        reserva = ReservaCliente.objects.get(id=idReserva)
    except ReservaCliente.DoesNotExist:
        return HttpResponse("La reserva de cliente no existe.")

    cronograma = reserva.idCronograma  # Accede al objeto de cronograma asociado a la reserva

    estado_realizado = EstadoReserva.objects.get(pk=4)  # Realizado id 4
    cronograma.estado = estado_realizado
    cronograma.save()

    return redirect(request.META.get('HTTP_REFERER', ''))


class ListCronogramaDisponibles(LoginRequiredMixin,ListView):
    context_object_name= 'lista_hora_disponible'
    template_name= 'users/lista_hora_disponible.html'
    login_url = reverse_lazy('users_app:user_login')

    def get_queryset(self):
        usuario= self.request.user
        return Cronograma.objects.horas_por_user_disponibles(usuario)
    

class CronogramaDeleteView(LoginRequiredMixin,DeleteView):
    model = Cronograma
    success_url=reverse_lazy('users_app:horaseliminar') 
    login_url = reverse_lazy('users_app:user_login')
    def get_success_url(self):
        return reverse_lazy('users_app:horaseliminar') + '?deleted'


