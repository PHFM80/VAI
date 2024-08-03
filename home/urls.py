from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('servicios/', views.servicios_view, name='servicios'),
    path('catalogos/', views.catalogos_view, name='catalogos'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('acercanuestro/', views.acerca_view, name='acerca'),
]


