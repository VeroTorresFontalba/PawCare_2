# Generated by Django 3.2.8 on 2023-06-12 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0062_merge_20230611_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diareserva',
            name='estado',
        ),
        migrations.DeleteModel(
            name='Hora',
        ),
        migrations.DeleteModel(
            name='DiaReserva',
        ),
        migrations.DeleteModel(
            name='EstadoReserva',
        ),
    ]
