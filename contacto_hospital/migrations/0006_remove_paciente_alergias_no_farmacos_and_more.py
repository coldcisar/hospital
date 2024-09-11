# Generated by Django 5.0.7 on 2024-09-11 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto_hospital', '0005_alter_paciente_alergias_farmacos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='alergias_no_farmacos',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='enfermedades_cronicas',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='farmacos_cronicos',
        ),
        migrations.AddField(
            model_name='paciente',
            name='alergias_comunes',
            field=models.ManyToManyField(blank=True, choices=[('polenes', 'Pólenes'), ('pastos', 'Pastos'), ('malezas', 'Malezas'), ('arboles', 'Árboles'), ('hongos', 'Hongos ambientales'), ('acaros', 'Ácaros como dermatofagoides'), ('alimentos', 'Alimentos'), ('picaduras', 'Picaduras de abejas/avispas'), ('polvo', 'Polvo'), ('animales_domesticos', 'Animales domésticos'), ('otros', 'Otros (campo alfabético libre de 25 caracteres)')], to='contacto_hospital.paciente'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='condiciones_cronicas',
            field=models.ManyToManyField(blank=True, choices=[('infarto_corazon', 'Infarto al corazón, "ataque al corazón", IAM'), ('infarto_cerebral', 'Infarto cerebral, AVE, ACV, accidente cerebro vascular'), ('hipertension', 'Hipertensión arterial, HTA, presión alta'), ('cardiopatia_coronaria', 'Cardiopatía coronaria'), ('insuficiencia_cardiaca', 'Insuficiencia cardiaca'), ('valvulopatías_cardiacas', 'Valvulopatías cardiacas'), ('aneurismas', 'Aneurismas'), ('diabetes', 'Diabetes'), ('obesidad_sobrepeso', 'Obesidad, sobrepeso'), ('síndrome_metabólico', 'Síndrome metabólico'), ('EPOC_ICFA_enfermedad_pulmonar_obstructiva_crónica', ' EPOC, ICFA, enfermedad pulmonar obstructiva crónica'), ('tabaquismo', 'Tabaquismo'), ('alcoholismo', 'Alcoholismo'), ('adicción_a_droga_o_múltiples_drogas_de_abuso', 'Adición a droga o múltiples drogas de abuso'), ('enfermedad_renal_crónica_insuficiencia_renal_crónica', 'Enfermedad renal crónica, insuficiencia renal crónica'), ('hemodiálisis_peritoneo_diálisis', 'Hemodiálisis, peritoneo diálisis'), ('asma', 'Asma'), ('sida_VIH', 'Sida / VIH'), ('artritis_artrosis', 'Artritis / artrosis'), ('hernia_del_núcleo_pulposo_HNP_hernia_en_la_columna', 'Hernia del núcleo pulposo, HNP, hernia en la columna'), ('ulcera_gástrica_gastritis_crónica_gastritis_erosiva_helycobacter_pilory', 'ulcera gástrica, gastritis crónica, gastritis erosiva, helycobacter pilory'), ('hipotiroidismo', 'Hipotiroidismo'), ('Hipertiroidismo', 'Hipertiroidismo')], to='contacto_hospital.paciente'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='farmacos_patologias_cronicas',
            field=models.ManyToManyField(blank=True, choices=[('losartan', 'Losartán'), ('enalapril', 'Enalapril'), ('metformina', 'Metformina'), ('atorvastatina', 'Atorvastatina'), ('insulina', 'Insulina'), ('amlodipino', 'Amlodipino'), ('salbutamol', 'Salbutamol'), ('omeprazol', 'Omeprazol'), ('levotiroxina', 'Levotiroxina'), ('glibenclamida', 'Glibenclamida')], to='contacto_hospital.paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='alergias_farmacos',
            field=models.ManyToManyField(blank=True, choices=[('penicilina', 'Penicilina'), ('aine', 'Antiinflamatorios no esteroidales (AINEs)'), ('anestesicos', 'Anestésicos locales y generales'), ('medios_contraste', 'Medios de contraste radiológicos'), ('anticonvulsivantes', 'Anticonvulsivantes'), ('betalactamicos', 'Betalactámicos'), ('cefalosporinas', 'Cefalosporinas'), ('sulfas', 'Sulfas'), ('aspirina', 'Aspirina'), ('dipirona', 'Dipirona'), ('ninguna', 'NINGUNA'), ('otros', 'Otros (campo alfabético libre de 25 caracteres)')], to='contacto_hospital.paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cirugias_comunes',
            field=models.ManyToManyField(blank=True, choices=[('colecistectomia', 'Colecistectomía (extracción de vesícula)'), ('cirugias_bariatricas', 'Cirugías bariátricas'), ('herniorrafia', 'Herniorrafia (reparación de hernias)'), ('cirugia_toracica_oncologica', 'Cirugía Torácica Oncológica'), ('cirugia_deformidades_torax', 'Cirugía de las Deformidades del Tórax'), ('simpatectomia', 'Cirugía del Simpático o Simpatectomía'), ('tumores_mediastino', 'Tumores de Mediastino'), ('trasplante_pulmonar', 'Trasplante Pulmonar'), ('colecistectomia_vesicula', 'Colecistectomía (problemas de la vesícula)'), ('apendicectomia', 'Apendicectomía'), ('gastrectomia_cancer_gastrico', 'Gastrectomía por cáncer gástrico'), ('pancreatectomia_cancer', 'Pancreatectomía por cáncer de páncreas'), ('cirugia_cabeza_cuello_oncologica', 'Cirugía de Cabeza y Cuello Oncológica'), ('lifting_cuello', 'Lifting de Cuello (Cervicoplastía)'), ('cirugia_tiroides', 'Cirugía de Tiroides'), ('cirugia_parotida', 'Cirugía de Parótida'), ('cirugia_laringe', 'Cirugía de Laringe'), ('prostatectomia', 'Prostatectomía'), ('cirugia_calculos_renales', 'Cirugía de cálculos renales'), ('vasectomia', 'Vasectomía'), ('cirugia_cancer_vejiga', 'Cirugía para el cáncer de vejiga'), ('cirugia_reconstructiva_urogenital', 'Cirugía reconstructiva urogenital'), ('cesarea', 'Cesárea'), ('histerectomia', 'Histerectomía'), ('laparoscopia_ginecologica', 'Laparoscopía Ginecológica'), ('cirugia_prolapso_pelviano', 'Cirugía de Prolapso Pelviano'), ('cirugia_oncologica_ginecologica', 'Cirugía Oncológica Ginecológica'), ('cirugia_coronaria', 'Cirugía Coronaria'), ('cirugia_valvular', 'Cirugía Valvular'), ('cirugia_aorta_toracica', 'Cirugía de la Aorta Torácica'), ('cardiopatias_congenitas_adulto', 'Cardiopatías Congénitas del Adulto'), ('cirugia_arritmias', 'Cirugía de Arritmias'), ('tumores_cardiacos', 'Tumores Cardíacos'), ('trasplante_cardiaco', 'Trasplante Cardíaco y Corazón Artificial'), ('procedimientos_endovasculares', 'Procedimientos Endovasculares'), ('tratamiento_varices', 'Tratamiento de Várices'), ('patologia_aortica', 'Manejo de Patología Aórtica'), ('enfermedad_arterial_oclusiva', 'Enfermedad Arterial Oclusiva'), ('accesos_hemodialisis', 'Accesos Vasculares para Hemodiálisis'), ('prevencion_tromboembolica', 'Prevención y Tratamiento de la Enfermedad Tromboembólica'), ('cirugia_cancer_piel', 'Cirugía del cáncer de piel'), ('cirugia_lunares', 'Cirugía de Lunares (Nevos)'), ('cirugia_unas', 'Cirugía de uñas'), ('extirpacion_lesiones_benignas', 'Extirpación de lesiones cutáneas benignas'), ('inyeccion_queloides', 'Inyección intracutánea de queloides'), ('biopsias_piel', 'Biopsias de piel'), ('cirugia_catarata', 'Cirugía de Catarata'), ('cirugia_lasik', 'Cirugía Lasik'), ('vitrectomia', 'Vitrectomía'), ('pterigion', 'Pterigión'), ('glaucoma', 'Cirugías para tratar el Glaucoma'), ('chalazion', 'Chalazión (remoción de nódulos en el párpado)'), ('blefarochalasis', 'Blefarochalasis (corrección del exceso de piel en los párpados)'), ('crosslinking_queratocono', 'Crosslinking - Queratocono'), ('entropion', 'Entropión (corrección de párpados que se giran hacia adentro)'), ('fotocoagulacion_retina', 'Fotocoagulación de Retina'), ('implante_lente_alta_miopia', 'Implante de Lente Intraocular para Corrección de Alta Miopía')], to='contacto_hospital.paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cirugias_traumatologicas',
            field=models.ManyToManyField(blank=True, choices=[('artroscopia_rodilla', 'Artroscopia de rodilla'), ('artroscopia_hombro', 'Artroscopia de hombro'), ('protesis_total_rodilla', 'Prótesis total de rodilla'), ('protesis_total_cadera', 'Prótesis total de cadera'), ('reconstruccion_ligamento_cruzado', 'Reconstrucción del ligamento cruzado anterior'), ('cirugia_hallux_valgus', 'Cirugía del hallux valgus (juanete)'), ('reemplazo_articular_total_unicompartimental', 'Cirugía de Reemplazo Articular Total y Unicompartimental'), ('cirugia_asistida_robot', 'Cirugía asistida por Robot'), ('traumatologia_deportiva', 'Traumatología Deportiva'), ('trauma_complejo_rodilla', 'Trauma Complejo de Rodilla')], to='contacto_hospital.paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='enfermedades_comunes',
            field=models.ManyToManyField(blank=True, choices=[('Colon irritable', 'Colon irritable'), ('Cáncer', 'Cáncer, de cualquier zona del cuerpo y de cualquier tipo'), ('Depresión, ansiedad', 'Depresión, ansiedad'), ('Cefalea, dolor de cabeza', 'Cefalea, dolor de cabeza'), ('Quistes ováricos, patología ovárica', 'Quistes ováricos, patología ovárica'), ('Demencia', 'Demencia de cualquier tipo, ALZ, etc.'), ('Otras', 'Otras (campo alfabético libre de 25 caracteres).')], to='contacto_hospital.paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='farmacos_no_cronicos',
            field=models.ManyToManyField(blank=True, choices=[('paracetamol', 'Paracetamol'), ('ibuprofeno', 'Ibuprofeno'), ('ketorolaco', 'Ketorolaco'), ('clorfenamina', 'Clorfenamina'), ('diclofenaco', 'Diclofenaco'), ('loperamida', 'Loperamida'), ('famotidina', 'Famotidina'), ('naproxeno', 'Naproxeno'), ('acido_mefenamico', 'Ácido Mefenámico'), ('ciprofloxacina', 'Ciprofloxacina'), ('ninguna', 'NINGUNA'), ('otros', 'Otros (campo alfabético libre de 25 caracteres)')], to='contacto_hospital.paciente'),
        ),
    ]
