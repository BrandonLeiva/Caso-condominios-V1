# Generated by Django 4.2 on 2023-05-25 17:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_areacomun_estado_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areacomun',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='pagocomun',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
