# Generated by Django 5.0.7 on 2024-09-16 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto_hospital', '0016_alter_paciente_autorizacion_informacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='autorizacion_informacion',
            field=models.CharField(choices=[('Acepto', 'Acepto'), ('Rechazo', 'Rechazo')], max_length=7),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='consentimiento_procedimientos',
            field=models.CharField(choices=[('Acepto', 'Acepto'), ('Rechazo', 'Rechazo')], max_length=7),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='descargo_responsabilidad',
            field=models.CharField(choices=[('Acepto', 'Acepto'), ('Rechazo', 'Rechazo')], max_length=7),
        ),
    ]
