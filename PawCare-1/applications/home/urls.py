from django.urls import path
from .views import *

app_name = "home_app"

urlpatterns = [
    path('',HomeView.as_view(),name='home',),
    path('colaboradores/',ColaboradoresView.as_view(),name='colaboradores',),
    path('servicios/',ServicioView.as_view(),name='servicios',),
    path('somos/',SomosView.as_view(),name='somos',),

    path('base/',BaseView.as_view(),name='base',),


]
