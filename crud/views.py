from django.shortcuts import render
from crud import models, forms

def index(request):
    return render(request, 'index.html')

def proyectos_listado(request):
    proyectos = models.Proyecto.objects.all()
    data = {'proyectos' : proyectos}
    return render(request, 'proyectos.html', data)

def proyecto_agregar(request):
    form = forms.ProyectoForm()
    if(request.method=='POST'):
        form = forms.ProyectoForm(request.POST)
        if(form.is_valid()): form.save()
        return index(request)
    data = {'form':form}
    return render(request, 'proyecto_agregar.html', data)
def proyecto_eliminar(request, id):
    proyecto = models.Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect('/proyectos')
def proyecto_actualizar(request, id):
    proyecto = models.Proyecto.objects.get(id=id)
    form = forms.ProyectoForm(instance=proyecto)
    if(request.method=='POST'):
        form = forms.ProyectoForm(request.POST, instance=proyecto)
        if(form.is_valid()):
            form.save()
        return index(request)
    data = {'form':form}
    return render(request, 'proyecto_actualizar.html', data)
