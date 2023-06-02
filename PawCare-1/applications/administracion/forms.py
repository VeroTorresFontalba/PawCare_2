from django import forms
from .models import Colaboradores

class ColaboradorForm(forms.ModelForm):

    class Meta:
        model= Colaboradores
        fields = ['title','image','content','descuento','url','published']
        labels = {
            'title':'Ingrese el nombre del Colaborador',
            'image':'Imagen del Colaborador',
            'content':'Descripccion del Colaborador',
            'descuento':'Ingrese el codigo de descuento del Colaborador',
            # 'url':'Ingrese el sitio web del Colaborador',
            'published':'Publicar',
        }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'descuento':forms.TextInput(attrs={'class':'form-control'}),
            'url':forms.TextInput(attrs={'class':'form-control'}),
            # 'published':forms.BooleanField(required=True,label='Deseas ocultarlo',label_suffix='',initial=True,error_messages={'required':'Porfavor selecciona un estado'}),

            # 'url':forms.URLField(),
            # 'published':forms.BooleanField(),
        }