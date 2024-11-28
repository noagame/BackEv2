# Creacion de formularios
from django.contrib.auth.models import User
from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cliente_id', 'edad', 'genero', 'saldo', 'active', 'nivel_de_satisfaccion']
        widgets = {
            'cliente_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del Cliente'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'saldo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Saldo'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nivel_de_satisfaccion': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Nivel de Satisfacción'}),
        }
        # Etiquetas de formulario
        labels = {
            'cliente_id': 'ID del Cliente',
            'edad': 'Edad',
            'genero': 'Género',
            'saldo': 'Saldo',
            'active': 'Activo',
            'nivel_de_satisfacción': 'Nivel de Satisfacción',
        }
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'password': 'Contraseña'
        }
        help_texts = {
            'username': '',  # Esto elimina el texto de ayuda predeterminado
            'password': ''   # Limpia cualquier ayuda extra para la contraseña
        }
        widgets = {
            'password2': forms.PasswordInput(),  # Asegura el tipo de campo para la contraseña
        }