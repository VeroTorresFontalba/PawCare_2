# Generated by Django 4.2 on 2023-05-23 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_alter_profile_servicios'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Tservicio',
        ),
    ]
