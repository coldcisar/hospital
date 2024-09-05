# Generated by Django 5.0.7 on 2024-09-04 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto_hospital', '0007_alter_pacientes_nombre_completo_responsable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='edad_responsable',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='idioma_responsable',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='nacionalidad_responsable',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='numero_documento_identidad_responsable',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='pais_nacimiento_responsable',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='tipo_documento_identidad_responsable',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
