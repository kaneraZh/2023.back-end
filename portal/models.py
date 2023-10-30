from django.db import models

class Item(models.Model):
    def __str__(self):return self.name
    def get_absolute_url(self):return reverse("item_detail", kwargs={"pk": self.pk})
    nombre      = models.CharField(max_length=20)
    precio      = models.IntegerField()
    descripcion = models.CharField(max_length=150, default="")

class Producto(models.Model):
    def __str__(self):return self.name
    def get_absolute_url(self):return reverse("producto_detail", kwargs={"pk": self.pk})
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    stock= models.IntegerField()

class Servicio(models.Model):
    def __str__(self):return self.name
    def get_absolute_url(self):return reverse("servicio_detail", kwargs={"pk": self.pk})
    item    = models.ForeignKey(Item,on_delete=models.CASCADE)
    tiempo  = models.TimeField(auto_now=False, auto_now_add=False)
    

class Persona(models.Model):
    def __str__(self):return self.name
    def get_absolute_url(self):return reverse("persona_detail", kwargs={"pk": self.pk})
    nombre      = models.CharField(max_length=20)
    correo      = models.CharField(max_length=50)
    productos   = models.ManyToManyField(Producto)
    servicios   = models.ManyToManyField(Servicio)
