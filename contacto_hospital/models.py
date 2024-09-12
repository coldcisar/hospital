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

    NINGUNA = 'Ninguna'
    INFARTO_CORAZON = 'Infarto al corazón'
    INFARTO_CEREBRAL = 'Infarto cerebral'
    HIPERTENSION = 'Hipertensión arterial'
    CARDIOPATIA_CORONARIA = 'Cardiopatía coronaria'
    INSUFICIENCIA_CARDIACA = 'Insuficiencia cardiaca'
    VALVULOPATIAS = 'Valvulopatías cardiacas'
    ANEURISMAS = 'Aneurismas'
    DIABETES = 'Diabetes'
    OBESIDAD = 'Obesidad'
    SINDROME_METABOLICO = 'Síndrome metabólico'
    EPOC = 'EPOC'
    TABAQUISMO = 'Tabaquismo'
    ALCOHOLISMO = 'Alcoholismo'
    ENFERMEDAD_RENAL = 'Enfermedad renal crónica'
    HEMODIALISIS = 'Hemodiálisis'
    ASTMA = 'Asma'
    SIDA_VIH = 'Sida / VIH'
    ARTRITIS_ARTROSIS = 'Artritis / artrosis'
    HERNIA_NUCLEO_PULPOSO = 'Hernia del núcleo pulposo'
    ULCERA_GASTRICA = 'Úlcera gástrica'
    HIPOTIROIDISMO = 'Hipotiroidismo'
    HIPERTIROIDISMO = 'Hipertiroidismo'
    OTRO = 'Otro'

    ENFERMEDADES_CRONICAS_CHOICES = [
        (NINGUNA, 'Ninguna'),
        (INFARTO_CORAZON, 'Infarto al corazón'),
        (INFARTO_CEREBRAL, 'Infarto cerebral'),
        (HIPERTENSION, 'Hipertensión arterial'),
        (CARDIOPATIA_CORONARIA, 'Cardiopatía coronaria'),
        (INSUFICIENCIA_CARDIACA, 'Insuficiencia cardiaca'),
        (VALVULOPATIAS, 'Valvulopatías cardiacas'),
        (ANEURISMAS, 'Aneurismas'),
        (DIABETES, 'Diabetes'),
        (OBESIDAD, 'Obesidad'),
        (SINDROME_METABOLICO, 'Síndrome metabólico'),
        (EPOC, 'EPOC'),
        (TABAQUISMO, 'Tabaquismo'),
        (ALCOHOLISMO, 'Alcoholismo'),
        (ENFERMEDAD_RENAL, 'Enfermedad renal crónica'),
        (HEMODIALISIS, 'Hemodiálisis'),
        (ASTMA, 'Asma'),
        (SIDA_VIH, 'Sida / VIH'),
        (ARTRITIS_ARTROSIS, 'Artritis / artrosis'),
        (HERNIA_NUCLEO_PULPOSO, 'Hernia del núcleo pulposo'),
        (ULCERA_GASTRICA, 'Úlcera gástrica'),
        (HIPOTIROIDISMO, 'Hipotiroidismo'),
        (HIPERTIROIDISMO, 'Hipertiroidismo'),
        (OTRO, 'Otro'),
    ]

    enfermedades_cronicas = models.TextField(blank=True, help_text="Seleccione las enfermedades crónicas y especifique otras si selecciona 'Otro'.")
    otras_enfermedades_cronicas = models.CharField(max_length=25, blank=True, help_text="Otras enfermedades crónicas (25 caracteres máx.)")


    def get_enfermedades_cronicas_list(self):
        # Retorna una lista de enfermedades crónicas seleccionadas
        if self.enfermedades_cronicas:
            return [enfermedad.strip() for enfermedad in self.enfermedades_cronicas.split(',') if enfermedad.strip()]
        return []

    def save(self, *args, **kwargs):
        if self.enfermedades_cronicas and self.OTRO in self.enfermedades_cronicas and not self.otras_enfermedades_comunes:
            raise ValidationError("Debe especificar otras cirugías si selecciona 'Otro'.")
        super().save(*args, **kwargs)

    NINGUNA = 'Ninguna'
    COLON_IRRITABLE = 'Colon irritable'
    CANCER = 'Cáncer'
    DEPRESION_ANXIEDAD = 'Depresión, ansiedad'
    CEFALEA = 'Cefalea, dolor de cabeza'
    QUISTES_OVARIOS = 'Quistes ováricos, patología ovárica'
    DEMENCIA = 'Demencia'
    OTRO = 'Otro'

    ENFERMEDADES_COMUNES_CHOICES = [
        (COLON_IRRITABLE, 'Colon irritable'),
        (CANCER, 'Cáncer'),
        (DEPRESION_ANXIEDAD, 'Depresión, ansiedad'),
        (CEFALEA, 'Cefalea, dolor de cabeza'),
        (QUISTES_OVARIOS, 'Quistes ováricos, patología ovárica'),
        (DEMENCIA, 'Demencia'),
        (OTRO, 'Otro'),
    ]

    enfermedades_comunes = models.TextField(blank=True, help_text="Seleccione las enfermedades comunes y especifique otras si selecciona 'Otro'.")
    otras_enfermedades_comunes = models.CharField(max_length=25, blank=True, help_text="Otras enfermedades comunes (25 caracteres máx.)")


    def get_enfermedades_comunes_list(self):
        # Retorna una lista de enfermedades comunes seleccionadas
        if self.enfermedades_comunes:
            return [enfermedad.strip() for enfermedad in self.enfermedades_comunes.split(',') if enfermedad.strip()]
        return []

    def save(self, *args, **kwargs):
        if self.cirugias_comunes and self.OTRO in self.cirugias_comunes and not self.otras_cirugias_comunes:
            raise ValidationError("Debe especificar otras cirugías si selecciona 'Otro'.")
        super().save(*args, **kwargs)

    NINGUNA = 'Ninguna'
    COLECISTECTOMIA = 'Colecistectomía'
    CIRUGIAS_BARIATRICAS = 'Cirugías bariátricas'
    HERNIORRAFIA = 'Herniorrafia'
    CIRUGIA_TORACICA_ONCOLOGICA = 'Cirugía Torácica Oncológica'
    CIRUGIA_DEFORMIDADES_TORAX = 'Cirugía de las Deformidades del Tórax'
    SIMPATECTOMIA = 'Cirugía del Simpático o Simpatectomía'
    TUMORES_MEDIASTINO = 'Tumores de Mediastino'
    TRASPLANTE_PULMONAR = 'Trasplante Pulmonar'
    APENDICECTOMIA = 'Apendicectomía'
    GASTRECTOMIA = 'Gastrectomía por cáncer gástrico'
    PANCREATECTOMIA = 'Pancreatectomía por cáncer de páncreas'
    CIRUGIA_CABEZA_CUELLO = 'Cirugía de Cabeza y Cuello Oncológica'
    LIFTING_CUELLO = 'Lifting de Cuello (Cervicoplastía)'
    CIRUGIA_TIROIDES = 'Cirugía de Tiroides'
    CIRUGIA_PAROTIDA = 'Cirugía de Parótida'
    CIRUGIA_LARINGE = 'Cirugía de Laringe'
    PROSTATECTOMIA = 'Prostatectomía'
    CIRUGIA_CALCULOS_RENALES = 'Cirugía de cálculos renales'
    VASECTOMIA = 'Vasectomía'
    CIRUGIA_CANCER_VEJIGA = 'Cirugía para el cáncer de vejiga'
    CIRUGIA_RECONSTRUCTIVA_UROGENITAL = 'Cirugía reconstructiva urogenital'
    CESAREA = 'Cesárea'
    HISTERECTOMIA = 'Histerectomía'
    LAPAROSCOPIA_GINECOLOGICA = 'Laparoscopía Ginecológica'
    CIRUGIA_PROLAPSO_PELVIANO = 'Cirugía de Prolapso Pelviano'
    CIRUGIA_ONCOLOGICA_GINECOLOGICA = 'Cirugía Oncológica Ginecológica'
    CIRUGIA_CORONARIA = 'Cirugía Coronaria'
    CIRUGIA_VALVULAR = 'Cirugía Valvular'
    CIRUGIA_AORTA_TORACICA = 'Cirugía de la Aorta Torácica'
    CARDIOPATIAS_CONGENITAS = 'Cardiopatías Congénitas del Adulto'
    CIRUGIA_ARRITMIAS = 'Cirugía de Arritmias'
    TUMORES_CARDIACOS = 'Tumores Cardíacos'
    TRASPLANTE_CARDIACO = 'Trasplante Cardíaco y Corazón Artificial'
    PROCEDIMIENTOS_ENDOVASCULARES = 'Procedimientos Endovasculares'
    TRATAMIENTO_VARICES = 'Tratamiento de Várices'
    MANEJO_PATOLOGIA_AORTICA = 'Manejo de Patología Aórtica'
    ENFERMEDAD_ARTERIAL_OCCLUSIVA = 'Enfermedad Arterial Oclusiva'
    ACCESOS_VASCULARES_HEMODIALISIS = 'Accesos Vasculares para Hemodiálisis'
    PREVENCION_TRATAMIENTO_ENFERMEDAD_TROMBOEMBOLICA = 'Prevención y Tratamiento de la Enfermedad Tromboembólica'
    CIRUGIA_CANCER_PIEL = 'Cirugía del cáncer de piel'
    CIRUGIA_LUNARES = 'Cirugía de Lunares (Nevos)'
    CIRUGIA_UNAS = 'Cirugía de uñas'
    EXTIRPACION_LESIONES_CUTANEAS = 'Extirpación de lesiones cutáneas benignas'
    INYECCION_INTRACUTANEA_QUELOIDES = 'Inyección intracutánea de queloides'
    BIOPSIAS_PIEL = 'Biopsias de piel'
    CIRUGIA_CATARATA = 'Cirugía de Catarata'
    CIRUGIA_LASIK = 'Cirugía Lasik'
    VITRECTOMIA = 'Vitrectomía'
    PTERIGION = 'Pterigión'
    GLAUCOMA = 'Glaucoma'
    CHALAZION = 'Chalazión'
    BLEFAROCHALASIS = 'Blefarochalasis'
    CROSSLINKING_QUERATOCONO = 'Crosslinking - Queratocono'
    ENTROPION = 'Entropión'
    FOTCOAGULACION_RETINA = 'Fotocoagulación de Retina'
    IMPLANTE_LENTE_INTRAOCULAR = 'Implante de Lente Intraocular para Corrección de Alta Miopía'
    OTRO = 'Otro'

    CIRUGIAS_COMUNES_CHOICES = [
        (NINGUNA, 'Ninguna'),
        (COLECISTECTOMIA, 'Colecistectomía (extracción de vesícula)'),
        (CIRUGIAS_BARIATRICAS, 'Cirugías bariátricas'),
        (HERNIORRAFIA, 'Herniorrafia'),
        (CIRUGIA_TORACICA_ONCOLOGICA, 'Cirugía Torácica Oncológica'),
        (CIRUGIA_DEFORMIDADES_TORAX, 'Cirugía de las Deformidades del Tórax'),
        (SIMPATECTOMIA, 'Cirugía del Simpático o Simpatectomía'),
        (TUMORES_MEDIASTINO, 'Tumores de Mediastino'),
        (TRASPLANTE_PULMONAR, 'Trasplante Pulmonar'),
        (APENDICECTOMIA, 'Apendicectomía'),
        (GASTRECTOMIA, 'Gastrectomía por cáncer gástrico'),
        (PANCREATECTOMIA, 'Pancreatectomía por cáncer de páncreas'),
        (CIRUGIA_CABEZA_CUELLO, 'Cirugía de Cabeza y Cuello Oncológica'),
        (LIFTING_CUELLO, 'Lifting de Cuello (Cervicoplastía)'),
        (CIRUGIA_TIROIDES, 'Cirugía de Tiroides'),
        (CIRUGIA_PAROTIDA, 'Cirugía de Parótida'),
        (CIRUGIA_LARINGE, 'Cirugía de Laringe'),
        (PROSTATECTOMIA, 'Prostatectomía'),
        (CIRUGIA_CALCULOS_RENALES, 'Cirugía de cálculos renales'),
        (VASECTOMIA, 'Vasectomía'),
        (CIRUGIA_CANCER_VEJIGA, 'Cirugía para el cáncer de vejiga'),
        (CIRUGIA_RECONSTRUCTIVA_UROGENITAL, 'Cirugía reconstructiva urogenital'),
        (CESAREA, 'Cesárea'),
        (HISTERECTOMIA, 'Histerectomía'),
        (LAPAROSCOPIA_GINECOLOGICA, 'Laparoscopía Ginecológica'),
        (CIRUGIA_PROLAPSO_PELVIANO, 'Cirugía de Prolapso Pelviano'),
        (CIRUGIA_ONCOLOGICA_GINECOLOGICA, 'Cirugía Oncológica Ginecológica'),
        (CIRUGIA_CORONARIA, 'Cirugía Coronaria'),
        (CIRUGIA_VALVULAR, 'Cirugía Valvular'),
        (CIRUGIA_AORTA_TORACICA, 'Cirugía de la Aorta Torácica'),
        (CARDIOPATIAS_CONGENITAS, 'Cardiopatías Congénitas del Adulto'),
        (CIRUGIA_ARRITMIAS, 'Cirugía de Arritmias'),
        (TUMORES_CARDIACOS, 'Tumores Cardíacos'),
        (TRASPLANTE_CARDIACO, 'Trasplante Cardíaco y Corazón Artificial'),
        (PROCEDIMIENTOS_ENDOVASCULARES, 'Procedimientos Endovasculares'),
        (TRATAMIENTO_VARICES, 'Tratamiento de Várices'),
        (MANEJO_PATOLOGIA_AORTICA, 'Manejo de Patología Aórtica'),
        (ENFERMEDAD_ARTERIAL_OCCLUSIVA, 'Enfermedad Arterial Oclusiva'),
        (ACCESOS_VASCULARES_HEMODIALISIS, 'Accesos Vasculares para Hemodiálisis'),
        (PREVENCION_TRATAMIENTO_ENFERMEDAD_TROMBOEMBOLICA, 'Prevención y Tratamiento de la Enfermedad Tromboembólica'),
        (CIRUGIA_CANCER_PIEL, 'Cirugía del cáncer de piel'),
        (CIRUGIA_LUNARES, 'Cirugía de Lunares (Nevos)'),
        (CIRUGIA_UNAS, 'Cirugía de uñas'),
        (EXTIRPACION_LESIONES_CUTANEAS, 'Extirpación de lesiones cutáneas benignas'),
        (INYECCION_INTRACUTANEA_QUELOIDES, 'Inyección intracutánea de queloides'),
        (BIOPSIAS_PIEL, 'Biopsias de piel'),
        (CIRUGIA_CATARATA, 'Cirugía de Catarata'),
        (CIRUGIA_LASIK, 'Cirugía Lasik'),
        (VITRECTOMIA, 'Vitrectomía'),
        (PTERIGION, 'Pterigión'),
        (GLAUCOMA, 'Glaucoma'),
        (CHALAZION, 'Chalazión'),
        (BLEFAROCHALASIS, 'Blefarochalasis'),
        (CROSSLINKING_QUERATOCONO, 'Crosslinking - Queratocono'),
        (ENTROPION, 'Entropión'),
        (FOTCOAGULACION_RETINA, 'Fotocoagulación de Retina'),
        (IMPLANTE_LENTE_INTRAOCULAR, 'Implante de Lente Intraocular para Corrección de Alta Miopía'),
        (OTRO, 'Otro'),
    ]

    cirugias_comunes = models.TextField(blank=True, help_text="Seleccione las cirugías comunes y especifique otras si selecciona 'Otro'.")
    otras_cirugias_comunes = models.CharField(max_length=25, blank=True, help_text="Otras cirugías comunes (25 caracteres máx.)")

    def get_cirugias_comunes_list(self):
        # Retorna una lista de cirugías comunes seleccionadas
        if self.cirugias_comunes:
            return [cirugia.strip() for cirugia in self.cirugias_comunes.split(',') if cirugia.strip()]
        return []

    def save(self, *args, **kwargs):
        if self.cirugias_comunes and self.OTRO in self.cirugias_comunes and not self.otras_cirugias_comunes:
            raise ValidationError("Debe especificar otras cirugías si selecciona 'Otro'.")
        super().save(*args, **kwargs)

     # Opciones de cirugías traumatológicas
    NINGUNA = 'Ninguna'
    COLECISTECTOMIA = 'Colecistectomía'
    CIRUGIAS_BARIATRICAS = 'Cirugías bariátricas'
    HERNIORRAFIA = 'Herniorrafia'
    CIRUGIA_TORACICA_ONCOLOGICA = 'Cirugía Torácica Oncológica'
    CIRUGIA_DEFORMIDADES_TORAX = 'Cirugía de las Deformidades del Tórax'
    SIMPATECTOMIA = 'Cirugía del Simpático o Simpatectomía'
    TUMORES_MEDIOSTINO = 'Tumores de Mediastino'
    TRASPLANTE_PULMONAR = 'Trasplante Pulmonar'
    APENDICECTOMIA = 'Apendicectomía'
    GASTRECTOMIA = 'Gastrectomía por cáncer gástrico'
    PANCREATECTOMIA = 'Pancreatectomía por cáncer de páncreas'
    CIRUGIA_CABEZA_CUELLO_ONCOLOGICA = 'Cirugía de Cabeza y Cuello Oncológica'
    LIFTING_CUELLO = 'Lifting de Cuello (Cervicoplastía)'
    CIRUGIA_TIROIDES = 'Cirugía de Tiroides'
    CIRUGIA_PAROTIDA = 'Cirugía de Parótida'
    CIRUGIA_LARINGE = 'Cirugía de Laringe'
    PROSTATECTOMIA = 'Prostatectomía'
    CIRUGIA_CALCULOS_RENALES = 'Cirugía de cálculos renales'
    VASECTOMIA = 'Vasectomía'
    CIRUGIA_CANCER_VEJIGA = 'Cirugía para el cáncer de vejiga'
    CIRUGIA_RECONSTRUCTIVA_UROGENITAL = 'Cirugía reconstructiva urogenital'
    CESAREA = 'Cesárea'
    HISTERECTOMIA = 'Histerectomía'
    LAPAROSCOPIA_GINECOLOGICA = 'Laparoscopía Ginecológica'
    CIRUGIA_PROLAPSO_PELVIANO = 'Cirugía de Prolapso Pelviano'
    CIRUGIA_ONCOLOGICA_GINECOLOGICA = 'Cirugía Oncológica Ginecológica'
    CIRUGIA_CORONARIA = 'Cirugía Coronaria'
    CIRUGIA_VALVULAR = 'Cirugía Valvular'
    CIRUGIA_AORTICA_TORACICA = 'Cirugía de la Aorta Torácica'
    CARDIOPATIAS_CONGENITAS_ADULTO = 'Cardiopatías Congénitas del Adulto'
    CIRUGIA_ARRITMIAS = 'Cirugía de Arritmias'
    TUMORES_CARDIACOS = 'Tumores Cardíacos'
    TRASPLANTE_CARDIACO = 'Trasplante Cardíaco'
    PROCEDIMIENTOS_ENDOVASCULARES = 'Procedimientos Endovasculares'
    TRATAMIENTO_VARICES = 'Tratamiento de Várices'
    MANEJO_PATHOLOGIA_AORTICA = 'Manejo de Patología Aórtica'
    ENFERMEDAD_ARTERIAL_OCCLUSIVA = 'Enfermedad Arterial Oclusiva'
    ACCESOS_VASCULARES_HEMODIALISIS = 'Accesos Vasculares para Hemodiálisis'
    PREVENCION_TRATAMIENTO_ENFERMEDAD_TROMBOEMBOLICA = 'Prevención y Tratamiento de la Enfermedad Tromboembólica'
    CIRUGIA_CANCER_PIEL = 'Cirugía del cáncer de piel'
    CIRUGIA_LUNARES = 'Cirugía de Lunares (Nevos)'
    CIRUGIA_UNAS = 'Cirugía de uñas'
    EXTIRPACION_LESIONES_CUTANEAS = 'Extirpación de lesiones cutáneas benignas'
    INYECCION_QUELOIDES = 'Inyección intracutánea de queloides'
    BIOPSIAS_PIEL = 'Biopsias de piel'
    CIRUGIA_CATARATA = 'Cirugía de Catarata'
    CIRUGIA_LASIK = 'Cirugía Lasik'
    VITRECTOMIA = 'Vitrectomía'
    PTERIGION = 'Pterigión'
    GLAUCOMA = 'Glaucoma'
    CHALAZION = 'Chalazión'
    BLEFAROCHALASIS = 'Blefarochalasis'
    CROSSLINKING_QUERATOCONO = 'Crosslinking - Queratocono'
    ENTROPION = 'Entropión'
    FOTOCOAGULACION_RETINA = 'Fotocoagulación de Retina'
    IMPLANTE_LENTE_ALTA_MIOPIA = 'Implante de Lente Intraocular para Corrección de Alta Miopía'
    OTRO = 'Otro'

    CIRUGIAS_TRAUMATOLOGICAS_CHOICES = [
        (NINGUNA, 'Ninguna'),
        (COLECISTECTOMIA, 'Colecistectomía (extracción de vesícula)'),
        (CIRUGIAS_BARIATRICAS, 'Cirugías bariátricas'),
        (HERNIORRAFIA, 'Herniorrafia'),
        (CIRUGIA_TORACICA_ONCOLOGICA, 'Cirugía Torácica Oncológica'),
        (CIRUGIA_DEFORMIDADES_TORAX, 'Cirugía de las Deformidades del Tórax'),
        (SIMPATECTOMIA, 'Cirugía del Simpático o Simpatectomía'),
        (TUMORES_MEDIOSTINO, 'Tumores de Mediastino'),
        (TRASPLANTE_PULMONAR, 'Trasplante Pulmonar'),
        (APENDICECTOMIA, 'Apendicectomía'),
        (GASTRECTOMIA, 'Gastrectomía por cáncer gástrico'),
        (PANCREATECTOMIA, 'Pancreatectomía por cáncer de páncreas'),
        (CIRUGIA_CABEZA_CUELLO_ONCOLOGICA, 'Cirugía de Cabeza y Cuello Oncológica'),
        (LIFTING_CUELLO, 'Lifting de Cuello (Cervicoplastía)'),
        (CIRUGIA_TIROIDES, 'Cirugía de Tiroides'),
        (CIRUGIA_PAROTIDA, 'Cirugía de Parótida'),
        (CIRUGIA_LARINGE, 'Cirugía de Laringe'),
        (PROSTATECTOMIA, 'Prostatectomía'),
        (CIRUGIA_CALCULOS_RENALES, 'Cirugía de cálculos renales'),
        (VASECTOMIA, 'Vasectomía'),
        (CIRUGIA_CANCER_VEJIGA, 'Cirugía para el cáncer de vejiga'),
        (CIRUGIA_RECONSTRUCTIVA_UROGENITAL, 'Cirugía reconstructiva urogenital'),
        (CESAREA, 'Cesárea'),
        (HISTERECTOMIA, 'Histerectomía'),
        (LAPAROSCOPIA_GINECOLOGICA, 'Laparoscopía Ginecológica'),
        (CIRUGIA_PROLAPSO_PELVIANO, 'Cirugía de Prolapso Pelviano'),
        (CIRUGIA_ONCOLOGICA_GINECOLOGICA, 'Cirugía Oncológica Ginecológica'),
        (CIRUGIA_CORONARIA, 'Cirugía Coronaria'),
        (CIRUGIA_VALVULAR, 'Cirugía Valvular'),
        (CIRUGIA_AORTICA_TORACICA, 'Cirugía de la Aorta Torácica'),
        (CARDIOPATIAS_CONGENITAS_ADULTO, 'Cardiopatías Congénitas del Adulto'),
        (CIRUGIA_ARRITMIAS, 'Cirugía de Arritmias'),
        (TUMORES_CARDIACOS, 'Tumores Cardíacos'),
        (TRASPLANTE_CARDIACO, 'Trasplante Cardíaco'),
        (PROCEDIMIENTOS_ENDOVASCULARES, 'Procedimientos Endovasculares'),
        (TRATAMIENTO_VARICES, 'Tratamiento de Várices'),
        (MANEJO_PATHOLOGIA_AORTICA, 'Manejo de Patología Aórtica'),
        (ENFERMEDAD_ARTERIAL_OCCLUSIVA, 'Enfermedad Arterial Oclusiva'),
        (ACCESOS_VASCULARES_HEMODIALISIS, 'Accesos Vasculares para Hemodiálisis'),
        (PREVENCION_TRATAMIENTO_ENFERMEDAD_TROMBOEMBOLICA, 'Prevención y Tratamiento de la Enfermedad Tromboembólica'),
        (CIRUGIA_CANCER_PIEL, 'Cirugía del cáncer de piel'),
        (CIRUGIA_LUNARES, 'Cirugía de Lunares (Nevos)'),
        (CIRUGIA_UNAS, 'Cirugía de uñas'),
        (EXTIRPACION_LESIONES_CUTANEAS, 'Extirpación de lesiones cutáneas benignas'),
        (INYECCION_QUELOIDES, 'Inyección intracutánea de queloides'),
        (BIOPSIAS_PIEL, 'Biopsias de piel'),
        (CIRUGIA_CATARATA, 'Cirugía de Catarata'),
        (CIRUGIA_LASIK, 'Cirugía Lasik'),
        (VITRECTOMIA, 'Vitrectomía'),
        (PTERIGION, 'Pterigión'),
        (GLAUCOMA, 'Glaucoma'),
        (CHALAZION, 'Chalazión'),
        (BLEFAROCHALASIS, 'Blefarochalasis'),
        (CROSSLINKING_QUERATOCONO, 'Crosslinking - Queratocono'),
        (ENTROPION, 'Entropión'),
        (FOTOCOAGULACION_RETINA, 'Fotocoagulación de Retina'),
        (IMPLANTE_LENTE_ALTA_MIOPIA, 'Implante de Lente Intraocular para Corrección de Alta Miopía'),
        (OTRO, 'Otro')
    ]

    cirugias_traumatologicas = models.TextField(blank=True, help_text="Seleccione las cirugías traumatológicas y especifique otras si selecciona 'Otro'.")
    otras_cirugias_traumatologicas = models.CharField(max_length=25, blank=True, help_text="Otras cirugías traumatológicas (25 caracteres máx.)")

    def get_cirugias_traumatologicas_list(self):
        # Retorna una lista de cirugías traumatológicas seleccionadas
        if self.cirugias_traumatologicas:
            return [cirugia.strip() for cirugia in self.cirugias_traumatologicas.split(',') if cirugia.strip()]
        return []

    def save(self, *args, **kwargs):
        if self.cirugias_comunes and self.OTRO in self.cirugias_comunes and not self.otras_cirugias_comunes:
            raise ValidationError("Debe especificar otras cirugías si selecciona 'Otro'.")
        super().save(*args, **kwargs)

    cirugias_traumatologicas = models.TextField(blank=True, help_text="Seleccione las cirugías traumatológicas y especifique otras si selecciona 'Otro'.")
    otras_cirugias_traumatologicas = models.CharField(max_length=25, blank=True, help_text="Otras cirugías traumatológicas (25 caracteres máx.)")




    # Opciones de fármacos para patologías crónicas
    LOSARTAN = 'Losartán'
    ENALAPRIL = 'Enalapril'
    METFORMINA = 'Metformina'
    ATORVASTATINA = 'Atorvastatina'
    INSULINA = 'Insulina'
    AMLODIPINO = 'Amlodipino'
    SALBUTAMOL = 'Salbutamol'
    OMEPRAZOL = 'Omeprazol'
    LEVOTIROXINA = 'Levotiroxina'
    GLIBENCLAMIDA = 'Glibenclamida'
    NINGUNA = 'NINGUNA'
    OTRO = 'Otro'

    FARMACOS_CHOICES = [
        (LOSARTAN, 'Losartán'),
        (ENALAPRIL, 'Enalapril'),
        (METFORMINA, 'Metformina'),
        (ATORVASTATINA, 'Atorvastatina'),
        (INSULINA, 'Insulina'),
        (AMLODIPINO, 'Amlodipino'),
        (SALBUTAMOL, 'Salbutamol'),
        (OMEPRAZOL, 'Omeprazol'),
        (LEVOTIROXINA, 'Levotiroxina'),
        (GLIBENCLAMIDA, 'Glibenclamida'),
        (NINGUNA, 'NINGUNA'),
        (OTRO, 'Otro')
    ]

    farmacos_patologias_cronicas = models.TextField(blank=True, help_text="Seleccione los fármacos utilizados para patologías crónicas y especifique otros si selecciona 'Otro'.")
    otros_farmacos_patologias_cronicas = models.CharField(max_length=25, blank=True, help_text="Otros fármacos utilizados para patologías crónicas (25 caracteres máx.)")
    detalle_farmacos_cronicos = models.CharField(max_length=60, blank=True, null=True)



    def get_farmacos_patologias_cronicas_list(self):
        # Retorna una lista de fármacos utilizados para patologías crónicas
        if self.farmacos_patologias_cronicas:
            return [farmaco.strip() for farmaco in self.farmacos_patologias_cronicas.split(',') if farmaco.strip()]
        return []

    def save(self, *args, **kwargs):
        if self.farmacos_patologias_cronicas and self.OTRO in self.farmacos_patologias_cronicas and not self.otros_farmacos_patologias_cronicas:
            raise ValidationError("Debe especificar otras cirugías si selecciona 'Otro'.")
        super().save(*args, **kwargs)


    # Opciones de fármacos más usados en Chile (no crónicos)
    PARACETAMOL = 'Paracetamol'
    IBUPROFENO = 'Ibuprofeno'
    KETOROLACO = 'Ketorolaco'
    CLORFENAMINA = 'Clorfenamina'
    DICLOFENACO = 'Diclofenaco'
    LOPERAMIDA = 'Loperamida'
    FAMOTIDINA = 'Famotidina'
    NAPROXENO = 'Naproxeno'
    ACIDO_MEFENAMICO = 'Ácido Mefenámico'
    CIPROFLOXACINA = 'Ciprofloxacina'
    NINGUNA = 'NINGUNA'
    OTRO = 'Otro'

    FARMACOS_NO_CRONICOS_CHOICES = [
        (PARACETAMOL, 'Paracetamol'),
        (IBUPROFENO, 'Ibuprofeno'),
        (KETOROLACO, 'Ketorolaco'),
        (CLORFENAMINA, 'Clorfenamina'),
        (DICLOFENACO, 'Diclofenaco'),
        (LOPERAMIDA, 'Loperamida'),
        (FAMOTIDINA, 'Famotidina'),
        (NAPROXENO, 'Naproxeno'),
        (ACIDO_MEFENAMICO, 'Ácido Mefenámico'),
        (CIPROFLOXACINA, 'Ciprofloxacina'),
        (NINGUNA, 'NINGUNA'),
        (OTRO, 'Otro')
    ]
    farmacos_no_cronicos = models.TextField(blank=True, help_text="Seleccione los fármacos más usados en Chile (no crónicos) y especifique otros si selecciona 'NINGUNA'.")
    otros_farmacos_no_cronicos = models.CharField(max_length=25, blank=True, help_text="Otros fármacos (25 caracteres máx.)")
    detalle_farmacos_no_cronicos = models.CharField(max_length=60, blank=True, null=True)



    def get_farmacos_no_cronicos_list(self):
        # Retorna una lista de fármacos no crónicos seleccionados
        if self.farmacos_no_cronicos:
            return [farmaco.strip() for farmaco in self.farmacos_no_cronicos.split(',') if farmaco.strip()]
        return []

    def save(self, *args, **kwargs):
        if self.farmacos_no_cronicos and self.OTRO in self.farmacos_no_cronicos and not self.otros_farmacos_no_cronicos:
            raise ValidationError("Debe especificar otras cirugías si selecciona 'Otro'.")
        super().save(*args, **kwargs)


     # Opciones de alergias a fármacos más comunes
    PENICILINA = 'Penicilina'
    AINEs = 'Antiinflamatorios no esteroidales (AINEs)'
    ANESTESICOS = 'Anestésicos locales y generales'
    MEDIOS_CONTRASTE = 'Medios de contraste radiológicos'
    ANTICONVULSIVANTES = 'Anticonvulsivantes'
    BETALACTAMICOS = 'Betalactámicos'
    CEFALOSPORINAS = 'Cefalosporinas'
    SULFAS = 'Sulfas'
    ASPIRINA = 'Aspirina'
    DIPIRONA = 'Dipirona'
    NINGUNA = 'NINGUNA'
    OTRO = 'Otro'

    ALERGIAS_FARMACOS_CHOICES = [
        (PENICILINA, 'Penicilina'),
        (AINEs, 'Antiinflamatorios no esteroidales (AINEs)'),
        (ANESTESICOS, 'Anestésicos locales y generales'),
        (MEDIOS_CONTRASTE, 'Medios de contraste radiológicos'),
        (ANTICONVULSIVANTES, 'Anticonvulsivantes'),
        (BETALACTAMICOS, 'Betalactámicos'),
        (CEFALOSPORINAS, 'Cefalosporinas'),
        (SULFAS, 'Sulfas'),
        (ASPIRINA, 'Aspirina'),
        (DIPIRONA, 'Dipirona'),
        (NINGUNA, 'NINGUNA'),
        (OTRO, 'Otro')
    ]
    alergias_farmacos = models.TextField(blank=True, help_text="Seleccione las alergias a fármacos más comunes y especifique otras si selecciona 'Otro'.")
    otras_alergias_farmacos = models.CharField(max_length=25, blank=True, help_text="Otras alergias a fármacos (25 caracteres máx.)")
    detalle_alergias_farmacos = models.CharField(max_length=60, blank=True, null=True)



    def get_alergias_farmacos_list(self):
        # Retorna una lista de alergias a fármacos seleccionadas
        if self.alergias_farmacos:
            return [alergia.strip() for alergia in self.alergias_farmacos.split(',') if alergia.strip()]
        return []

    def save(self, *args, **kwargs):
        if self.alergias_farmacos and self.OTRO in self.alergias_farmacos and not self.otras_alergias_farmacos:
            raise ValidationError("Debe especificar otras cirugías si selecciona 'Otro'.")
        super().save(*args, **kwargs)


    # Opciones de alergias más comunes en Chile (no fármacos)
    POLENES = 'Pólenes'
    PASTOS = 'Pastos'
    MALEZAS = 'Malezas'
    ARBOLES = 'Árboles'
    HONGOS = 'Hongos ambientales'
    ACAROS = 'Ácaros como dermatofagoides'
    ALIMENTOS = 'Alimentos'
    PICADURAS = 'Picaduras de abejas/avispas'
    POLVO = 'Polvo'
    ANIMALES = 'Animales domésticos'
    OTRO = 'Otro'
    NINGUNA = 'NINGUNA'

    ALERGIAS_COMUNES_CHOICES = [
        (POLENES, 'Pólenes'),
        (PASTOS, 'Pastos'),
        (MALEZAS, 'Malezas'),
        (ARBOLES, 'Árboles'),
        (HONGOS, 'Hongos ambientales'),
        (ACAROS, 'Ácaros como dermatofagoides'),
        (ALIMENTOS, 'Alimentos'),
        (PICADURAS, 'Picaduras de abejas/avispas'),
        (POLVO, 'Polvo'),
        (ANIMALES, 'Animales domésticos'),
        (OTRO, 'Otro')
    ]

    alergias_comunes = models.TextField(blank=True, help_text="Seleccione las alergias más comunes y especifique otras si selecciona 'Otro'.")
    otras_alergias_comunes = models.CharField(max_length=25, blank=True, help_text="Otras alergias comunes (25 caracteres máx.)")
    detalle_alergias_no_farmacos = models.CharField(max_length=60, blank=True, null=True)


    def get_alergias_comunes_list(self):
        # Retorna una lista de alergias comunes seleccionadas
        if self.alergias_comunes:
            return [alergia.strip() for alergia in self.alergias_comunes.split(',') if alergia.strip()]
        return []

    def save(self, *args, **kwargs):
        if self.alergias_comunes and self.OTRO in self.alergias_comunes and not self.otras_alergias_comunes:
            raise ValidationError("Debe especificar otras cirugías si selecciona 'Otro'.")
        super().save(*args, **kwargs)


    # Campos para detalles adicionales
    otros_antecedentes = models.CharField(max_length=60, blank=True, null=True)
    
    motivo_consulta_texto = models.CharField(max_length=60, blank=True, null=True)


    
    SI = 'Sí'
    NO = 'No'
    OTRO = 'Otro'

    CENTRO_SALUD_CHOICES = [
        (SI, 'Sí'),
        (NO, 'No'),
        (OTRO, 'Otro'),
    ]

    centro_salud_previo = models.CharField(max_length=5, choices=CENTRO_SALUD_CHOICES)
    otro_centro_salud = models.CharField(max_length=25, blank=True, help_text="Especifique otro centro de salud (25 caracteres máx.)")


    def save(self, *args, **kwargs):
        # Valida si se seleccionó 'Otro' y si se ingresó un valor en 'otro_centro_salud'
        if self.centro_salud_previo == self.OTRO and not self.otro_centro_salud:
            raise ValidationError("Debe especificar el centro de salud si selecciona 'Otro'.")
        super().save(*args, **kwargs)


    SI = 'Sí'
    NO = 'No'
    PARCIALMENTE = 'Parcialmente'
    OTRO = 'Otro'

    RESOLUCION_SALUD_CHOICES = [
        (SI, 'Sí'),
        (NO, 'No'),
        (PARCIALMENTE, 'Parcialmente'),
        (OTRO, 'Otro'),
    ]

    resolucion_problema_salud = models.CharField(max_length=12, choices=RESOLUCION_SALUD_CHOICES)
    otro_resolucion_salud = models.CharField(max_length=25, blank=True, help_text="Especifique otro (25 caracteres máx.)")


    def save(self, *args, **kwargs):
        # Valida si se seleccionó 'Otro' y si se ingresó un valor en 'otro_resolucion_salud'
        if self.resolucion_problema_salud == self.OTRO and not self.otro_resolucion_salud:
            raise ValidationError("Debe especificar el resultado si selecciona 'Otro'.")
        super().save(*args, **kwargs)   

    # Definimos las opciones
    DOLOR_ABDOMINAL_AGUDO = 'Dolor abdominal agudo (de inicio reciente)'
    DOLOR_ABDOMINAL_CRONICO = 'Dolor abdominal crónico (de inicio antiguo)'
    DOLOR_TORACICO_AGUDO = 'Dolor torácico agudo (de inicio reciente)'
    DIFICULTAD_RESPIRATORIA = 'Dificultad respiratoria'
    FIEBRE_ALTA = 'Fiebre alta (38,0 °)'
    TRAUMATISMOS = 'Traumatismos (caídas, golpes, agresiones)'
    CEFALEA_INTENSA = 'Cefalea intensa (dolor de cabeza)'
    SINTOMAS_INFECCION_URINARIA = 'Síntomas de infección urinaria'
    CRISIS_HIPERTENSIVA = 'Crisis hipertensiva (presión alta)'
    SINTOMAS_GASTROINTESTINALES = 'Síntomas gastrointestinales (náuseas, vómitos, dolor abdominal, diarrea, constipado, etc)'
    DESCOMPENSACION_DIABETES = 'Descompensación de diabetes (azúcar muy alta o muy baja)'
    REACCIONES_ALERGICAS = 'Reacciones alérgicas (lesiones rojizas en piel, picazón en una o varias zonas del cuerpo, falta de aire)'
    SINTOMAS_ENFERMEDAD_CEREBROVASCULAR = 'Síntomas de enfermedad cerebrovascular'
    CRISIS_EPILEPTICAS = 'Crisis epilépticas (convulsiones)'
    SINTOMAS_INFARTO_MIOCARDIO = 'Síntomas de infarto de miocardio (dolor en el pecho)'
    INFECCIONES_RESPIRATORIAS_AGUDAS = 'Infecciones respiratorias agudas'
    INTOXICACIONES = 'Intoxicaciones'
    HERIDAS_LACERACIONES = 'Heridas y laceraciones'
    QUEMADURAS = 'Quemaduras'
    MORDEDURAS_ANIMALES = 'Mordeduras de animales'
    PICADURAS_INSECTOS = 'Picaduras de insectos'
    ACCIDENTES_TRANSITO = 'Accidentes de tránsito'
    PROBLEMAS_PSIQUIATRICOS_AGUDOS = 'Problemas psiquiátricos agudos'
    SINTOMAS_APENDICITIS = 'Síntomas de apendicitis'
    ALTERACIONES_ESTADO_CONCIENCIA = 'Alteraciones del estado de conciencia'
    DOLOR_LUMBAR_AGUDO = 'Dolor lumbar agudo'
    DERIVADO_MEDICO_EXTERNO = 'Derivado por un médico externo'
    ACCIDENTE_TRABAJO = 'Accidente en el trabajo'
    ACCIDENTE_TRAYECTO_TRABAJO = 'Accidente en trayecto hacia / desde el trabajo'
    ACCIDENTE_COLEGIO = 'Accidente en el colegio o centro de estudios'
    ACCIDENTE_TRAYECTO_COLEGIO = 'Accidente en trayecto hacia / desde colegio o centro de estudios'
    OTROS = 'Otros'

    MOTIVO_CONSULTA_CHOICES = [
        (DOLOR_ABDOMINAL_AGUDO, 'Dolor abdominal agudo (de inicio reciente)'),
        (DOLOR_ABDOMINAL_CRONICO, 'Dolor abdominal crónico (de inicio antiguo)'),
        (DOLOR_TORACICO_AGUDO, 'Dolor torácico agudo (de inicio reciente)'),
        (DIFICULTAD_RESPIRATORIA, 'Dificultad respiratoria'),
        (FIEBRE_ALTA, 'Fiebre alta (38,0 °)'),
        (TRAUMATISMOS, 'Traumatismos (caídas, golpes, agresiones)'),
        (CEFALEA_INTENSA, 'Cefalea intensa (dolor de cabeza)'),
        (SINTOMAS_INFECCION_URINARIA, 'Síntomas de infección urinaria'),
        (CRISIS_HIPERTENSIVA, 'Crisis hipertensiva (presión alta)'),
        (SINTOMAS_GASTROINTESTINALES, 'Síntomas gastrointestinales'),
        (DESCOMPENSACION_DIABETES, 'Descompensación de diabetes'),
        (REACCIONES_ALERGICAS, 'Reacciones alérgicas'),
        (SINTOMAS_ENFERMEDAD_CEREBROVASCULAR, 'Síntomas de enfermedad cerebrovascular'),
        (CRISIS_EPILEPTICAS, 'Crisis epilépticas'),
        (SINTOMAS_INFARTO_MIOCARDIO, 'Síntomas de infarto de miocardio'),
        (INFECCIONES_RESPIRATORIAS_AGUDAS, 'Infecciones respiratorias agudas'),
        (INTOXICACIONES, 'Intoxicaciones'),
        (HERIDAS_LACERACIONES, 'Heridas y laceraciones'),
        (QUEMADURAS, 'Quemaduras'),
        (MORDEDURAS_ANIMALES, 'Mordeduras de animales'),
        (PICADURAS_INSECTOS, 'Picaduras de insectos'),
        (ACCIDENTES_TRANSITO, 'Accidentes de tránsito'),
        (PROBLEMAS_PSIQUIATRICOS_AGUDOS, 'Problemas psiquiátricos agudos'),
        (SINTOMAS_APENDICITIS, 'Síntomas de apendicitis'),
        (ALTERACIONES_ESTADO_CONCIENCIA, 'Alteraciones del estado de conciencia'),
        (DOLOR_LUMBAR_AGUDO, 'Dolor lumbar agudo'),
        (DERIVADO_MEDICO_EXTERNO, 'Derivado por un médico externo'),
        (ACCIDENTE_TRABAJO, 'Accidente en el trabajo'),
        (ACCIDENTE_TRAYECTO_TRABAJO, 'Accidente en trayecto hacia / desde el trabajo'),
        (ACCIDENTE_COLEGIO, 'Accidente en el colegio o centro de estudios'),
        (ACCIDENTE_TRAYECTO_COLEGIO, 'Accidente en trayecto hacia / desde colegio o centro de estudios'),
        (OTROS, 'Otros'),
    ]

    # Campos del modelo
    motivo_consulta = models.TextField(blank=True, help_text="Seleccione uno o varios motivos de consulta.")
    otros_motivos = models.CharField(max_length=50, blank=True, help_text="Especifique otros motivos (50 caracteres máx.).")


    def get_motivo_consulta_list(self):
        # Retorna una lista de motivos de consulta seleccionados
        if self.motivo_consulta:
            return [motivo.strip() for motivo in self.motivo_consulta.split(',') if motivo.strip()]
        return []

    def save(self, *args, **kwargs):
        # Validar si se selecciona "Otros" y no se especifican más detalles
        if self.OTROS in self.motivo_consulta and not self.otros_motivos:
            raise ValidationError("Debe especificar otros motivos si selecciona 'Otros'.")
        # Guarda el modelo
        super().save(*args, **kwargs)     

    # Definimos las opciones
    MINUTOS = 'Minutos'
    HORAS = 'Horas'
    DIAS = 'Días'
    SEMANAS = 'Semanas'
    MESES = 'Meses'
    ANOS = 'Años'

    TIEMPO_SINTOMAS_CHOICES = [
        (MINUTOS, 'Minutos'),
        (HORAS, 'Horas'),
        (DIAS, 'Días'),
        (SEMANAS, 'Semanas'),
        (MESES, 'Meses'),
        (ANOS, 'Años'),
    ]

    # Campos del modelo
    tiempo_sintomas = models.CharField(
        max_length=20,
        choices=TIEMPO_SINTOMAS_CHOICES,
        help_text="Seleccione aproximadamente hace cuánto comenzaron los síntomas."
    )

     # Opciones
    SI = 'Sí'
    NO = 'No'

    EXPERIMENTADO_PROBLEMA_CHOICES = [
        (SI, 'Sí'),
        (NO, 'No'),
    ]

    # Campos del modelo
    experimentado_problema_anteriormente = models.CharField(
        max_length=2,
        choices=EXPERIMENTADO_PROBLEMA_CHOICES,
        help_text="Seleccione si ha experimentado este problema anteriormente."
    )
    
    # Opciones de frecuencia
    DIARIA = 'Diaria'
    SEMANAL = 'Semanal'
    MENSUAL = 'Mensual'
    ANUAL = 'Anual'
    OTROS = 'Otros'

    FRECUENCIA_CHOICES = [
        (DIARIA, 'Diaria'),
        (SEMANAL, 'Semanal'),
        (MENSUAL, 'Mensual'),
        (ANUAL, 'Anual'),
        (OTROS, 'Otros'),
    ]

    # Campos del modelo
    frecuencia_problema = models.CharField(max_length=7,choices=FRECUENCIA_CHOICES,help_text="Seleccione con qué frecuencia ha experimentado este problema.")
    frecuencia_otros = models.CharField(max_length=50,blank=True,help_text="Especifique la frecuencia si selecciona 'Otros'.")


    def save(self, *args, **kwargs):
        # Validación si se selecciona "Otros" y no se proporciona un valor en 'frecuencia_otros'
        if self.frecuencia_problema == self.OTROS and not self.frecuencia_otros:
            raise ValidationError("Debe especificar la frecuencia si selecciona 'Otros'.")
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        db_table = 'paciente'

    def __str__(self):
        return self.nombre_completo if self.nombre_completo else "Paciente sin nombre"
