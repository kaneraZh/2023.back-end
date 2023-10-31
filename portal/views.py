from django.shortcuts import render
import portal.models as models
def main(request):
    data = {}
    data['productos'] = models.Producto.objects.all()
    data['servicios'] = models.Servicio.objects.all()
    return render(request, 'main.html', data)
