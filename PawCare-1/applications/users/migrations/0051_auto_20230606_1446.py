# Generated by Django 3.2.8 on 2023-06-06 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0050_rename_dueno_mascotaficha_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascotaficha',
            name='especies',
        ),
        migrations.AddField(
            model_name='mascotaficha',
            name='especies',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='especies', to='users.especies', verbose_name='Tipos de mascota'),
        ),
        migrations.AlterField(
            model_name='mascotaficha',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]