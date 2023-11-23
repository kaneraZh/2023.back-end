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
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path("proyectos/", views.proyectos_listado, name="proyectos_ver"),
    path("proyecto/agregar", views.proyecto_agregar, name="proyecto_agregar"),
    path("proyecto/eliminar/<int:id>", views.proyecto_eliminar, name="proyecto_eliminar"),
    path("proyecto/actualizar/<int:id>", views.proyecto_actualizar, name="proyecto_actualizar"),
]
