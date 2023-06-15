from django.db import models
from .managers import ColabManager
# Create your models here.


#Esta tabla debe ser llanada por nosotros
class Colaboradores(models.Model):

    IS_PUBLISHED_CHOICES = [
        ('No','No '), 
        ('Si', 'Si')]

    title = models.CharField(max_length= 100, verbose_name='Nombre del Patrocinador')
    image = models.ImageField(upload_to='colaboradores' ,null=True, blank=True, verbose_name='Imagen del Patrocinador')
    content = models.TextField(verbose_name='Descripccion del Colaborador')
    descuento = models.CharField(max_length=100,null=True,verbose_name='Codigo de descuento') 
    url = models.URLField(max_length=350, blank=True, null=True, verbose_name='Enlace' , default= 'http://127.0.0.1:8000/colab/')
    published = models.BooleanField(default=True, verbose_name='Publicado')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha en las que se nos unio')

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
        ordering = ['-created']

    objects = ColabManager()

    def __str__(self):
        return self.title