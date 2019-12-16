# Generated by Django 2.2.6 on 2019-11-21 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('zona', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=30)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('horario', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido1', models.CharField(max_length=30)),
                ('apellido2', models.CharField(max_length=30)),
                ('contrasena', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ruta', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('horario', models.TextField()),
                ('duracion', models.IntegerField()),
                ('rampa', models.BooleanField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Punto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField()),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('esParada', models.BooleanField()),
                ('descripcion', models.CharField(max_length=100)),
                ('ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Ruta')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accion', models.CharField(max_length=30)),
                ('tabla', models.CharField(max_length=30)),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('nombre_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Usuario')),
            ],
        ),
    ]
