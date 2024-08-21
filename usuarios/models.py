from django.db import models
from django.contrib.auth.models import AbstractUser
from plantas.models import Empresa, Planta, Estacion, Sensor, Actuador

class Rol(models.Model):
    nombre = models.CharField(max_length=25)
    codigo = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.nombre

class Cargo(models.Model):
    nombre = models.CharField(max_length=25, unique=True)
    codigo = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.nombre

class UsuarioVai(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='usuarios')  # Un usuario está vinculado con una sola empresa
    plantas = models.ManyToManyField(Planta, related_name='usuarios')  # Relación con plantas
    estaciones = models.ManyToManyField(Estacion, related_name='usuarios')  # Relación con estaciones
    sensores = models.ManyToManyField(Sensor, related_name='usuarios')  # Relación con sensores
    actuadores = models.ManyToManyField(Actuador, related_name='usuarios')  # Relación con actuadores


    def __str__(self):
        return self.username