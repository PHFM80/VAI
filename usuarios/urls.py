from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.login_view, name='login'),  # Usa tu propia vista de login
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro-usuario/', views.registro_usuario_view, name='registro-usuario'),
    path('ultimo-usuario/', views.ultimo_usuario_view, name='ultimo_usuario'),
    path('modificar-usuario/', views.modificar_usuario_view, name='modificar_usuario'),
    path('modificar-habilitacion/', views.modificar_habilitacion_view, name='modificar_habilitacion'),
    path('cambiar-contrasena/', views.cambiar_contrasena_view, name='cambiar_contrasena'),
    path('buscar-usuario/', views.buscar_usuario_view, name='buscar_usuario'),

]
