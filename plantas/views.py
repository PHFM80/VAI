from django.shortcuts import render, redirect, get_object_or_404
from .models import Planta, Empresa
from .forms import EmpresaForm, PlantaForm, TipoSensorForm, SensorForm, Estacion, ModeloE
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import generar_codigo_qr

@login_required
def agregar_empresa_view(request):
    next_url = request.GET.get('next', '/dashboard/')  # Obtiene la URL de la página anterior o por defecto el dashboard

    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(next_url)  # Redirige a la URL anterior
    else:
        form = EmpresaForm()

    return render(request, 'plantas/crud-plantas/agregar-empresa.html', {'form': form})

@login_required
def agregar_planta_view(request):

    next_url = request.GET.get('next', '/dashboard/')  # Obtiene la URL de la página anterior o por defecto redirige al dashboard

    if request.method == 'POST':
        form = PlantaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(next_url)  # Redirige a la URL anterior o al dashboard por defecto
    else:
        form = PlantaForm()

    return render(request, 'plantas/crud-plantas/agregar-planta.html', {'form': form})

@login_required
def eliminar_planta_view(request):
    empresas = Empresa.objects.all()
    plantas = []

    if request.method == 'GET':
        empresa_id = request.GET.get('empresa')
        if empresa_id:
            plantas = Planta.objects.filter(empresa_id=empresa_id)

    if request.method == 'POST':
        planta_id = request.POST.get('planta_id')
        if planta_id:
            planta = Planta.objects.get(id=planta_id)
            planta.delete()
            return redirect('dashboard')  # Redirige a la misma vista para actualizar la lista

    return render(request, 'plantas/crud-plantas/eliminar-planta.html', {
        'empresas': empresas,
        'plantas': plantas,
    })

@login_required
def agregar_tipo_sensor_view(request):
    next_url = request.GET.get('next', '/dashboard/')

    if request.method == 'POST':
        form = TipoSensorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(next_url)  # Redirige a la URL obtenida o al dashboard
    else:
        form = TipoSensorForm()

    return render(request, 'plantas/crud-sensores/agregar-tipo-sensor.html', {'form': form, 'next_url': next_url})

@login_required
def agregar_sensor_view(request):
    next_url = request.GET.get('next', '/dashboard/')

    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            sensor = form.save(commit=False)
            
            # Generar el código QR en el backend
            data_qr = f'ID: {sensor.id}, Tipo: {sensor.tipo.nombre}, Descripción: {sensor.descripcion}'
            sensor.codigo_qr = generar_codigo_qr(data_qr)
            
            # Guardar el sensor con el QR generado
            sensor.save()
            return redirect(next_url)
    else:
        form = SensorForm()

    return render(request, 'plantas/crud-sensores/agregar-sensor.html', {'form': form, 'next_url': request.path})

@login_required
@csrf_exempt
def generate_qr_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tipo = data.get('tipo')
        descripcion = data.get('descripcion')
        
        # Genera el texto del QR basado en el tipo y la descripción
        data_qr = f'Tipo: {tipo}, Descripción: {descripcion}'
        qr_code = generar_codigo_qr(data_qr)
        
        # Retorna la imagen del QR en base64
        return JsonResponse({'qr_image': qr_code})
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)














@login_required
def agregar_estacion_view(request):
    if request.method == 'POST':
        planta_id = request.POST.get('planta')
        modelo_id = request.POST.get('modelo')
        codigo_barras = request.POST.get('codigo_barras')

        planta = Planta.objects.get(id=planta_id)
        modelo = ModeloE.objects.get(id=modelo_id)

        # Generar código de barras si no existe
        if not codigo_barras:
            codigo_barras = "1234567890"  # Aquí podrías implementar una lógica para generar el código de barras
            img_barras = generar_codigo_barras(codigo_barras)
            # Puedes guardar el código de barras generado en el servidor si es necesario

        # Guardar la estación en la base de datos
        estacion = Estacion.objects.create(
            planta=planta,
            modelo=modelo,
            codigo_barras=codigo_barras
        )
        estacion.save()

        # Redirigir al dashboard u otra vista
        return redirect('dashboard')

    else:
        plantas = Planta.objects.all()
        modelos = ModeloE.objects.all()
        return render(request, 'plantas/crud-estaciones/agregar-estacion.html', {'plantas': plantas, 'modelos': modelos})

@login_required
def agregar_modelo_estacion_view(request):
    return render(request, 'plantas/crud-estaciones/agregar-modelo.html')


