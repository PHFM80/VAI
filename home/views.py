from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from home.forms import FormularioContacto

# Create your views here.

def home_view(request):
    return render(request, 'home/home.html', {'active_page': 'home'})

def servicios_view(request):
    return render(request, 'home/servicios.html', {'active_page': 'servicios'})

def catalogos_view(request):
    return render(request, 'home/catalogos.html', {'active_page': 'catalogos'})

def contacto_view(request):
    mensaje_enviado = False
    if request.method == 'POST':
        miFormulario = FormularioContacto(request.POST)
        if miFormulario.is_valid():
            infoForm = miFormulario.cleaned_data
            send_mail(
                infoForm['asunto'],
                f"Nombre: {infoForm['nombre']}\nTeléfono: {infoForm['telefono']}\nEmpresa: {infoForm['empresa']}\nMensaje: {infoForm['mensaje']}",
                infoForm.get('email', ''),  # Remitente
                ['contacto.vaiprocess@gmail.com', 'pablofloresmaza@gmail.com'],  # Destinatarios en una lista
            )
            mensaje_enviado = True
            miFormulario = FormularioContacto()  # Reiniciar el formulario después de enviar
    else:
        miFormulario = FormularioContacto()
    context = {
        "form": miFormulario,
        'active_page': 'contacto',
        'mensaje_enviado': mensaje_enviado,
    }
    return render(request, 'home/contacto.html', context)

def acerca_view(request):
    return render(request, 'home/acerca-nuestro.html', {'active_page': 'acerca'})
