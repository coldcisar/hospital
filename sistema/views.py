
from django.shortcuts import render,redirect
from contacto_hospital.models import Paciente,nuevoUsuario,Doctores,Responsable
from django.contrib import messages 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


def paginaIndex(request):
    return render(request, 'index.html')
def paginaAgregarD(request):
    return render(request,'agregarD.html')
def paginaAgregarP(request):
    return render(request, 'agregarP.html')

@csrf_exempt
def agregarP(request):
    if request.method == 'POST':
        # Datos del paciente
        email=request.POST.get('email')
        nombre_completo = request.POST.get('nombre_completo')
        print(f"Nombre completo: {nombre_completo}")
        nombre_social = request.POST.get('nombre_social', '')
        edad = int(request.POST.get('edad')) if request.POST.get('edad') else None
        pais_nacimiento = request.POST.get('pais_nacimiento')
        region_zona_nacimiento = request.POST.get('region_zona_nacimiento', '')
        region_zona_residencia_actual = request.POST.get('region_zona_residencia_actual', '')
        nacionalidad = request.POST.get('nacionalidad')
        idioma_hablado = request.POST.get('idioma_hablado')
        metodo_contacto_fono = request.POST.get('metodo_contacto_fono')
        metodo_contacto_email = request.POST.get('metodo_contacto_email')
        tipo_documento_identidad = request.POST.get('tipo_documento_identidad')
        numero_documento_identidad = request.POST.get('numero_documento_identidad')
        enfermedades_cronicas = request.POST.getlist('enfermedades_cronicas', [])
        otras_enfermedades_cronicas = request.POST.get('otras_enfermedades_cronicas', '')
        enfermedades_comunes = request.POST.getlist('enfermedades_comunes', [])
        otras_enfermedades_comunes = request.POST.get('otras_enfermedades_comunes', '')
        cirugias_comunes = request.POST.getlist('cirugias_comunes', [])
        otras_cirugias_comunes = request.POST.get('otras_cirugias_comunes', '')
        cirugias_traumatologicas = request.POST.getlist('cirugias_traumatologicas',[])
        otras_cirugias_traumatologicas = request.POST.get('otras_cirugias_traumatologicas','')
        farmacos_patologias_cronicas = request.POST.getlist('farmacos_patologias_cronicas',[])
        otros_farmacos_patologias_cronicas = request.POST.get('otros_farmacos_patologias_cronicas','')
        detalle_farmacos_cronicos=request.POST.get('detalle_farmacos_cronicos')
        farmacos_no_cronicos = request.POST.getlist('farmacos_no_cronicos',[])
        otros_farmacos_no_cronicos = request.POST.get('otros_farmacos_no_cronicos','')
        detalle_farmacos_no_cronicos=request.POST.get('detalle_farmacos_no_cronicos')
        alergias_farmacos = request.POST.getlist('alergias_farmacos',[])
        otras_alergias_farmacos = request.POST.get('otras_alergias_farmacos','')
        detalle_alergias_farmacos=request.POST.get('detalle_alergias_farmacos')
        alergias_comunes = request.POST.getlist('alergias_comunes',[])
        otras_alergias_comunes = request.POST.get('otras_alergias_comunes','')
        detalle_alergias_no_farmacos=request.POST.get('detalle_alergias_no_farmacos')
        otros_antecedentes=request.POST.get('otros_antecedentes')
        centro_salud_previo = request.POST.get('centro_salud_previo',[])
        otro_centro_salud = request.POST.get('otro_centro_salud', '')
        resolucion_problema_salud = request.POST.get('resolucion_problema_salud',[])
        otro_resolucion_salud = request.POST.get('otro_resolucion_salud', '')
        motivo_consulta = request.POST.getlist('motivo_consulta',[])
        otros_motivos = request.POST.get('otros_motivos')
        tiempo_sintomas = request.POST.get('tiempo_sintomas',[])
        experimentado_problema_anteriormente = request.POST.get('experimentado_problema_anteriormente',[])
        frecuencia_problema = request.POST.get('frecuencia_problema',[])
        frecuencia_otros = request.POST.get('frecuencia_otros', '')
        motivo_consulta_texto=request.POST.get('motivo_consulta_texto'),
        descargo_responsabilidad=request.POST.get('descargo_responsabilidad',[])
        consentimiento_procedimientos=request.POST.get('consentimiento_procedimientos',[])
        autorizacion_informacion=request.POST.get('autorizacion_informacion',[])
        expectativas=request.POST.get('expectativas')
        preguntas=request.POST.get('preguntas')
        entendimiento_enfermedad=request.POST.get('entendimiento_enfermedad',[])

        
        
        enfermedades_cronicas_str = ', '.join(enfermedades_cronicas)
        enfermedades_comunes_str = ', '.join(enfermedades_comunes)
        cirugias_comunes_str = ', '.join(cirugias_comunes)
        cirugias_traumatologicas_str = ', '.join(cirugias_traumatologicas)
        farmacos_patologias_cronicas_str=', '.join(farmacos_patologias_cronicas)
        farmacos_no_cronicos_str=', '.join(farmacos_no_cronicos)
        alergias_farmacos_str=', '.join(alergias_farmacos)
        alergias_comunes_str=', '.join(alergias_comunes)
        motivo_consulta_str = ', '.join(motivo_consulta)



        # Datos del responsable
        es_paciente = request.POST.get('es_paciente') == 'on'
        relacion = request.POST.get('relacion')
        nombre_completo_responsable = request.POST.get('nombre_completo_responsable')
        nombre_social_responsable = request.POST.get('nombre_social_responsable', '')
        edad_responsable = int(request.POST.get('edad_responsable')) if request.POST.get('edad_responsable') else None
        pais_nacimiento_responsable = request.POST.get('pais_nacimiento_responsable')
        nacionalidad_responsable = request.POST.get('nacionalidad_responsable')
        idioma_responsable = request.POST.get('idioma_responsable')
        metodo_contacto_fono_responsable = request.POST.get('metodo_contacto_fono_responsable')
        metodo_contacto_email_responsable = request.POST.get('metodo_contacto_email_responsable')
        tipo_documento_identidad_responsable = request.POST.get('tipo_documento_identidad_responsable')
        numero_documento_identidad_responsable = request.POST.get('numero_documento_identidad_responsable')

        # Crear o recuperar responsable
        responsable = Responsable.objects.create(
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
        responsable.save()

        # Crear paciente y asociar responsable
        try:
            paciente = Paciente.objects.create(
                email=email,
                fecha_envio=timezone.now().date(),
                hora_envio=timezone.now().time(),
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
                responsable=responsable,
                enfermedades_cronicas=enfermedades_cronicas_str,
                otras_enfermedades_cronicas=otras_enfermedades_cronicas,
                enfermedades_comunes=enfermedades_comunes_str,
                otras_enfermedades_comunes=otras_enfermedades_comunes,
                cirugias_comunes=cirugias_comunes_str,
                otras_cirugias_comunes=otras_cirugias_comunes,
                cirugias_traumatologicas=cirugias_traumatologicas_str,
                otras_cirugias_traumatologicas=otras_cirugias_traumatologicas,
                farmacos_patologias_cronicas=farmacos_patologias_cronicas_str,
                otros_farmacos_patologias_cronicas=otros_farmacos_patologias_cronicas,
                detalle_farmacos_cronicos=detalle_farmacos_cronicos,
                farmacos_no_cronicos=farmacos_no_cronicos_str,
                otros_farmacos_no_cronicos=otros_farmacos_no_cronicos,
                detalle_farmacos_no_cronicos=detalle_farmacos_no_cronicos,
                alergias_farmacos=alergias_farmacos_str,
                otras_alergias_farmacos=otras_alergias_farmacos,
                detalle_alergias_farmacos=detalle_alergias_farmacos,
                alergias_comunes=alergias_comunes_str,
                otras_alergias_comunes=otras_alergias_comunes,
                detalle_alergias_no_farmacos=detalle_alergias_no_farmacos,
                otros_antecedentes=otros_antecedentes,
                motivo_consulta_texto=motivo_consulta_texto,
                centro_salud_previo=centro_salud_previo,
                otro_centro_salud=otro_centro_salud,
                resolucion_problema_salud=resolucion_problema_salud,
                otro_resolucion_salud=otro_resolucion_salud,
                motivo_consulta=motivo_consulta_str,
                otros_motivos=otros_motivos,
                tiempo_sintomas=tiempo_sintomas,
                experimentado_problema_anteriormente=experimentado_problema_anteriormente,
                frecuencia_problema=frecuencia_problema,
                frecuencia_otros=frecuencia_otros,
                descargo_responsabilidad=descargo_responsabilidad,
                consentimiento_procedimientos=consentimiento_procedimientos,
                autorizacion_informacion=autorizacion_informacion,
                expectativas=expectativas,
                preguntas=preguntas,
                entendimiento_enfermedad=entendimiento_enfermedad,



            )
            paciente.save()
        except Exception as e:
            print(f"Error al crear el paciente: {e}")
            return render(request, 'agregarP.html', {'error': 'Error al crear el paciente'})

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
    pacientes=Paciente.objects.all()
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





         
            
