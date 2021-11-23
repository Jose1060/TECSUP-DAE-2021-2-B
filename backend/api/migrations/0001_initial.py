# Generated by Django 3.2.9 on 2021-11-14 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('titulo', models.CharField(max_length=255)),
                ('ISBN', models.CharField(max_length=80)),
                ('editorial', models.CharField(max_length=255)),
                ('numPage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('numUsuario', models.IntegerField()),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('NIF', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecPrestamo', models.DateTimeField()),
                ('fecDevolucion', models.DateTimeField()),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.usuario')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.libro')),
            ],
        ),
    ]
