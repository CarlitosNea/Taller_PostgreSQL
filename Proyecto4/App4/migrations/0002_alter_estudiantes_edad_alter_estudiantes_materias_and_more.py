# Generated by Django 4.1.7 on 2023-05-01 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App4', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantes',
            name='edad',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='materias',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='promedio',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
