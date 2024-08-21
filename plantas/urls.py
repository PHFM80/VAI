from django.urls import path
from . import views

urlpatterns = [
    path('agregar_empresa/', views.agregar_empresa_view, name='agregar_empresa'),  
    path('agregar_planta/', views.agregar_planta_view, name='agregar_planta'),
    path('eliminar_planta/', views.eliminar_planta_view, name='eliminar_planta'),
    path('agregar_estacion/', views.agregar_estacion_view, name='agregar_estacion'),
    path('agregar_modelo_estacion/', views.agregar_modelo_estacion_view, name='agregar_modelo_estacion'),
    path('agregar_sensor/', views.agregar_sensor_view, name='agregar_sensor'),
    path('agregar_tipo_sensor/', views.agregar_tipo_sensor_view, name='agregar_tipo_sensor'),
    path('generate-qr/', views.generate_qr_view, name='generate_qr'), 

]


