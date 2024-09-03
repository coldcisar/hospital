from django import forms
from contacto_hospital.models import Pacientes, Responsable

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['nombre_completo', 'nombre_social', 'edad', 'pais_nacimiento', 'region_zona_nacimiento', 'region_zona_residencia_actual', 'nacionalidad', 'idioma_hablado', 'metodo_contacto_fono', 'metodo_contacto_email', 'tipo_documento_identidad', 'numero_documento_identidad']

class ResponsableForm(forms.ModelForm):
    class Meta:
        model = Responsable
        fields = ['paciente','es_paciente', 'relacion', 'nombre_completo_responsable', 'nombre_social_responsable', 'edad_responsable', 'pais_nacimiento_responsable', 'nacionalidad_responsable', 'idioma_responsable', 'metodo_contacto_fono_responsable', 'metodo_contacto_email_responsable', 'tipo_documento_identidad_responsable', 'numero_documento_identidad_responsable']
