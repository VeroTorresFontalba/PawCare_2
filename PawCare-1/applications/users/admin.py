from django.contrib import admin
from .models import User,Servicio, Profile ,Especies ,Mascota,DiaReserva,EstadoReserva
# Hora
# Register your models here.
admin.site.register(User)
admin.site.register(Servicio)
admin.site.register(Profile)
admin.site.register(EstadoReserva)
admin.site.register(DiaReserva)
admin.site.register(Especies)
admin.site.register(Mascota)



