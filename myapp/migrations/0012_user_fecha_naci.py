# Generated by Django 4.2 on 2023-05-31 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_multa_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fecha_naci',
            field=models.DateField(null=True),
        ),
    ]
