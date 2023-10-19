from django.shortcuts import render

from model_app.models import Emplado
# Create your views here.
def empleados_data(request):
    empleados = Emplado.objects.all()
    data = {'empleados':empleados}
    return render(request, 'empleados.html', data)