# Generated by Django 4.2 on 2023-06-28 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_alter_multa_estado_pago'),
    ]

    operations = [
        migrations.RenameField(
            model_name='multa',
            old_name='estado_pago',
            new_name='estado',
        ),
    ]
