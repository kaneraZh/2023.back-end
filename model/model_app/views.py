from django.shortcuts import render

from model_app.models import Empleado
# Create your views here.
def empleados_data(request):
    empleados = Empleado.objects.all()
    data = {'empleados':empleados}
    return render(request, 'empleados.html', data)