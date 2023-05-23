# from django.db import models
# from applications.users.models import User
# from django.contrib.auth.models import AbstractBaseUser
# from django.db.models.signals import post_save
# # Create your models here.

# #Modelo de Tipos de servicios
# class Tservicio(models.Model):
#     nombre = models.CharField(max_length=80, unique= True,verbose_name='Tipo de servicio')

#     class Meta:
#         verbose_name = 'Tipo de servicio'
#         verbose_name_plural ='Tipos de servicios'
#         ordering = ['nombre']
#     def __str__(self):
#         return self.nombre


# class Profile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile'), #mañana veelo
#     image = models.ImageField(default='users/image_user.png',upload_to='users/'),
#     descripccion = models.TextField(max_length=500,null=True, blank=True)
#     servicios = models.ManyToManyField(Tservicio,verbose_name='Tipos de servicios')

#     class Meta:
#         verbose_name = 'Perfil'
#         verbose_name_plural = 'Perfiles'
#         ordering = ['-id']

# def create_users_profile(sender, instance, created,**kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# def save_users_profile(sender, instance,**kwargs):
#     instance.profile.save()

# # post_save.connect(create_users_profile,sender=User)
# # post_save.connect(save_users_profile,sender=User)#mañan veelo