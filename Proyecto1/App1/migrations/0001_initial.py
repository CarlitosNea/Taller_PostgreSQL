# Generated by Django 4.1.7 on 2023-04-29 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.TextField(max_length=10)),
                ('nombre', models.TextField(max_length=20)),
                ('apellido', models.TextField(max_length=20)),
                ('apodo', models.TextField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('contrasena', models.TextField(max_length=20)),
                ('genero', models.TextField(max_length=10)),
                ('ciudad', models.TextField(max_length=20)),
                ('telefono1', models.TextField(max_length=20)),
                ('telefono2', models.TextField(max_length=20)),
            ],
        ),
    ]
