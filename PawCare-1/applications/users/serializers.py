from rest_framework import serializers

from .models import Mascota

class MascotaSerializers(serializers.ModelSerializer):

    class Meta:
        model= Mascota 
        fields= (
            'id',
            'user',
            'nombre_de_mascota',
            'chip',
            'n_chip',
            'image',
            'descripccion',
            'especies',
            
            )