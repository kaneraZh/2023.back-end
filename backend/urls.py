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
import portal.views as views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='index'),

    path('producto', views.producto, name='producto'),
    path('producto/<int:pagina>/', views.producto, name='producto_explorador'),
    path('producto/detalle/<str:nombre>/', views.producto_detalle, name='producto_detalle'),
    
    path('servicio', views.servicio, name='servicio'),
    path('servicio/<int:pagina>/', views.servicio, name='servicio_explorador'),
    path('servicio/detalle/<str:nombre>/', views.servicio_detalle, name='servicio_detalle'),
    
    path('persona/<str:persona>/', views.persona)
]
