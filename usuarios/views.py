from django.shortcuts import redirect, render, get_object_or_404
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroUsuarioForm, BuscarUsuarioForm
from .models import UsuarioVai
from django.urls import reverse
from .models import UsuarioVai, Cargo
import openpyxl
from django.http import HttpResponse



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    form.add_error(None, "Tu cuenta no está habilitada.")
            else:
                form.add_error(None, "La información ingresada no es correcta.")
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect ('home')

@login_required
def dashboard_view(request):
    return render(request, 'usuarios/dashboard.html', {'is_dashboard': True})

@login_required
def registro_usuario_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            # Extraer datos del formulario
            cleaned_data = form.cleaned_data
            rol = cleaned_data.get('rol')
            cargo = cleaned_data.get('cargo')

            # Generar el username
            last_user = UsuarioVai.objects.all().order_by('id').last()
            new_id = last_user.id + 1 if last_user else 1
            username = f"{rol.codigo}{new_id}{cargo.codigo}"

            # Crear el usuario y guardar
            user = UsuarioVai(
                first_name=cleaned_data.get('first_name'),
                last_name=cleaned_data.get('last_name'),
                email=cleaned_data.get('email'),
                telefono=cleaned_data.get('telefono'),
                rol=rol,
                cargo=cargo,
                username=username
            )
            user.set_password('vaiprocess2024')  # Establecer la contraseña por defecto
            user.save()

            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect(reverse('ultimo_usuario'))
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'usuarios/registro-usuario.html', {'form': form, 'isin_dashboard': True})

@login_required
def ultimo_usuario_view(request):
    # Obtiene el último usuario registrado
    ultimo_usuario = UsuarioVai.objects.order_by('-id').first()
    
    # Verifica si hay usuarios en la base de datos
    if not ultimo_usuario:
        return render(request, 'usuarios/ultimo-usuario.html', {'mensaje': 'No hay usuarios registrados.'})
    
    return render(request, 'usuarios/ultimo-usuario.html', {'usuario': ultimo_usuario, 'isin_dashboard': True})

@login_required
def modificar_usuario_view(request):
    usuario = None
    form_buscar = BuscarUsuarioForm()

    if request.method == 'POST' and 'buscar_usuario' in request.POST:
        # Buscar el usuario
        form_buscar = BuscarUsuarioForm(request.POST)
        if form_buscar.is_valid():
            username = form_buscar.cleaned_data['username']
            usuario = get_object_or_404(UsuarioVai, username=username)

    if request.method == 'POST' and 'modificar_usuario' in request.POST:
        # Modificar el usuario
        usuario = get_object_or_404(UsuarioVai, username=request.POST.get('username'))
        form_modificar = RegistroUsuarioForm(request.POST, instance=usuario)
        if form_modificar.is_valid():
            # Extraer rol y cargo del formulario
            cleaned_data = form_modificar.cleaned_data
            rol = cleaned_data.get('rol')
            cargo = cleaned_data.get('cargo')


            nuevo_username = f"{rol.codigo}{usuario.id}{cargo.codigo}"
            usuario.username = nuevo_username

            # Guardar el usuario con las modificaciones
            form_modificar.save()
            messages.success(request, 'Usuario modificado exitosamente.')
            return redirect('dashboard')
    else:
        if usuario:
            form_modificar = RegistroUsuarioForm(instance=usuario)
        else:
            form_modificar = None

    return render(request, 'usuarios/modificar-usuario.html', {
        'form_buscar': form_buscar,
        'form_modificar': form_modificar,
        'usuario': usuario,
        'isin_dashboard': True
    })

@login_required
def modificar_habilitacion_view(request):
    usuario = None
    form_buscar = BuscarUsuarioForm()
    
    if request.method == 'POST':
        if 'buscar_usuario' in request.POST:
            # Buscar el usuario
            form_buscar = BuscarUsuarioForm(request.POST)
            if form_buscar.is_valid():
                username = form_buscar.cleaned_data['username']
                usuario = get_object_or_404(UsuarioVai, username=username)
        
        if 'guardar_cambio' in request.POST:
            # Modificar la habilitación del usuario
            username = request.POST.get('username')
            usuario = get_object_or_404(UsuarioVai, username=username)
            is_active = request.POST.get('is_active') == '1'
            usuario.is_active = is_active
            usuario.save()
            messages.success(request, 'Estado del usuario modificado exitosamente.')
            return redirect('modificar_habilitacion')  # Redirige para actualizar el estado
        
    return render(request, 'usuarios/modificar-habilitacion.html', {
        'form_buscar': form_buscar,
        'usuario': usuario,
        'isin_dashboard': True
    })

@login_required
def cambiar_contrasena_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        current_password = request.POST.get('current_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        
        # Verificar que el nombre de usuario sea el correcto
        if username != request.user.username:
            messages.error(request, 'Nombre de usuario incorrecto.')
            return render(request, 'cambiar_contrasena.html')
        
        # Verificar que la contraseña actual sea correcta
        user = authenticate(username=request.user.username, password=current_password)
        if user is None:
            messages.error(request, 'La contraseña actual es incorrecta.')
            return render(request, 'cambiar_contrasena.html')
        
        # Verificar que las nuevas contraseñas coincidan
        if new_password1 != new_password2:
            messages.error(request, 'Las nuevas contraseñas no coinciden.')
            return render(request, 'cambiar_contrasena.html')
        
        # Guardar la nueva contraseña
        user.set_password(new_password1)
        user.save()
        update_session_auth_hash(request, user)  # Mantener la sesión activa del usuario
        
        # Logout después de cambiar la contraseña
        logout(request)
        messages.success(request, 'Contraseña cambiada con éxito. Por favor, inicie sesión nuevamente.')
        return redirect('login')  # Redirigir al inicio de sesión o a la página deseada
    
    else:
        return render(request, 'usuarios/cambiar-contrasena.html', {'isin_dashboard': True})

@login_required
def buscar_usuario_view(request):
    # Inicializamos una lista vacía para los resultados
    resultados = []
    cargos = Cargo.objects.all()  # Cargar los cargos
    #plantas = Planta.objects.all()  # Cargar las plantas
    #empresas = Empresa.objects.all()  # Cargar las empresas
    plantas = ["Gersa"]
    empresas = ["Gersa"]

    # Verificamos si se ha enviado el formulario de búsqueda
    if request.method == 'GET':
        criterio = request.GET.get('criterio')
        print(f'Criterio recibido: {criterio}')  # Verifica el criterio recibido

        if criterio == 'activos':
            resultados = UsuarioVai.objects.filter(is_active=True)
        elif criterio == 'inactivos':
            resultados = UsuarioVai.objects.filter(is_active=False)
        elif criterio == 'cargo':
            cargo = request.GET.get('cargo')
            if cargo:
                resultados = UsuarioVai.objects.filter(cargo_id=cargo)
        elif criterio == 'planta':
            planta = request.GET.get('planta')
            if planta:
                resultados = UsuarioVai.objects.filter(planta_id=planta)
        elif criterio == 'empresa':
            empresa = request.GET.get('empresa')
            if empresa:
                resultados = UsuarioVai.objects.filter(empresa_id=empresa)

    # Pasamos los resultados y los datos de los selects a la plantilla
    return render(request, 'usuarios/buscar-usuarios.html', {
        'isin_dashboard': True,
        'resultados': resultados,
        'cargos': cargos,
        'plantas': plantas,
        'empresas': empresas,
    })

@login_required
def exportar_usuarios_excel_view(request):
    criterio = request.GET.get('criterio')
    usuarios = []

    print(f'Criterio recibido: {criterio}')  # Depuración

    # Lógica de búsqueda de usuarios según el criterio
    if criterio == 'activos':
        usuarios = UsuarioVai.objects.filter(is_active=True)
    elif criterio == 'inactivos':
        usuarios = UsuarioVai.objects.filter(is_active=False)
    elif criterio == 'cargo':
        cargo = request.GET.get('cargo')
        print(f'Filtrando por cargo: {cargo}')  # Depuración
        if cargo:
            usuarios = UsuarioVai.objects.filter(cargo_id=cargo)
    # elif criterio == 'planta':
    #     planta = request.GET.get('planta')
    #     print(f'Filtrando por planta: {planta}')  # Depuración
    #     if planta:
    #         usuarios = UsuarioVai.objects.filter(planta_id=planta)
    # elif criterio == 'empresa':
    #     empresa = request.GET.get('empresa')
    #     print(f'Filtrando por empresa: {empresa}')  # Depuración
    #     if empresa:
    #         usuarios = UsuarioVai.objects.filter(empresa_id=empresa)

    print(f'Usuarios encontrados: {len(usuarios)}')  # Depuración

    # Crear un libro de Excel y una hoja
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Usuarios'

    # Agregar encabezados
    headers = ['Username', 'Nombres', 'Apellidos', 'Email', 'Teléfono', 'Cargo', 'Habilitado', 'Planta', 'Fecha Registro', 'Último Ingreso']
    sheet.append(headers)

    # Agregar datos de usuarios
    for usuario in usuarios:
        sheet.append([
            usuario.username,
            usuario.first_name,
            usuario.last_name,
            usuario.email,
            usuario.telefono,
            usuario.cargo.nombre if usuario.cargo else 'Sin cargo',
            'Sí' if usuario.is_active else 'No',
            #usuario.planta.nombre if usuario.planta else 'Sin planta',
            usuario.date_joined.strftime('%Y-%m-%d %H:%M:%S'),
            usuario.last_login.strftime('%Y-%m-%d %H:%M:%S') if usuario.last_login else 'Nunca'
        ])

    # Preparar la respuesta HTTP con el archivo Excel
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=usuarios.xlsx'
    workbook.save(response)
    return response



