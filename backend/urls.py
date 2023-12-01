"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import portal.views as portal
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portal.main, name='index'),

    path('producto', portal.producto, name='producto'),
    path('producto/<int:page>/', portal.producto, name='producto_explorador'),
    #path('producto/detalle/<str:nombre>/', portal.producto_detalle, name='producto_detalle'),
    
    path('servicio', portal.servicio, name='servicio'),
    path('servicio/<int:page>/', portal.servicio, name='servicio_explorador'),
    #path('servicio/detalle/<str:nombre>/', portal.servicio_detalle, name='servicio_detalle'),
    
    path('persona/ver/<int:pk>/', portal.persona, name='persona_ver'),
    path('persona/agregar/', portal.persona_agregar, name='persona_agregar'),
    path('persona/modificar/<int:pk>/', portal.persona_modificar, name='persona_modificar'),
    path('persona/eliminar/<int:pk>/', portal.persona_eliminar, name='persona_eliminar'),
    path('persona/lista/', portal.persona_lista, name='persona_lista'),

    path('producto/ver/<int:pk>/', portal.producto_detalle, name='producto_ver'),
    path('producto/agregar/', portal.producto_agregar, name='producto_agregar'),
    path('producto/modificar/<int:pk>/', portal.producto_modificar, name='producto_modificar'),
    path('producto/eliminar/<int:pk>/', portal.producto_eliminar, name='producto_eliminar'),
    path('producto/lista/', portal.producto_lista, name='producto_lista'),
    
    path('servicio/ver/<int:pk>/', portal.servicio_detalle, name='servicio_ver'),
    path('servicio/agregar/', portal.servicio_agregar, name='servicio_agregar'),
    path('servicio/modificar/<int:pk>/', portal.servicio_modificar, name='servicio_modificar'),
    path('servicio/eliminar/<int:pk>/', portal.servicio_eliminar, name='servicio_eliminar'),
    path('servicio/lista/', portal.servicio_lista, name='servicio_lista'),
]
