from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name= 'id')
    name = models.CharField('Tipo de Usuario',max_length=20)
    short_name = models.CharField('Sigla',max_length=2)
    
    # def __str__(self):
        # return str(self.id) + '-' + self.name + ' - ' + self.short_name
    
    def __str__(self):
        return self.name 