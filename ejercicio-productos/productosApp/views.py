from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')

def electronica(request):
  data = {
    'titulo':'electronica',
    'producto1':'Pantalones',
    'producto2':'Chaqueta',
    'producto3':'Camisa',
  }
  return render(request, 'productos.html', data)
def juguetes(request):
  data = {
    'titulo':'juguetes',
    'producto1':'123',
    'producto2':'123',
    'producto3':'123',
  }
  return render(request, 'productos.html', data)
def ropa(request):
  data = {
    'titulo':'Ropa',
    'producto1':'abc',
    'producto2':'abc',
    'producto3':'abc',
  }
  return render(request, 'productos.html', data)
