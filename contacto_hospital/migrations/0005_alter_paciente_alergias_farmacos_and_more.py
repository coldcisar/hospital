# Generated by Django 5.0.7 on 2024-09-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto_hospital', '0004_paciente_alergias_farmacos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='alergias_farmacos',
            field=models.ManyToManyField(blank=True, to='contacto_hospital.paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='alergias_no_farmacos',
            field=models.ManyToManyField(blank=True, to='contacto_hospital.paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cirugias_comunes',
            field=models.ManyToManyField(blank=True, to='contacto_hospital.paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cirugias_traumatologicas',
            field=models.ManyToManyField(blank=True, to='contacto_hospital.paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='enfermedades_comunes',
            field=models.ManyToManyField(blank=True, to='contacto_hospital.paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='enfermedades_cronicas',
            field=models.ManyToManyField(blank=True, to='contacto_hospital.paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='farmacos_cronicos',
            field=models.ManyToManyField(blank=True, to='contacto_hospital.paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='farmacos_no_cronicos',
            field=models.ManyToManyField(blank=True, to='contacto_hospital.paciente'),
        ),
    ]
