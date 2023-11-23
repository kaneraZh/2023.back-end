from django.db import models

class Proyecto(models.Model):
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
    def __str__(self):return self.titulo
    def get_absolute_url(self):return reverse("proyecto_detail", kwargs={"pk": self.pk})

    titulo = models.CharField(max_length=50)
    tiempo_ejecucion = models.DurationField()
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
