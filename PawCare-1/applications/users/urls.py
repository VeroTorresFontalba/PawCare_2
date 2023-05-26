
from django.urls import path


from .views import *


app_name ="users_app"


urlpatterns = [
    path('registro/', UserRegisterView.as_view(),name='user_register'),
    path('login/', LoginUser.as_view(),name='user_login'),
    path('logout/', LogoutView.as_view(),name='user_logout'),
    path('perfil/perfil', PerfilView.as_view(),name='user_perfil'),
    path('users/<username>/', UserProfileView.as_view(), name='profile'),
    path('profile/edit',EditProfile, name='edit-profile'),
    # path('perfil/perfil', UserProfileView.as_view(), name='profile'),

    # path('administrador/listar_servicio/',ListadoServicios.as_view(),name= 'listar_servicio'),
    # path('administrador/crear_servicio/',CrearServicio.as_view(),name= 'crear_servicio'),
    path('administrador/listar_servicio/',listar_servicio,name= 'listar_servicio'),
    path('administrador/crear_servicio/',crear_servicio, name='crear_servicio'),
    path('administrador/modificar_servicio/<id>', modificar_servicio, name='modificar_servicio'),
    path('eliminar_servicio/<id>', eliminar_servicio, name='eliminar_servicio'),
    #
    path('administrador/perfiles/',listar_perfiles,name= 'listar_perfil'), 
    path('administrador/modificar_perfil/<id>',modificar_perfil,name= 'modificar_perfil'), 


]