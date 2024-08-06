from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroUsuarioForm
from .models import UsuarioVai
from django.urls import reverse

# Create your views here.

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

    return render(request, 'usuarios/registro-usuario.html', {'form': form})

@login_required
def ultimo_usuario_view(request):
    # Obtiene el último usuario registrado
    ultimo_usuario = UsuarioVai.objects.order_by('-id').first()
    
    # Verifica si hay usuarios en la base de datos
    if not ultimo_usuario:
        return render(request, 'usuarios/ultimo-usuario.html', {'mensaje': 'No hay usuarios registrados.'})
    
    return render(request, 'usuarios/ultimo-usuario.html', {'usuario': ultimo_usuario})

