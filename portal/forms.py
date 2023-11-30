from django import forms
from .models import Item, Producto, Servicio, Persona

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"
