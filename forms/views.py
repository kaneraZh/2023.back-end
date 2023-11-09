from django.shortcuts import render
import forms.forms as forms

def index(request):
    form = forms.UserRegistrationForm()
    if(request.method=='POST'):
        form = forms.UserRegistrationForm(request.POST)
        if(form.is_valid()):
            print('Formulario OK')
            print('Nombre: ', form.cleaned_data['nombre'])
            print('Email: ', form.cleaned_data['email'])
            print('Fono: ', form.cleaned_data['fono'])
    data = {'form' : form}
    return render(request, 'index.html', data)
