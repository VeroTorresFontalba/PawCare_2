# Generated by Django 4.2 on 2023-05-21 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0003_alter_categoria_id'),
        ('users', '0016_alter_user_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='categoria',
            field=models.ForeignKey(default='Cliente', null=True, on_delete=django.db.models.deletion.CASCADE, to='categoria.categoria'),
        ),
    ]
