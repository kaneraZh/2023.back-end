from django.db import models

class Item(models.Model):
    def __str__(self):return self.nombre
    def get_absolute_url(self):return reverse("item_detail", kwargs={"pk": self.pk})
    nombre      = models.CharField(max_length=20)
    precio      = models.IntegerField()
    descripcion = models.CharField(max_length=150, default="")
    def __str__(self):return self.nombre
class Producto(Item):
    #def __str__(self):return f'{self.nombre}, {self.precio}, {self.descripcion}, {self.stock}'
    def get_absolute_url(self):return reverse("producto_detail", kwargs={"pk": self.pk})
    stock = models.IntegerField()
class Servicio(Item):
    #def __str__(self):return f'{self.nombre}, {self.precio}, {self.descripcion}, {self.tiempo}'
    def get_absolute_url(self):return reverse("servicio_detail", kwargs={"pk": self.pk})
    tiempo = models.DurationField()
class Persona(models.Model):
    def __str__(self):return f'{self.nombre}, {self.correo}, productos: {self.productos.count()}, servicios: {self.servicios.count()}'
    def get_absolute_url(self):return reverse("persona_detail", kwargs={"pk": self.pk})
    nombre      = models.CharField(max_length=20)
    correo      = models.CharField(max_length=50)
    productos   = models.ManyToManyField(Producto)
    servicios   = models.ManyToManyField(Servicio)
