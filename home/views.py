from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home/home.html')

def servicios_view(request):
    return render(request, 'home/servicios.html')

def catalogos_view(request):
    return render(request, 'home/catalogos.html')

def contacto_view(request):
    return render(request, 'home/contacto.html')


