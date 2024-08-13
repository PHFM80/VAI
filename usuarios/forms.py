from django import forms
from .models import UsuarioVai, Rol, Cargo


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class RegistroUsuarioForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label='Nombres')
    last_name = forms.CharField(max_length=30, label='Apellidos')
    email = forms.EmailField(max_length=254, label='Correo Electrónico')
    telefono = forms.CharField(max_length=20, required=False, label='Teléfono')
    rol = forms.ModelChoiceField(queryset=Rol.objects.all(), label='Rol')
    cargo = forms.ModelChoiceField(queryset=Cargo.objects.all(), label='Cargo')

    class Meta:
        model = UsuarioVai
        fields = ['first_name', 'last_name', 'email', 'telefono', 'rol', 'cargo']

class BuscarUsuarioForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario', max_length=150)














