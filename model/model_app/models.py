from django.db import models

class Emplado(models.Model):
    nombre  = models.CharField(max_length=50)
    email   = models.CharField(max_length=50)
    fono    = models.CharField(max_length=15)
