# Generated by Django 4.2 on 2023-05-24 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_alter_tservicio_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tservicio',
            new_name='Servicio',
        ),
    ]