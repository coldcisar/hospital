from django.db import models
from django.core.exceptions import ValidationError


class nuevoUsuario(models.Model):
    usuario=models.CharField(blank=True ,max_length=150,verbose_name="Usuario")
    contraseña=models.CharField(blank=True, max_length=150,verbose_name="Contraseña")

    def __str__(self):
        return self.usuario
    class Meta:
        ordering =['usuario'] 
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Doctores(models.Model):
    rut_doctor = models.CharField(max_length=12, unique=True)
    nombre_doctor = models.CharField(max_length=100)
    especialidad_doctor = models.CharField(max_length=100)
    fono_doctor = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural ="Doctores"
        db_table ='doctores'

    def __str__(self):
        return self.nombre_doctor
    



class Pacientes(models.Model):
    nombre_completo = models.CharField(max_length=35,blank=True, null=True)
    nombre_social = models.CharField(max_length=35, blank=True, null=True)
    edad = models.PositiveIntegerField(blank=True, null=True)
    pais_nacimiento = models.CharField(max_length=50,blank=True, null=True)
    region_zona_nacimiento = models.CharField(max_length=100, blank=True, null=True)
    region_zona_residencia_actual = models.CharField(max_length=100, blank=True, null=True)
    nacionalidad = models.CharField(max_length=50,blank=True, null=True)
    idioma_hablado = models.CharField(max_length=50,blank=True, null=True)
    metodo_contacto_fono = models.CharField(max_length=15, blank=True, null=True)
    metodo_contacto_email = models.EmailField(blank=True, null=True)
    tipo_documento_identidad = models.CharField(max_length=50,blank=True, null=True)
    numero_documento_identidad = models.CharField(max_length=25,blank=True, null=True)
    es_paciente = models.BooleanField(default=False,null=True)
    relacion = models.CharField(max_length=50, blank=True, null=True)
    nombre_completo_responsable = models.CharField(max_length=35, blank=True, null=True)
    nombre_social_responsable = models.CharField(max_length=35, blank=True, null=True)
    edad_responsable = models.PositiveIntegerField(blank=True, null=True)
    pais_nacimiento_responsable = models.CharField(max_length=50, blank=True, null=True)
    nacionalidad_responsable = models.CharField(max_length=50, blank=True, null=True)
    idioma_responsable = models.CharField(max_length=50, blank=True, null=True)
    metodo_contacto_fono_responsable = models.CharField(max_length=15, blank=True, null=True)
    metodo_contacto_email_responsable = models.EmailField(blank=True, null=True)
    tipo_documento_identidad_responsable = models.CharField(max_length=50, blank=True, null=True)
    numero_documento_identidad_responsable = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        db_table = 'pacientes'

    def __str__(self):
        return self.numero_documento_identidad

    
    


    
    










