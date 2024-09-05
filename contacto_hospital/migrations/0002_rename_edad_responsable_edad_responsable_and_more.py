# Generated by Django 5.0.7 on 2024-09-05 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacto_hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='responsable',
            old_name='edad',
            new_name='edad_responsable',
        ),
        migrations.RenameField(
            model_name='responsable',
            old_name='idioma_hablado',
            new_name='idioma_responsable',
        ),
        migrations.RenameField(
            model_name='responsable',
            old_name='metodo_contacto_email',
            new_name='metodo_contacto_email_responsable',
        ),
        migrations.RenameField(
            model_name='responsable',
            old_name='metodo_contacto_fono',
            new_name='metodo_contacto_fono_responsable',
        ),
        migrations.RenameField(
            model_name='responsable',
            old_name='nacionalidad',
            new_name='nacionalidad_responsable',
        ),
        migrations.RenameField(
            model_name='responsable',
            old_name='nombre_completo',
            new_name='nombre_completo_responsable',
        ),
        migrations.RenameField(
            model_name='responsable',
            old_name='nombre_social',
            new_name='nombre_social_responsable',
        ),
        migrations.RenameField(
            model_name='responsable',
            old_name='numero_documento_identidad',
            new_name='numero_documento_identidad_responsable',
        ),
        migrations.RenameField(
            model_name='responsable',
            old_name='pais_nacimiento',
            new_name='pais_nacimiento_responsable',
        ),
        migrations.RenameField(
            model_name='responsable',
            old_name='tipo_documento_identidad',
            new_name='tipo_documento_identidad_responsable',
        ),
    ]
