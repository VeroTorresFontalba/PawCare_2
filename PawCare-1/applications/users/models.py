from datetime import date
import datetime
from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin
from django.db.models.signals import post_save 

from .managers import UserManager ,MascotaManager,HorasManager,HorasSolicitadasManager

from applications.categoria.models import Categoria

# Create your models here.
class User (AbstractBaseUser, PermissionsMixin, models.Model ):

    # TIPO DE USUARIOS
    CLIENTE = '1' 
    CUIDADOR = '2'
    ADMINISTRADOR= '3'
    TIPOUSER_CHOICES = [
        (CLIENTE, 'Cliente'),
        (CUIDADOR, 'Cuidador'),
        (ADMINISTRADOR, 'Administrador'),
    ]

    username = models.CharField(max_length=16, unique=True)
    email = models.EmailField()
    rut = models.CharField(max_length=9, null= True)
    nombres= models.CharField(max_length=100)
    apellidos= models.CharField(max_length=100)
    telefono= models.CharField(max_length=9,null = True)
    # tipodeusuario=models.CharField(max_length=2,choices=TIPOUSER_CHOICES,null=True,default=2)
    # categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,null=True)
    categoria = models.CharField(max_length=2,choices=TIPOUSER_CHOICES,null=True,default=1)
    promediocalificacion = models.DecimalField(max_digits=3, decimal_places=2, null=True)
 
    #
    is_staff = models.BooleanField(default=False) #para especificar si el usuario es administrador
    is_active= models.BooleanField(default=True)   
    USERNAME_FIELD ='username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()
    def __str__(self):
        return str(self.id)+"-"+str(self.username) 

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


class EstadoReserva(models.Model):
    id=models.AutoField(primary_key=True)
    reservaEstado= models.CharField(max_length=15)
    def __str__(self):
        return str(self.id) + "-" +str(self.reservaEstado) 
    
class Hora(models.Model):
    id=models.AutoField(primary_key=True)
    horaInicio=models.TimeField(verbose_name='inicio')
    horaFin=models.TimeField(null=True,verbose_name='fin')
    # estado= models.ForeignKey(EstadoReserva,on_delete=models.CASCADE,related_name='Estado',null=True,default=1)

    def __str__(self):
        return  str(self.id) + " - " +str(self.horaInicio) + " - " +str(self.horaFin) 
    
class Cronograma(models.Model):
     id= models.AutoField(primary_key=True)
     user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='cronograma', null=True)
     fechaReserva=models.DateField('Dia',null=True,blank=True,default=date.today)
    #  horas=models.ManyToManyField(Hora,related_name='horas',verbose_name='Horas a seleccionar')
     horas=models.ForeignKey(Hora,on_delete=models.CASCADE,related_name='horas',verbose_name='Hora a seleccionar',null=True, default=2)
     estado= models.ForeignKey(EstadoReserva,on_delete=models.CASCADE,related_name='Estado',null=True,default=1)
    
     objects = HorasManager()

     def __str__(self):
        return str(self.fechaReserva) +"/"+ str(self.user)+"/"+ str(self.estado)
     


     

# def create_user_cronograma(sender, instance, created, **kwargs):
#     if created:
#         Cronograma.objects.create(user=instance)


# def save_user_cronograma(sender, instance, **kwargs):
#     instance.cronograma.save()

# # created profile
# post_save.connect(create_user_cronograma, sender=User)
# # save created profile
# post_save.connect(save_user_cronograma, sender=User)

    

#Reserva
#Esta tabla debe ser llanda por nostros
# class EstadoReserva(models.Model):
#     id=models.AutoField(primary_key=True)
#     reservaEstado= models.CharField(max_length=15)
#     def __str__(self):
#         return self.reservaEstado 
 
# class DiaReserva(models.Model):
#     id=models.AutoField(primary_key=True)
#     fechaReserva=models.DateField('Dia',null=True,blank=True,default=date.today)
#     horaInicio=models.TimeField(verbose_name='inicio')
#     horaFin=models.TimeField(null=True,verbose_name='fin')
#     estado= models.ForeignKey(EstadoReserva,on_delete=models.CASCADE,related_name='Estado',null=True)

#     objects = HoraManager()

#     def __str__(self):
#         return str(self.fechaReserva) + "/ " + str(self.horaInicio) + "-"+ str(self.horaFin) 


# class Hora(models.Model):
#     id=models.AutoField(primary_key=True)
#     horas=models.TimeField()
    



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
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='Dueño',null=True,blank=True)
    nombre_de_mascota = models.CharField(max_length=50, blank= True, null=True)
    chip= models.CharField(max_length=2 ,verbose_name='Chip', choices=IS_PUBLISHED_CHOICES, default='NO')
    n_chip= models.CharField(max_length=50, blank= True, null=True, default='No poose')
    image = models.ImageField(upload_to='mascotas' ,null=True, blank=True, verbose_name='Imagen del la Mascota')
    descripccion = models.TextField(verbose_name='Descripccion del la mascota')
    especies=models.ForeignKey(Especies,related_name='especies',verbose_name='Tipos de mascota',on_delete=models.CASCADE,null=True,default=1)

   

    class Meta:
        verbose_name = 'mascota'
        verbose_name_plural ='mascotas'
        ordering = ['id']

    objects = MascotaManager()
    
    def __str__(self):
        return  str(self.nombre_de_mascota)+"/"+str(self.user)

                                         
class ReservaCliente(models.Model):
    id= models.AutoField(primary_key=True)
    clienteusername=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='Usuario',null=True,blank=True)
    idCronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE,related_name='reservas',null=True,blank=True)
    correocuidaor=models.CharField(max_length=100,null=True, blank=True)
    correocliente=models.CharField(max_length=100,null=True, blank=True)
    idCuidador=models.CharField(max_length=100,null=True, blank=True)
    idCliente=models.CharField(max_length=100, null=True, blank=True)
    nombreCliente=models.CharField(max_length=100, null=True, blank=True)
    nombreCuidador=models.CharField(max_length=100, null=True, blank=True)
    fechareserva=models.CharField( max_length=100,null=True, blank=True)
    horasInicio=models.CharField(max_length=100, null=True, blank=True)
    horasFin=models.CharField( max_length=100,null=True, blank=True)
    calificacion=models.CharField(max_length=10, null=True, blank=True)

    objects = HorasSolicitadasManager()

    def __str__(self):
        return  str(self.nombreCuidador)+"/"+str(self.nombreCliente)

#str(self.nombreCuidador)+"/"+str(self.nombreCliente)
    # idCuidador=models.IntegerField(unique=True ,null=True, blank=True)
    # cuidador=models.CharField(max_length=16, null=True, blank=True)
    # idCliente=models.IntegerField(unique=True ,null=True, blank=True)
    # cliente=models.CharField(max_length=16, null=True, blank=True)
    # idReserva= models.IntegerField(unique=True ,null=True, blank=True)
    # fechaReserva=models.DateField(null=True,blank=True)
    # estado=models.CharField(max_length=15,null=True,blank=True)  


    

