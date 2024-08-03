from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('dashboard/', views.user_dashboard, name= 'dashboard'), 
    # path('logout/', auth_views.LogoutView.as_view(), name= 'logout'),
    # path('register/', views.user_register, name='register'),

]