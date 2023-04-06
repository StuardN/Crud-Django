# Generated by Django 4.2 on 2023-04-06 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=200, null=True)),
                ('marca', models.CharField(max_length=200, null=True)),
                ('placa', models.CharField(max_length=200, null=True, unique=True)),
                ('año_fabricado', models.DateField(null=True)),
                ('motor', models.CharField(max_length=200, null=True, unique=True)),
                ('año_modelo', models.DateField(null=True)),
                ('chasis', models.CharField(max_length=200, null=True)),
                ('kilometraje', models.CharField(max_length=10, null=True)),
                ('capacidad_pasajero', models.CharField(max_length=2, null=True)),
                ('ruedas', models.CharField(max_length=2, null=True)),
                ('ejes', models.CharField(max_length=2, null=True)),
                ('Propietario', models.CharField(max_length=100, null=True)),
                ('cedula', models.CharField(max_length=10, null=True, unique=True)),
                ('telefono', models.CharField(max_length=10, null=True)),
                ('direccion', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Buses',
                'verbose_name_plural': 'Buses',
                'ordering': ['id'],
            },
        ),
    ]
