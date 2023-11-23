from django import forms
from crud import models

class ProyectoForm(forms.Form):
    class Meta:
        model = models.Proyecto
        fields = '__all__'
