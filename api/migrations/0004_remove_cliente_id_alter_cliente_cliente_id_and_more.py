# Generated by Django 5.1.3 on 2024-11-21 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_activo_cliente_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='id',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nivel_de_satisfaccion',
            field=models.FloatField(choices=[(1, 'Muy insatisfecho'), (2, 'Insatisfecho'), (3, 'Neutro'), (4, 'Satisfecho'), (5, 'Muy satisfecho')]),
        ),
    ]
