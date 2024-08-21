# Generated by Django 5.0.7 on 2024-08-14 19:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ModeloE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoActuador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('usuarios', models.ManyToManyField(related_name='empresas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_barras', models.CharField(max_length=50, unique=True)),
                ('usuarios', models.ManyToManyField(related_name='estaciones', to=settings.AUTH_USER_MODEL)),
                ('modelo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='estaciones', to='plantas.modeloe')),
            ],
        ),
        migrations.CreateModel(
            name='Actuador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_instalacion', models.DateField()),
                ('codigo_barras', models.CharField(max_length=50, unique=True)),
                ('usuarios', models.ManyToManyField(related_name='actuadores', to=settings.AUTH_USER_MODEL)),
                ('estacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actuadores', to='plantas.estacion')),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actuadores', to='plantas.tipoactuador')),
            ],
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plantas', to='plantas.empresa')),
                ('usuarios', models.ManyToManyField(related_name='plantas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='estacion',
            name='planta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estaciones', to='plantas.planta'),
        ),
        migrations.CreateModel(
            name='DatosActuador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('actuador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datos', to='plantas.actuador')),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datos_actuadores', to='plantas.planta')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_instalacion', models.DateField()),
                ('codigo_barras', models.CharField(max_length=50, unique=True)),
                ('estacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensores', to='plantas.estacion')),
                ('usuarios', models.ManyToManyField(related_name='sensores', to=settings.AUTH_USER_MODEL)),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sensores', to='plantas.tiposensor')),
            ],
        ),
        migrations.CreateModel(
            name='DatosSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datos_sensores', to='plantas.planta')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datos', to='plantas.sensor')),
            ],
        ),
    ]
