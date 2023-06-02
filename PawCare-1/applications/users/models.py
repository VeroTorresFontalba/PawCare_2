from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin
from django.db.models.signals import post_save 

from .managers import UserManager

from applications.categoria.models import Categoria

# Create your models here.
class User (AbstractBaseUser, PermissionsMixin, models.Model ):

    username = models.CharField(max_length=16, unique=True)
    email = models.EmailField()
    rut = models.CharField(max_length=9, null= True)
    nombres= models.CharField(max_length=100)
    apellidos= models.CharField(max_length=100)
    telefono= models.CharField(max_length=9,null = True)
    #tipodeusuario=models.CharField(max_length=2,choices=TIPOUSER_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,null=True,default=1)
    #
    is_staff = models.BooleanField(default=False) #para especificar si el usuario es administrador
    is_active= models.BooleanField(default=True)   
    USERNAME_FIELD ='username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_short_name(self):
        return self.username
    def get_full_name(self):
        return self.nombres+" "+self.apellidos

#Modelo de Tipos de servicios
class Servicio(models.Model):
    id= models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=80, unique= True,verbose_name='Tipo de servicio')
    informacion=models.TextField(max_length=2000,blank=False,null=True, default='Sin description')
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural ='servicios'
        ordering = ['id']
    def __str__(self):
        return self.nombre 

#Modelo perfil
def user_directory_path_profile(instance, filename):
    profile_picture_name = 'users/{0}/profile.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name
class Profile(models.Model):
    id= models.AutoField(primary_key=True)
    user= models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    # picture = models.ImageField(default='users/user_default_profile.png', upload_to=user_directory_path_profile)
    picture = models.ImageField(default='users/perfil_defecto.jpg', upload_to=user_directory_path_profile)
    descripcion= models.TextField(max_length=2000,null=True,blank=True)
    # servicios=models.ForeignKey(Tservicio,on_delete=models.CASCADE,null=True)
    servicios=models.ManyToManyField(Servicio,related_name='servicios',verbose_name='Tipos de servicios')

    def __str__(self):
        return self.user.username
    

    # def obtener_servicios(self):
    #     servicio = str([servicios for servicios in self.servicios_id.all().values_list('nombre',flat = True)]).replace("[","").replace("]","").replace("'","")
    #     return servicio
    

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# created profile
post_save.connect(create_user_profile, sender=User)
# save created profile
post_save.connect(save_user_profile, sender=User)
 
class DiaReserva(models.Model):
    id=models.AutoField(primary_key=True)
    fechaReserva=models.DateField()
    horaReserva=models.TimeField()

class Hora(models.Model):
    id=models.AutoField(primary_key=True)
    horas=models.TimeField()
    

class EstadoReserva(models.Model):
    id=models.AutoField(primary_key=True)
    reservaEstado= models.CharField(max_length=10)

class Calificacion(models.Model):
    id=models.AutoField(primary_key=True)
    rating=models.IntegerField()

