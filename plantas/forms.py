from django import forms
from .models import Empresa, Planta, TipoSensor, Sensor, Estacion, ModeloE
from .utils import generar_codigo_qr

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre']  

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = ['nombre', 'empresa']

    empresa = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Empresa'
    )

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Nombre de la Planta'
    )

class TipoSensorForm(forms.ModelForm):
    class Meta:
        model = TipoSensor
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Tipo de Sensor'}),
        }

class SensorForm(forms.ModelForm):
    en_uso = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Sensor
        fields = ['fecha_instalacion', 'estacion', 'tipo', 'en_uso', 'descripcion', 'codigo_qr']
        widgets = {
            'fecha_instalacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estacion': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'en_uso': forms.CheckboxInput(attrs={'class': 'form-check-input', 'value': False}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'codigo_qr': forms.Textarea(attrs={'class': 'form-control', 'readonly': 'readonly', 'rows': 4, 'type': 'hidden'})
        }

    def __init__(self, *args, **kwargs):
        super(SensorForm, self).__init__(*args, **kwargs)
        # Añadir una opción vacía para estaciones y tipos
        self.fields['estacion'].choices = [('', '---------')] + [
            (estacion.id, estacion.nombre) for estacion in Estacion.objects.all()
        ]
        self.fields['tipo'].choices = [('', '---------')] + [
            (tipo.id, tipo.nombre) for tipo in TipoSensor.objects.all()
        ]

    def save(self, commit=True):
        sensor = super(SensorForm, self).save(commit=False)
        # Generar el QR utilizando los datos del sensor
        data_qr = f'ID: {sensor.id}, Tipo: {sensor.tipo.nombre}, Descripción: {sensor.descripcion}'
        sensor.codigo_qr = generar_codigo_qr(data_qr)
        if commit:
            sensor.save()
        return sensor












class EstacionForm(forms.ModelForm):
    class Meta:
        model = Estacion
        fields = ['planta', 'modelo', 'codigo_qr']  # Solo campos necesarios