from django.contrib import admin
from .models import User,Servicio, Profile ,Especies ,Mascota, EstadoReserva, Hora,Cronograma,ReservaCliente
# ,DiaReserva,EstadoReserva
# Hora
# Register your models here.
admin.site.register(User)
admin.site.register(Servicio)
admin.site.register(Profile)
#
admin.site.register(Hora)
admin.site.register(EstadoReserva)
admin.site.register(Cronograma)
# admin.site.register(DiaReserva)
admin.site.register(Especies)
admin.site.register(Mascota)
admin.site.register(ReservaCliente)



