from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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

def register_view(request):
    pass