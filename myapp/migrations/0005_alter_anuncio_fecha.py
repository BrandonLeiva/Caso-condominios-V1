# Generated by Django 4.2 on 2023-05-25 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_areacomun_fecha_alter_pagocomun_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
