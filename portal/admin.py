from django.contrib import admin

from portal.models import Producto
from portal.models import Servicio
from portal.models import Persona
admin.site.register(Producto)
admin.site.register(Servicio)
admin.site.register(Persona)
