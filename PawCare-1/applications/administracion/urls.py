from django.urls import path
from .views import *

app_name = "admin_app"

urlpatterns = [
    # path('colab/', ListColaboradores.as_view(),name='colaboradores'),
    path('colab/', lista_colaboradores, name='colaboradores'),
    path('list_colab_admin/', lista_colaboradores_admin, name='colaboradores_admin'),
    path('crear_colaborador/',colaboradorCrear, name='crear_colaborador'),

    path('colaborador_eliminar/<id>', colaborador_eliminar, name='colaborador_eliminar'),
]