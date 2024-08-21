
from django.shortcuts import render,redirect
from contacto_hospital.models import Pacientes,nuevoUsuario,Doctores
from django.contrib import messages 
from django.http import HttpResponseRedirect
from django.urls import reverse


def paginaIndex(request):
    return render(request, 'index.html')
def paginaAgregarD(request):
    return render(request,'agregarD.html')
def paginaAgregarP(request):
    return render(request, 'agregarP.html')

def agregarP(request):
    if request.method == 'POST':
        # Collect form data
        form_data = {
            'nombre_completo': request.POST.get('nombre_completo'),
            'edad': request.POST.get('edad'),
            'pais_nacimiento': request.POST.get('pais_nacimiento'),
            'nacionalidad': request.POST.get('nacionalidad'),
            'idioma_hablado': request.POST.get('idioma_hablado'),
            'metodo_contacto_fono': request.POST.get('metodo_contacto_fono'),
            'metodo_contacto_email': request.POST.get('metodo_contacto_email'),
            'tipo_documento_identidad': request.POST.get('tipo_documento_identidad'),
            'numero_documento_identidad': request.POST.get('numero_documento_identidad'),
        }

        # Validation messages
        required_fields = {
            'nombre_completo': 'Debe ingresar su nombre completo.',
            'edad': 'Debe ingresar su edad.',
            'pais_nacimiento': 'Debe ingresar su país de nacimiento.',
            'nacionalidad': 'Debe ingresar su nacionalidad.',
            'idioma_hablado': 'Debe ingresar el idioma que habla.',
            'metodo_contacto_fono': 'Debe ingresar un método de contacto (teléfono).',
            'metodo_contacto_email': 'Debe ingresar un email de contacto.',
            'tipo_documento_identidad': 'Debe ingresar el tipo de documento de identidad.',
            'numero_documento_identidad': 'Debe ingresar un número de documento de identidad.',
        }

        for field, error_message in required_fields.items():
            if not form_data.get(field):
                messages.error(request, error_message)


        if not messages.get_messages(request):
            # Save the patient data
            paciente = Pacientes(
                nombre_completo=form_data['nombre_completo'],
                nombre_social=request.POST.get('nombre_social'),
                edad=form_data['edad'],
                pais_nacimiento=form_data['pais_nacimiento'],
                region_zona_nacimiento=request.POST.get('region_zona_nacimiento'),
                region_zona_residencia_actual=request.POST.get('region_zona_residencia_actual'),
                nacionalidad=form_data['nacionalidad'],
                idioma_hablado=form_data['idioma_hablado'],
                metodo_contacto_fono=form_data['metodo_contacto_fono'],
                metodo_contacto_email=form_data['metodo_contacto_email'],
                tipo_documento_identidad=form_data['tipo_documento_identidad'],
                numero_documento_identidad=form_data['numero_documento_identidad'],
            )
            paciente.save()
            messages.success(request, 'Paciente registrado correctamente.')
            return redirect('list_paciente')

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





         
            
