from django import forms
from apps.Usuario.models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'punto_control',
            'documento',
        ]
        label = {
            'punto_control':'Punto Control',
            'documento':'Documento',
        }
        widgets = {
			'punto_control': forms.Select(attrs={'class': 'selectpicker', 'data-size':"7", "data-style":"btn btn-primary btn-round"}) ,
			'documento': forms.TextInput(attrs={'class': 'form-control', 'required':'required'}) ,
		}

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        label = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Direccion de correo electronico',
        }
        widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control', 'required':'required'}) ,
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required':'required'}) ,
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required':'required'}) ,
            'email': forms.TextInput(attrs={'class': 'form-control', 'required':'required'}) ,
		}