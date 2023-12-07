from django.shortcuts import render
from django.http import JsonResponse

from .models import Employee
def employeeView(request):
    empleados = Employee.objects.all()
    data = {
        'employees' : list(empleados.values('name', 'salary'))
    }
    return JsonResponse(data)
