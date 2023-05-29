# Generated by Django 4.2 on 2023-05-22 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tservicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, unique=True, verbose_name='Tipo de servicio')),
            ],
            options={
                'verbose_name': 'Tipo de servicio',
                'verbose_name_plural': 'Tipos de servicios',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripccion', models.TextField(blank=True, max_length=500, null=True)),
                ('servicios', models.ManyToManyField(blank=True, null=True, to='perfil.tservicio', verbose_name='Tipos de servicios')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
                'ordering': ['-id'],
            },
        ),
    ]