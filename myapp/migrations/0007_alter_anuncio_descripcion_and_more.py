# Generated by Django 4.2 on 2023-05-28 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_multa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='areacomun',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='multa',
            name='Motivo',
            field=models.TextField(),
        ),
    ]
