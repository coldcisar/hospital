# Generated by Django 5.0.7 on 2024-09-05 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto_hospital', '0010_alter_pacientes_es_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='es_paciente',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
