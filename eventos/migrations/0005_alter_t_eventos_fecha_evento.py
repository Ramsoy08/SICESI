# Generated by Django 4.2.5 on 2023-11-07 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_remove_t_eventos_completado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_eventos',
            name='fecha_evento',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]