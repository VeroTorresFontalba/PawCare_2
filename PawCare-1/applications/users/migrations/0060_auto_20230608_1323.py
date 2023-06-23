# Generated by Django 3.2.8 on 2023-06-08 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0059_auto_20230607_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diareserva',
            name='fechaReserva',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Dia'),
        ),
        migrations.AlterField(
            model_name='estadoreserva',
            name='reservaEstado',
            field=models.CharField(max_length=15),
        ),
    ]
