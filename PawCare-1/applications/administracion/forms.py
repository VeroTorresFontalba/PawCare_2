from django import forms
from .models import Colaboradores

class ColaboradorForm(forms.ModelForm):

    class Meta:
        model= Colaboradores
        fields = ['title','image','content','descuento','url','published']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'descuento':forms.Textarea(attrs={'class':'form-control'}),


            # 'url':forms.URLField(),
            # 'published':forms.BooleanField(attrs={'class':'form-control'}),
        }