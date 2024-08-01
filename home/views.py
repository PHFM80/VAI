from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home/home.html', {'active_page': 'home'})

def servicios_view(request):
    return render(request, 'home/servicios.html', {'active_page': 'servicios'})

def catalogos_view(request):
    return render(request, 'home/catalogos.html', {'active_page': 'catalogos'})

def contacto_view(request):
    return render(request, 'home/contacto.html', {'active_page': 'contacto'})

def acerca_view(request):
    return render(request, 'home/acercanuestro.html', {'active_page': 'acerca'})
