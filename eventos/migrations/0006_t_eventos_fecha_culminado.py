# Generated by Django 4.2.5 on 2023-11-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_alter_t_eventos_fecha_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_eventos',
            name='fecha_culminado',
            field=models.DateTimeField(null=True),
        ),
    ]
