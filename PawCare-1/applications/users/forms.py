from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm , SetPasswordForm
# from .models import Cronograma, User, Servicio
# from .models import User, Categoria
from .models import User, Servicio, Profile,Mascota, Cronograma,Especies,Hora,ReservaCliente
# , Categoria, Profile, ReservaCliente







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
            'is_active',
            )
        
        labels={
             'is_active':'Bajar cuenta',
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
               'nombre':forms.TextInput(
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

class EspeciesForm(forms.ModelForm):
     class Meta:
          model = Especies
          fields = ['id','nombre']
          labels = {
               'id': 'Identificador del la especie',
               'nombre':'Nombre de la especie',

          }
          widgets = {
               'id':forms.TextInput(
                    attrs ={
                         'class':'form-control',
                         'placeholder':'Ingrese el numero de la nueva especie'
                    }
               ),
               'nombre':forms.TextInput(
                    attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese el nombre de la nueva especie'
                    }
               ),
          }



class PerfilForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('picture','descripcion','servicios')

    picture = forms.ImageField(label='Nueva foto de perfil',required=False, widget=forms.FileInput(attrs={'class':'form-control'}))

    descripcion = forms.CharField(label= 'Ingresa una breve descripción',widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=260, required=False)

    servicios = forms.ModelMultipleChoiceField(
         queryset= None,
         required=False,
         widget=forms.CheckboxSelectMultiple()
    )
    def __init__(self,*args,**kwargs):
         super(PerfilForm, self).__init__(*args,**kwargs)
         self.fields['servicios'].queryset = Servicio.objects.all() 

class MascotaForm(forms.ModelForm):

    class Meta:
        model= Mascota
        fields = ['nombre_de_mascota','chip','n_chip','image','descripccion','especies']
        labels = {
            # 'dueño':'Dueños de Mascota',
            'nombre_de_mascota':'Nombre de la mascota',
            'chip':'Posee chip',
            'n_chip':'Ingrese el numero de Chip',
            'image':'Ingrese una foto de su mascota',
            'descripccion':'Detalle una descripccion de su mascota',
            'especies':'A que especie pertenece su mascota',
        }
        widgets = {
            # 'dueño':forms.TextInput(attrs={'class':'form-control'}),
            'nombre_de_mascota':forms.TextInput(attrs={'class':'form-control'}),
            'n_chip':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'descripccion':forms.Textarea(attrs={'class':'form-control'}),
            'especies': forms.Select(attrs={'class': 'form-control',
             }
             )
        }


class CronogramaForm(forms.ModelForm):
    class Meta:
        model = Cronograma
        fields = ('fechaReserva','horas')
        widgets = {
               'fechaReserva':forms.DateInput(
                    format= '%Y-%m-%d',
                    attrs ={
                         'type': 'date',
                         'class':'form-control',

                    }
               ),
               'horas':forms.Select(
                   attrs={
                       'class': 'form-control',
                }
             ),
        }
    # horas = forms.ModelMultipleChoiceField(
    #      queryset= None,
    #      required=False,
    #      widget=forms.CheckboxSelectMultiple()
    # )
    # def __init__(self,*args,**kwargs):
    #      super(CronogramaForm, self).__init__(*args,**kwargs)
    #      self.fields['horas'].queryset = Hora.objects.all() 


class ReservaForm(forms.ModelForm):
    class Meta:
        model = ReservaCliente
        fields = ('correocuidaor','correocliente','idCuidador','idCliente','nombreCliente','nombreCuidador','fechareserva','horasInicio','horasFin')
        widgets = {
               'correocuidaor':forms.TextInput(
                    # attrs ={
                    #      'class':'form-control',
                    #      'type':'hidden'
                         
                    # }
               ),
                'correocliente':forms.TextInput(
                    # attrs ={
                    #      'class':'form-control',
                    #       'type':'hidden'
                         
                    # }
               ),
                'idCuidador':forms.TextInput(
                    # attrs ={
                    #      'class':'form-control',
                    #       'type':'hidden'
                         
                    # }
               ),
                'idCliente':forms.TextInput(
                    # attrs ={
                    #      'class':'form-control',
                    #       'type':'hidden'
                        
                    # }
               ),
                'nombreCliente':forms.TextInput(
                    # attrs ={
                    #      'class':'form-control',
                    #       'type':'hidden'
                         
                    # }
               ),
                'nombreCuidador':forms.TextInput(
                    # attrs ={
                    #      'class':'form-control',
                    #       'type':'hidden'
                         
                    # }
               ),
                'fechareserva':forms.TextInput(
                    # attrs ={
                    #      'class':'form-control',
                    #       'type':'hidden'
                   
                    # }
               ),
                'horasInicio':forms.TextInput(
                    # attrs ={
                    #      'class':'form-control',
                    #       'type':'hidden'
                         
                    # }
               ),
                'horasFin':forms.TextInput(
                #     attrs ={
                #          'class':'form-control',
                #           'type':'hidden'
                         
                #     }
               ),

        }


        #           widgets = {
        #        'id':forms.TextInput(
        #             attrs ={
        #                  'class':'form-control',

        #                  'placeholder':'Ingrese el numero de la nueva especie'
        #             }
        #        ),
        #        'nombre':forms.TextInput(
        #             attrs={
        #                  'class':'form-control',
        #                  'placeholder':'Ingrese el nombre de la nueva especie'
        #             }
        #        ),
        #   }


