# Generated by Django 3.2.8 on 2023-06-06 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0051_auto_20230606_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascotaficha',
            name='user',
        ),
    ]
