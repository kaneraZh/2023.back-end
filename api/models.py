from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f'{self.id}-{self.name} : ${self.salary}'

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f'{self.id}-{self.name} : #{self.score}'