from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Planta(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='plantas')

    def __str__(self):
        return self.nombre

class Estacion(models.Model):
    nombre = models.CharField(max_length=100)
    codigo_qr = models.TextField(unique=True, null=True, blank=True)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE, related_name='estaciones', null=True, blank=True)
    modelo = models.ForeignKey('ModeloE', on_delete=models.SET_NULL, null=True, blank=True, related_name='estaciones')

    def __str__(self):
        return self.codigo_barras

class ModeloE(models.Model):
    modelo = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True)  #agregar al modelo posiblemente.

    def __str__(self):
        return self.modelo

class TipoSensor(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Sensor(models.Model):
    fecha_instalacion = models.DateField(null=True, blank=True)
    codigo_qr = models.TextField(unique=True, null=True, blank=True)
    en_uso = models.BooleanField(default=False)
    descripcion = models.CharField(max_length=250, null=True, blank=True)  #agregar al modelo posiblemente.
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='sensores', null=True, blank=True)
    tipo = models.ForeignKey(TipoSensor, on_delete=models.SET_NULL, null=True, blank=True, related_name='sensores')


    def __str__(self):
        return self.codigo_barras
    @property
    def planta(self):
        return self.estacion.planta

class DatosSensor(models.Model):
    valor = models.FloatField()
    fecha = models.DateField()
    hora = models.TimeField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='datos')
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE, related_name='datos_sensores', null=True, blank=True)
    

    def __str__(self):
        return f'{self.sensor.codigo_barras} - {self.fecha} {self.hora}'

class TipoActuador(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Actuador(models.Model):
    fecha_instalacion = models.DateField()
    codigo_qr = models.TextField(unique=True, null=True, blank=True)
    en_uso = models.BooleanField(default=False)
    descripcion = models.CharField(max_length=250, null=True, blank=True)  #agregar al modelo posiblemente.
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='actuadores', null=True, blank=True)
    tipo = models.ForeignKey(TipoSensor, on_delete=models.SET_NULL, null=True, blank=True, related_name='actuadores')

    def __str__(self):
        return self.codigo_barras
    @property
    def planta(self):
        return self.estacion.planta

class DatosActuador(models.Model):
    valor = models.FloatField()
    fecha = models.DateField()
    hora = models.TimeField()
    actuador = models.ForeignKey(Actuador, on_delete=models.CASCADE, related_name='datos')
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE, related_name='datos_actuadores', null=True, blank=True)
    
    def __str__(self):
        return f'{self.actuador.codigo_barras} - {self.fecha} {self.hora}'


