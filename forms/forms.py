from django import forms
from django.core import validators
ESTADOS = [
    ('activo', 'ACTIVO')
    ('inactivo', 'INACTIVO')
]

class UserRegistrationForm(forms.Form):
    nombre = forms.CharField()
    fono = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput())
    estado = forms.CharField(widget = forms.select(choices = ESTADOS))
    
    nombre  = 
    fono    = 
    email   = 
    password= 
    estado  = 