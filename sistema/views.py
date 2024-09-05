
from django.shortcuts import render,redirect
from contacto_hospital.models import Pacientes,nuevoUsuario,Doctores
from django.contrib import messages 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def paginaIndex(request):
    return render(request, 'index.html')
def paginaAgregarD(request):
    return render(request,'agregarD.html')
def paginaAgregarP(request):
    return render(request, 'agregarP.html')


@csrf_exempt
def agregarP(request):
    if request.method == 'POST':
        # Recibir los datos del formulario del paciente
        nombre_completo = request.POST.get('nombre_completo')
        nombre_social = request.POST.get('nombre_social', '')
        edad = request.POST.get('edad')
        pais_nacimiento = request.POST.get('pais_nacimiento')
        region_zona_nacimiento = request.POST.get('region_zona_nacimiento', '')
        region_zona_residencia_actual = request.POST.get('region_zona_residencia_actual', '')
        nacionalidad = request.POST.get('nacionalidad')
        idioma_hablado = request.POST.get('idioma_hablado')
        metodo_contacto_fono = request.POST.get('metodo_contacto_fono')
        metodo_contacto_email = request.POST.get('metodo_contacto_email')
        tipo_documento_identidad = request.POST.get('tipo_documento_identidad')
        numero_documento_identidad = request.POST.get('numero_documento_identidad')
        es_paciente = request.POST.get('es_paciente')
        relacion = request.POST.get('relacion')
        nombre_completo_responsable = request.POST.get('nombre_completo_responsable')
        nombre_social_responsable = request.POST.get('nombre_social_responsable', '')
        edad_responsable = request.POST.get('edad_responsable')
        pais_nacimiento_responsable = request.POST.get('pais_nacimiento_responsable')
        nacionalidad_responsable = request.POST.get('nacionalidad_responsable')
        idioma_responsable = request.POST.get('idioma_responsable')
        metodo_contacto_fono_responsable = request.POST.get('metodo_contacto_fono_responsable')
        metodo_contacto_email_responsable = request.POST.get('metodo_contacto_email_responsable')
        tipo_documento_identidad_responsable = request.POST.get('tipo_documento_identidad_responsable')
        numero_documento_identidad_responsable = request.POST.get('numero_documento_identidad_responsable')
        paciente = Pacientes(
            nombre_completo=nombre_completo,
            nombre_social=nombre_social,
            edad=edad,
            pais_nacimiento=pais_nacimiento,
            region_zona_nacimiento=region_zona_nacimiento,
            region_zona_residencia_actual=region_zona_residencia_actual,
            nacionalidad=nacionalidad,
            idioma_hablado=idioma_hablado,
            metodo_contacto_fono=metodo_contacto_fono,
            metodo_contacto_email=metodo_contacto_email,
            tipo_documento_identidad=tipo_documento_identidad,
            numero_documento_identidad=numero_documento_identidad,
            es_paciente=es_paciente,
            relacion=relacion,
            nombre_completo_responsable=nombre_completo_responsable,
            nombre_social_responsable=nombre_social_responsable,
            edad_responsable=edad_responsable,
            pais_nacimiento_responsable=pais_nacimiento_responsable,
            nacionalidad_responsable=nacionalidad_responsable,
            idioma_responsable=idioma_responsable,
            metodo_contacto_fono_responsable=metodo_contacto_fono_responsable,
            metodo_contacto_email_responsable=metodo_contacto_email_responsable,
            tipo_documento_identidad_responsable=tipo_documento_identidad_responsable,
            numero_documento_identidad_responsable=numero_documento_identidad_responsable,
        )
        paciente.save()
   
        return redirect('list_paciente')

    # Si no es un POST, renderizar la página del formulario
    return render(request, 'agregarP.html')

    
def agregarD(request):
    if request.method == 'POST':
        required_fields = ['nombreD', 'rutD', 'EspecialidadD', 'FonoD']
        if all(request.POST.get(field) for field in required_fields):
            rut = request.POST.get('rutD')
            if Doctores.objects.filter(rut_doctor=rut).exists():
                messages.error(request, 'Ya existe un doctor con este RUT.')
                return render(request, 'agregarD.html')

            try:
                doctor = Doctores(
                    nombre_doctor=request.POST.get('nombreD'),
                    rut_doctor=rut,
                    especialidad_doctor=request.POST.get('EspecialidadD'),
                    fono_doctor=request.POST.get('FonoD'),
                )
                doctor.save()
                return HttpResponseRedirect(reverse('list_doctor'))
            except Exception as e:
                messages.error(request, 'Error al agregar el doctor: {}'.format(str(e)))
                return render(request, 'agregarD.html')
        else:
            messages.error(request, 'Por favor, completa todos los campos obligatorios.')
            return render(request, 'agregarD.html')
    else:
        return render(request, "agregarD.html")

def paginaLogin(request):
    if request.method == 'POST':
        try:
            detalleUsuario=nuevoUsuario.objects.get(usuario=request.POST['usuario'],contraseña=request.POST['contraseña'])
            print("Usuario=",detalleUsuario)
            request.session['usuario']=detalleUsuario.usuario
            return render(request, 'index.html')
        except nuevoUsuario.DoesNotExist as e:
            messages.success(request,'Usuario no existe')
    return render(request, 'login.html')

def cerrar_sesion(request):
    template_name='inicio.html'
    return render(request, template_name)

def list_paciente(request):
    template_name='paciente.html'
    pacientes=Pacientes.objects.all()
    context={
        "pacientes": pacientes
    }
    return render(request, template_name,context)    
def list_doctor(request):
    template_name='doctor.html'
    doctores=Doctores.objects.all()
    context={
        "doctores": doctores
    }
    return render(request, template_name,context)    
def list_responsable(request):
    template_name='paciente.html'
    responsable=Responsable.objects.all()
    context={
        "responsable": responsable
    }
    return render(request, template_name,context)





         
            
