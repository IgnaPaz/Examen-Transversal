from django import forms
from .models import Catalogo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CatalogoForm(forms.ModelForm):
    class Meta:
        model = Catalogo
        fields = ['nombre', 'precio', 'imagen']

class LoginForm(forms.Form):
    correo = forms.EmailField(label="Correo electrónico", max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    contraseña = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    edad = forms.IntegerField(min_value=18, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("username", "email", "edad", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }