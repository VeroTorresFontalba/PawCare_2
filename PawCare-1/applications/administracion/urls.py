from django.urls import path
from .views import *

app_name = "admin_app"

urlpatterns = [
    path('colab/', ListColaboradores.as_view(),name='colaboradores'),
    path('list_colab_admin/', ListColaboradores_admin.as_view(), name='colaboradores_admin'),
    path('list_colab_admin/<id>', ListColaboradores2_admin.as_view(), name='colaboradores_admin_s'),
    path('crear_colaborador/',AddColaboradores_admin.as_view(), name='crear_colaborador'),
    path('colaborador_modificar/<int:pk>', ModificarColab_admin.as_view(),name='colaborador_modificar'),
    

]

