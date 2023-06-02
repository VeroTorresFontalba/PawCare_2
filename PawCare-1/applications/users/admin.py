from django.contrib import admin
from .models import User,Servicio, Profile, Hora
# Register your models here.
admin.site.register(User)
admin.site.register(Servicio)
admin.site.register(Profile)
admin.site.register(Hora)
