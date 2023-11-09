from django.db import models

class Employee(models.Model):
    class Meta:
        verbose_name = "employee"
        verbose_name_plural = "employees"
    def __str__(self):return self.nombre
    def get_absolute_url(self):return reverse("employee_detail", kwargs={"pk": self.pk})
    nombre = models.CharField(max_length=50)
    fono = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
