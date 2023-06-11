
from django.urls import path


from django.contrib.auth import views as auth_views
from .views import *

from .forms import UserPasswordResetForm

from .views import *
app_name ="users_app"


urlpatterns = [
    path('registro/', UserRegisterView.as_view(),name='user_register'),
    path('login/', LoginUser.as_view(),name='user_login'),
    path('logout/', LogoutView.as_view(),name='user_logout'),
    path('servicios/', ListCuidadores.as_view(),name='cuidadores'),


    path('users/<username>', PerfilDetailView.as_view(),name='profile'),


    
    path('list_mascota/', ListMascotas.as_view(), name='mascota'),
    path('list_mascota/<id>', ListMascotas2.as_view(), name='mascota'),
    path('crear_mascota/',AddMascota.as_view(), name='crear_mascota'),
    path('mascota_modificar/<int:pk>', ModificarMascota.as_view(),name='mascota_modificar'),
    path('mascota_eliminar/<int:pk>', MascotaDeleteView.as_view(),name='mascota_eliminar'),

    path('update/<int:pk>', PerfilUpdateView.as_view(),name='update'),


    path('servicios/', ListCuidadores.as_view(),name='cuidadores'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html', form_class=UserPasswordResetForm), name='password_reset'),
    
    path('calendario/',CalendarioView.as_view(), name= 'calendario'),
    path('calendario2/',AddFechaView.as_view(), name= 'calendario'),

    #MASCOTAS
    # path('lista_mascota/', ListMascotas.as_view(), name='mascotas'),
]