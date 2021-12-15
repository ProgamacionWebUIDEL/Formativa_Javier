# Generated by Django 3.2.8 on 2021-12-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historia_Clinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_historia', models.IntegerField(help_text='Número Único de la Historia CLinica')),
                ('fecha_creacion', models.DateTimeField(help_text='Fecha de Ingreso de la Mascota a la CLinica')),
                ('fecha_revision', models.DateTimeField(help_text='Fecha de Revision de la Mascota')),
                ('diagnostico', models.CharField(help_text='Diagnostico de la Mascota', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la Mascota', max_length=200)),
                ('edad', models.IntegerField(help_text='Edad en años de la Mascota')),
                ('raza', models.CharField(help_text='Raza de la Mascota', max_length=120)),
                ('tipo', models.CharField(help_text='Tipo de Mascota', max_length=120)),
                ('duenio', models.CharField(help_text='Nombre del dueño de la Mascota', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_medicamento', models.CharField(help_text='Nombre del Medicamento', max_length=200)),
                ('tipo_medicamento', models.CharField(help_text='Tipo de Medicamento', max_length=120)),
                ('precio_medicamento', models.FloatField(help_text='Precio de Venta del Medicamento', max_length=200)),
                ('fecha_caducidad', models.DateTimeField(help_text='Fecha de Caducidad del Medicamento')),
            ],
        ),
    ]
