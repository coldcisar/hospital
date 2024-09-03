
from django.shortcuts import render,redirect
from contacto_hospital.models import Pacientes,nuevoUsuario,Doctores
from django.contrib import messages 
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PacienteForm, ResponsableForm


def paginaIndex(request):
    return render(request, 'index.html')
def paginaAgregarD(request):
    return render(request,'agregarD.html')
def paginaAgregarP(request):
    return render(request, 'agregarP.html')


def agregarP(request):
    if request.method == 'POST':
        paciente_form = PacienteForm(request.POST)
        responsable_form = None

        if paciente_form.is_valid():
            paciente = paciente_form.save()

            es_paciente = request.POST.get('es-paciente')
            if es_paciente == 'no':
                responsable_form = ResponsableForm(request.POST)
                if responsable_form.is_valid():
                    responsable = responsable_form.save(commit=False)
                    responsable.paciente = paciente
                    responsable.save()
                    messages.success(request, 'Paciente y responsable registrados correctamente.')
                    return redirect('list_paciente')
                else:
                    # Mostrar errores del formulario de responsable.
                    for error in responsable_form.errors.values():
                        for message in error:
                            messages.error(request, message)
            else:
                messages.success(request, 'Paciente registrado correctamente.')
                return redirect('list_paciente')

        # Mostrar errores del formulario de paciente.
        for error in paciente_form.errors.values():
            for message in error:
                messages.error(request, message)

    else:
        paciente_form = PacienteForm()
        responsable_form = ResponsableForm()

    return render(request, 'agregarP.html', {
        'paciente_form': paciente_form,
        'responsable_form': responsable_form
    })

    
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





         
            
