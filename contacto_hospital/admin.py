from django.contrib import admin
from .models import nuevoUsuario, Paciente,Doctores,Responsable

admin.site.register(nuevoUsuario)
admin.site.register(Paciente)
admin.site.register(Doctores)
admin.site.register(Responsable)

