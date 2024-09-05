from django.db import models
from django.core.exceptions import ValidationError

class nuevoUsuario(models.Model):
    usuario = models.CharField(blank=True, max_length=150, verbose_name="Usuario")
    contraseña = models.CharField(blank=True, max_length=150, verbose_name="Contraseña")

    def __str__(self):
        return self.usuario

    class Meta:
        ordering = ['usuario']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Doctores(models.Model):
    rut_doctor = models.CharField(max_length=12, unique=True, verbose_name="RUT del Doctor")
    nombre_doctor = models.CharField(max_length=100, verbose_name="Nombre del Doctor")
    especialidad_doctor = models.CharField(max_length=100, verbose_name="Especialidad")
    fono_doctor = models.CharField(max_length=15, verbose_name="Teléfono")

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"
        db_table = 'doctores'

    def __str__(self):
        return self.nombre_doctor


class Responsable(models.Model):
    es_paciente = models.BooleanField(default=False, verbose_name="¿Es el paciente?")
    relacion = models.CharField(max_length=50, blank=True, null=True, verbose_name="Relación con Responsable")
    nombre_completo_responsable = models.CharField(max_length=35, blank=True, verbose_name="Nombre Completo")
    nombre_social_responsable = models.CharField(max_length=35, blank=True, verbose_name="Nombre Social")
    edad_responsable = models.PositiveIntegerField(blank=True, null=True, verbose_name="Edad")
    pais_nacimiento_responsable = models.CharField(max_length=50, blank=True, verbose_name="País de Nacimiento")
    nacionalidad_responsable = models.CharField(max_length=50, blank=True, verbose_name="Nacionalidad")
    idioma_responsable = models.CharField(max_length=50, blank=True, verbose_name="Idioma")
    metodo_contacto_fono_responsable = models.CharField(max_length=15, blank=True, verbose_name="Teléfono")
    metodo_contacto_email_responsable = models.EmailField(blank=True, verbose_name="Email")
    tipo_documento_identidad_responsable = models.CharField(max_length=50, blank=True, verbose_name="Tipo de Documento")
    numero_documento_identidad_responsable = models.CharField(max_length=25, blank=True, verbose_name="Número de Documento")

    class Meta:
        verbose_name = "Responsable"
        verbose_name_plural = "Responsables"
        db_table = 'responsable'

    def __str__(self):
        return self.nombre_completo_responsable if self.nombre_completo_responsable else "Responsable sin nombre"


class Paciente(models.Model):
    nombre_completo = models.CharField(max_length=35, blank=True, verbose_name="Nombre Completo")
    nombre_social = models.CharField(max_length=35, blank=True, verbose_name="Nombre Social")
    edad = models.PositiveIntegerField(blank=True, null=True, verbose_name="Edad")
    pais_nacimiento = models.CharField(max_length=50, blank=True, verbose_name="País de Nacimiento")
    region_zona_nacimiento = models.CharField(max_length=100, blank=True, verbose_name="Región/Zona de Nacimiento")
    region_zona_residencia_actual = models.CharField(max_length=100, blank=True, verbose_name="Región/Zona de Residencia Actual")
    nacionalidad = models.CharField(max_length=50, blank=True, verbose_name="Nacionalidad")
    idioma_hablado = models.CharField(max_length=50, blank=True, verbose_name="Idioma")
    metodo_contacto_fono = models.CharField(max_length=15, blank=True, verbose_name="Teléfono")
    metodo_contacto_email = models.EmailField(blank=True, verbose_name="Email")
    tipo_documento_identidad = models.CharField(max_length=50, blank=True, verbose_name="Tipo de Documento")
    numero_documento_identidad = models.CharField(max_length=25, blank=True, verbose_name="Número de Documento")
    responsable = models.ForeignKey(Responsable, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Responsable")

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        db_table = 'paciente'

    def __str__(self):
        return self.nombre_completo if self.nombre_completo else "Paciente sin nombre"
