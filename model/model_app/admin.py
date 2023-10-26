from django.contrib import admin

# Register your models here.
from model_app.models import Empleado
admin.site.register(Empleado)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ["nombre","email","fono"]