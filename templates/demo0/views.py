from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    data={
        'nombre' : 'Lala',
        'apellido' : 'Dog'
    }
    return render(request, 'demo0\demo.html', data)