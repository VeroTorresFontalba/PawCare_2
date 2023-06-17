# Generated by Django 3.2.8 on 2023-06-15 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0085_auto_20230615_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservacliente',
            name='cronograma',
        ),
        migrations.RemoveField(
            model_name='reservacliente',
            name='user',
        ),
        migrations.AddField(
            model_name='reservacliente',
            name='cliente',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='reservacliente',
            name='cuidador',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='reservacliente',
            name='estado',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='reservacliente',
            name='fechaReserva',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservacliente',
            name='idCliente',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='reservacliente',
            name='idCuidador',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='reservacliente',
            name='idReserva',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]