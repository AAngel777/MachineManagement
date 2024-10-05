# views.py
from django.shortcuts import render

def maquinaria(request):
    return render(request, 'maquinaria/maquinaria.html')  # Renderiza la plantilla maquinaria.html

def inventario(request):
    return render(request, 'inventario/inventario.html')

def status(request):
    return render(request, 'status/status.html')

def empleados(request):
    return render(request, 'empleados/empleados.html')
    
def empresa(request):
    return render(request, 'empresa/empresa.html')

def home(request):
    return render(request, 'home/index.html')