# Generated by Django 3.2.8 on 2023-06-07 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0055_alter_mascotaficha_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_de_mascota', models.CharField(blank=True, max_length=50, null=True)),
                ('chip', models.BooleanField(default=False, verbose_name='Chip')),
                ('n_chip', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='mascotas', verbose_name='Imagen del la Mascota')),
                ('descripccion', models.TextField(verbose_name='Descripccion del la mascota')),
                ('especies', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='especies', to='users.especies', verbose_name='Tipos de mascota')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Dueño', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'mascota',
                'verbose_name_plural': 'mascotas',
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='MascotaFicha',
        ),
    ]