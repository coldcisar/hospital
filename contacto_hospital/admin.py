from django.contrib import admin
from .models import nuevoUsuario, Pacientes,Doctores

admin.site.register(nuevoUsuario)
admin.site.register(Pacientes)
admin.site.register(Doctores)
