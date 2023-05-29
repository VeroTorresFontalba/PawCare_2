from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm , SetPasswordForm
from .models import User, Servicio
from .models import User, Categoria
from .models import User, Servicio, Profile
# , Categoria, Profile, 







class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                 'class': 'formulario__input',
                'placeholder': 'Contraseña',
                'minlength':'4',
                'maxlength':'12'
                
                 
            }
        )
    )


    password2 = forms.CharField(
        label='Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                 'class': 'formulario__input',
                'placeholder': 'Repetir Contraseña',
                'minlength':'4',
                'maxlength':'12'
            }
        )
    )



    class Meta:

        model = User 
        fields = (
            'username',
            'email',
            'rut',
            'nombres',
            'apellidos',
            'telefono',
            'categoria',
            )
        
        labels={
             'categoria':'Tipo de Usuario',
        }

        widgets = {
             'username': forms.TextInput(
                attrs={
                    'class': 'formulario__input',
                    'placeholder': 'Nombre de usuario...',
                    'minlength':'4',
                    'maxlength':'16'
                }
             ),
             'email': forms.EmailInput(
                attrs={
                     'class': 'formulario__input',
                     'placeholder': 'ejemplo@dominio.com',
                }
             ),
            'rut': forms.TextInput(
                attrs={
                    'class': 'formulario__input',
                    'placeholder': '112223334',
                    'maxlength':'9',
                    'onkeypress': 'return SoloNumeros(event);',
                    'type': 'text',
                    'onkeydown':'if(this.value.length == 9) return false;'
                    
                     
                }
             ),
            'nombres': forms.TextInput(
                attrs={
                     'class': 'formulario__input',
                     'placeholder': 'Ingresa tus nombre...',
                     'type':'text',
                     'onkeypress':'return SoloLetras(event);',
                }
             ),
            'apellidos': forms.TextInput(
                attrs={
                     'class': 'formulario__input',
                     'placeholder': 'Ingresa tus apellidos...',
                     'onkeypress':'return SoloLetras(event);'
                }
             ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'formulario__input',
                    'placeholder': '922644388',
                    'onkeypress': 'return SoloNumeros(event);',
                    'type': 'text',
                    'maxlength':'3',
                    'onkeydown':'if(this.value.length == 9) return false;'
                    
                    
                    
                }
             ),
             'categoria': forms.Select(
             attrs={
                  'class': 'formulario__input',
                  'id': 'categoria',
             }
             )
        }

    

    def clean_username(self):
         username= self.cleaned_data['username']
         existe = User.objects.filter(username=username).exists()
         if existe:
              raise ValidationError('El nombre de usuario ya existe')
         return username
        
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')

class LoginForm(forms.Form):
        username = forms.CharField(
        label='Nombre de usuario',
        required= True,
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su usuario',
                'style': '{margin: 10}',
            }
        )
    )
        password = forms.CharField(
        label='Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su contraseña',
            }
        )
    )
        
        def clean(self):
             cleaned_data = super(LoginForm, self).clean()
             username= self.cleaned_data['username']
             password= self.cleaned_data['password']

             if not authenticate(username=username, password=password):
                raise forms.ValidationError('Los datos de usuarios no son correctos')  
             return self.cleaned_data
        

        
class UserPasswordResetForm(PasswordResetForm):
    def init(self, args, **kwargs):
        super(UserPasswordResetForm, self).init(args, **kwargs)

    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'ejemplo@dominio.com',
        'type': 'email',
        'name': 'email'
        }))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label= ("Nueva Contraseña"),
        required= True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
              'class': 'form-control',
              'style': '{margin: 15}'}


    ))
    new_password2 = forms.CharField(
        label= ("Repita Nueva Contraseña"),
        required= True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña', 
            'class': 'form-control'
            }),
    )

class ServiciosForm(forms.ModelForm):
     class Meta:
          model = Servicio
          fields = ['id','nombre','informacion']
          labels = {
               'id': 'Numero del Servicio',
               'nombre':'Nombre del servicio',
               'informacion':'Informacion de servicios'
          }
          widgets = {
               'id':forms.TextInput(
                    attrs ={
                         'class':'form-control',
                         'placeholder':'Ingrese el numero del nuevo servicio'
                    }
               ),
               'nombre':forms.Textarea(
                    attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese el nombre del nuevo servicio'
                    }
               ),
               'informacion':forms.Textarea(
                    attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese una breve descripccion'
                    }
               )
          }


class PerfilForm(forms.ModelForm):
    picture = forms.ImageField(label='Nueva foto de perfil',required=False, widget=forms.FileInput(attrs={'class':'form-control'}))

    descripcion = forms.CharField(label= 'Ingresa una breve descripción',widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=260, required=False)

    servicios = forms.SelectMultiple(
        # label='',
        # required= True,
            attrs={
                    'class':'form-control',
                    'type':'checkbox'
            }
        
    )   
    class Meta:
        model = Profile
        fields = ('picture','descripcion','servicios')








# class PerfilForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('picture','descripcion','servicios')
#         label = {
#             'picture':'Imagen',
#             'descripcion': 'Bibliogrfia',
#             'servicios': 'Tipos de servicios'
#         }
#         widgets = {
#             'descripcion': forms.TextInput(
#                 attrs = {
#                     'class': 'form-control',
#                     'placeholder': 'Ingrese una breve descripción'
#                 }
#             ),
#             'servicios': forms.SelectMultiple(
#                 attrs = {
#                     'class':'form-control',
#                     'type':'checkbox'
#                 }
#             ),
#             'picture': forms.ImageField(
#                 attrs = {
#                     'class':'form-control'
#                 }
#             ),
#         }































    #     email = forms.EmailField(
    #     label='Correo',
    #     required= False,
    #     widget= forms.EmailField(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Ingrese un correo',
    #         }
    #     )
    # );
    #     telefono = forms.TextInput(
    #     label='Telefono',
    #     required= False,
    #     widget= forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Ingrese un telefono',
    #         }
    #     )
    # )
    #     picture = forms.ImageField(
    #          label='Profile picture',
    #          required= False,
    #          widget= forms.FileInput(
                  
    #          )
    #     )
    #     descripcion = forms.CharField(
    #     label='descripcion',
    #     widget= forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #         }
    #     )
    # )
     
    #     username = forms.CharField(
    #     label='Nombre de usuario',
    #     required= True,
    #     widget= forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Ingrese su usuario',
    #             'style': '{margin: 10}',
    #         }
    #     )
    # )
    #     password = forms.CharField(
    #     label='Contraseña',
    #     required= True,
    #     widget= forms.PasswordInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Ingrese su contraseña',
    #         }
    #     )
    # )
