from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin
from django.db.models.signals import post_save 

from .managers import UserManager , HoraManager

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

# Agregar una columna de valor x servicio que vamos a definir nosotros

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


#Reserva
#Esta tabla debe ser llanda por nostros
class EstadoReserva(models.Model):
    id=models.AutoField(primary_key=True)
    reservaEstado= models.CharField(max_length=15)
    def __str__(self):
        return self.reservaEstado 
 
class DiaReserva(models.Model):
    id=models.AutoField(primary_key=True)
    fechaReserva=models.DateField('Dia',auto_now=False,auto_now_add=True,null=True,blank=True)
    horaInicio=models.TimeField(verbose_name='inicio')
    horaFin=models.TimeField(null=True,verbose_name='fin')
    estado= models.ForeignKey(EstadoReserva,on_delete=models.CASCADE,related_name='Estado',null=True)

    objects = HoraManager()

    def __str__(self):
        return str(self.fechaReserva) + "/ " + str(self.horaInicio) + "-"+ str(self.horaFin) 


class Hora(models.Model):
    id=models.AutoField(primary_key=True)
    horas=models.TimeField()
    



class Calificacion(models.Model):
    id=models.AutoField(primary_key=True)
    rating=models.IntegerField()




#MASCOTAS
#Esta tabla debe ser llenada por nosotros
class Especies(models.Model):
    id= models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=80, unique= True,verbose_name='Tipo de mascota')


    class Meta:
        verbose_name = 'especie'
        verbose_name_plural ='especies'
        ordering = ['id']
    def __str__(self):
        return self.nombre 



class Mascota(models.Model):

    IS_PUBLISHED_CHOICES = [
        ('No','No'), 
        ('Si', 'Si')]

    id= models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Dueño',null=True,blank=True)
    nombre_de_mascota = models.CharField(max_length=50, blank= True, null=True)
    chip= models.CharField(max_length=2 ,verbose_name='Chip', choices=IS_PUBLISHED_CHOICES, default='NO')
    n_chip= models.CharField(max_length=50, blank= True, null=True)
    image = models.ImageField(upload_to='mascotas' ,null=True, blank=True, verbose_name='Imagen del la Mascota')
    descripccion = models.TextField(verbose_name='Descripccion del la mascota')
    especies=models.ForeignKey(Especies,related_name='especies',verbose_name='Tipos de mascota',on_delete=models.CASCADE,null=True,default=1)

   

    class Meta:
        verbose_name = 'mascota'
        verbose_name_plural ='mascotas'
        ordering = ['id']

    
    
    def __str__(self):
        return  self.nombre_de_mascota

                                         

