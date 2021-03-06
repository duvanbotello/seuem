from datetime import datetime

from django import template

from article.models import Post
from student.models import ResultadosModulo1, EntregaArchivos, Convocatoria, EntregaArchivosModulo3, EntidadFinanciera

register = template.Library()


@register.simple_tag()
def get_convocatoria():
    convocatoria_reciente = Convocatoria.objects.last()
    fecha_cierre_final = datetime(convocatoria_reciente.fecha_cierre.year, convocatoria_reciente.fecha_cierre.month,
                                  convocatoria_reciente.fecha_cierre.day)
    fecha_apertura = datetime(convocatoria_reciente.fecha_apertura.year, convocatoria_reciente.fecha_apertura.month,
                              convocatoria_reciente.fecha_apertura.day)
    fecha_hoy = datetime.now()

    if fecha_hoy > fecha_cierre_final:
        return {'activa': False, 'fecha_apertura': convocatoria_reciente.fecha_apertura}

    if fecha_hoy < fecha_apertura:
        return {'activa': False, 'fecha_apertura': convocatoria_reciente.fecha_apertura}

    return True


@register.simple_tag()
def get_indicadores_nivel_emprededor():
    total_presentados = ResultadosModulo1.objects.all().count()
    total_aprobados = ResultadosModulo1.objects.filter(resultado_total__gte=75).count()
    nivel_emprendedor = (total_aprobados / total_presentados) * 100
    return nivel_emprendedor


@register.simple_tag()
def get_indicadores_ideas_negocio():
    total_presentados = EntregaArchivos.objects.all().count()
    total_aprobados = EntregaArchivos.objects.filter(nota__gte=3).count()
    ideas_negocio = (total_presentados / total_aprobados) * 100

    return ideas_negocio


@register.simple_tag()
def get_indicadores_plan_negocio():
    total_presentados = EntregaArchivosModulo3.objects.all().count()
    total_aprobados = EntregaArchivosModulo3.objects.filter(nota__gte=3).count()
    viabilidad = (total_aprobados / total_presentados) * 100

    return viabilidad


@register.simple_tag()
def get_indicadores_m1():
    total_presentados = ResultadosModulo1.objects.all().count()
    total_aprobados = ResultadosModulo1.objects.filter(resultado_total__gte=75).count()
    total_reprobados = ResultadosModulo1.objects.filter(resultado_total__lte=74.99).count()

    return {'total_presentados': total_presentados, 'total_aprobados': total_aprobados,
            'total_reprobados': total_reprobados}


@register.simple_tag()
def get_indicadores_m2():
    total_presentados = EntregaArchivos.objects.all().count()
    total_aprobados = EntregaArchivos.objects.filter(nota__gte=3).count()
    total_reprobados = EntregaArchivos.objects.filter(nota__lte=2.99).count()

    return {'total_presentados': total_presentados, 'total_aprobados': total_aprobados,
            'total_reprobados': total_reprobados}


@register.simple_tag()
def get_indicadores_m3():
    total_presentados = EntregaArchivosModulo3.objects.all().count()
    total_aprobados = EntregaArchivosModulo3.objects.filter(nota__gte=3).count()
    total_reprobados = EntregaArchivosModulo3.objects.filter(nota__lte=2.99).count()

    return {'total_presentados': total_presentados, 'total_aprobados': total_aprobados,
            'total_reprobados': total_reprobados}


@register.simple_tag()
def get_entrega(estudiante):
    estudiante = EntregaArchivos.objects.filter(estudiante=estudiante).first()
    if estudiante:
        return estudiante.formato_guia.url
    return None


@register.simple_tag()
def get_entidades():
    estudiante = EntidadFinanciera.objects.all()
    if estudiante:
        return estudiante
    return None


@register.simple_tag()
def get_entrega_m3(estudiante):
    estudiante = EntregaArchivosModulo3.objects.filter(codigo_estudiante=estudiante.codigo_estudiante).first()
    if estudiante:
        return estudiante.formato_guia.url
    return None


@register.simple_tag()
def get_entrega_all(estudiante):
    estudiante = EntregaArchivos.objects.filter(estudiante=estudiante).first()
    if estudiante:
        return estudiante
    return None


@register.simple_tag()
def get_entrega_all_3(estudiante):
    estudiante = EntregaArchivosModulo3.objects.filter(estudiante=estudiante).first()
    if estudiante:
        return estudiante
    return None


@register.simple_tag()
def get_post(id_post):
    post = Post.objects.filter(id=id_post).first()
    return post.content


@register.simple_tag()
def resultados_linea(codigo_estudiante):
    resultados_Estudiante = ResultadosModulo1.objects.filter(codigo_estudiante=codigo_estudiante).last()
    if resultados_Estudiante:
        total = int(resultados_Estudiante.resultado_total)
        if total >= 75:
            respuesta = True
        else:
            respuesta = False
    else:
        respuesta = False

    return respuesta


@register.simple_tag()
def entregas_m2_linea(codigo_estudiante):
    entregas_m2_linea = EntregaArchivos.objects.filter(codigo_estudiante=codigo_estudiante).last()
    if entregas_m2_linea:
        if entregas_m2_linea.nota:
            total = float(entregas_m2_linea.nota)
            if total >= 4:
                respuesta = True
            else:
                respuesta = False
        else:
            respuesta = False
    else:
        respuesta = False

    return respuesta


@register.simple_tag()
def entregas_m3_linea(codigo_estudiante):
    entregas_m2_linea = EntregaArchivosModulo3.objects.filter(codigo_estudiante=codigo_estudiante).last()
    if entregas_m2_linea:
        if entregas_m2_linea.nota:
            total = float(entregas_m2_linea.nota)
            if total >= 4:
                respuesta = True
            else:
                respuesta = False
        else:
            respuesta = False
    else:
        respuesta = False

    return respuesta


@register.simple_tag()
def resultados(codigo_estudiante):
    respuesta = ''
    resultados_Estudiante = ResultadosModulo1.objects.filter(codigo_estudiante=codigo_estudiante).last()
    if resultados_Estudiante:
        total = int(resultados_Estudiante.resultado_total)
        resultado_liderazgo = int(resultados_Estudiante.resultado_liderazgo)
        resultado_trabajo_equipo = int(resultados_Estudiante.resultado_trabajo_equipo)
        resultado_resilencia = int(resultados_Estudiante.resultado_resilencia)
        resultado_inovacion = int(resultados_Estudiante.resultado_inovacion)
        resultado_creatividad = int(resultados_Estudiante.resultado_creatividad)

        if resultado_resilencia >= 14 and resultado_resilencia <= 20:
            respuesta_resilencia = "F. Tienes una fortaleza. Tiene una capacidad de automotivaci??n, tu confianza en ti mismo te hace sobreponerte a la adversidad haciendo de ti una persona m??s fuerte cada d??a. Eres realista y siempre esperar lo mejor."
        if resultado_resilencia >= 10 and resultado_resilencia <= 13:
            respuesta_resilencia = "R. Tienes una recomendaci??n: Ves las situaciones adversas como una oportunidad, pero debes procurar ser m??s decisivo al momento de encontrar soluci??n a esta, as?? que si consolidas tu perspectiva con iniciativa tendr??s un nivel de resiliencia adecuado."
        if resultado_resilencia < 9:
            respuesta_resilencia = "D. Tienes una debilidad: Seguramente cuando estas en una adversidad o crisis no la soportas y las ves desde una perspectiva negativa, as?? mismo no te consideras apto para resistir y sobrellevar los obst??culos en situaciones de incertidumbre. Recuerda que puedes hacer de esta debilidad una oportunidad de mejora."

        if resultado_inovacion >= 14 and resultado_inovacion <= 20:
            respuesta_inovacion = "F. Tienes una fortaleza. Siempre quieres hacer de algo ??nico y diferente a lo habitual, te esmeras en crear o mejorar cosas que se diferencien de las dem??s."
        if resultado_inovacion >= 10 and resultado_inovacion <= 13:
            respuesta_inovacion = "R.  Tienes una recomendaci??n. Te esmeras en buscar algo nuevo y creativo, pero no eres persistente y paciente a la espera de resultados."
        if resultado_inovacion < 9:
            respuesta_inovacion = "D. Tienes una debilidad. No visualizas escenarios de cambio, ni te adaptas a ellos. Piensas que no tienes la imaginaci??n para crear cosas nuevas.  Recuerda que puedes hacer de esta debilidad una oportunidad de mejora."

        if resultado_creatividad >= 14 and resultado_creatividad <= 20:
            respuesta_creatividad = "F. Tienes una fortaleza. Mantienes siempre una imaginaci??n en toda situaci??n o escenario, viendo en cada una de esas situaciones una oportunidad de mejora o de cambio."
        if resultado_creatividad >= 10 and resultado_creatividad <= 13:
            respuesta_creatividad = "R. Tienes una recomendaci??n. Tienes buenas bases creativas, pero te falta impulso para llevarlas a cabo. No dejes que tus ideas no se hagan realidad"
        if resultado_creatividad < 9:
            respuesta_creatividad = "D. Tienes una debilidad. No te enfocas en crear oportunidades a cada situaci??n o actividad en la que te encuentras, si no que te conformas con lo ya visto. Recuerda que puedes hacer de esta debilidad una oportunidad de mejora."

        if resultado_trabajo_equipo >= 14 and resultado_trabajo_equipo <= 20:
            respuesta_trabajo_equipo = ""
        if resultado_trabajo_equipo >= 10 and resultado_trabajo_equipo <= 13:
            respuesta_trabajo_equipo = ""
        if resultado_trabajo_equipo < 9:
            respuesta_trabajo_equipo = ""

        if resultado_trabajo_equipo >= 14 and resultado_trabajo_equipo <= 20:
            respuesta_trabajo_equipo = "F. Tienes una fortaleza. Eres flexible y adaptable en el trabajo, sabes escuchar a los dem??s y aceptar sus cr??ticas, conf??as en el trabajo de los dem??s colaboras para que lo hagan mejor"
        if resultado_trabajo_equipo >= 10 and resultado_trabajo_equipo <= 13:
            respuesta_trabajo_equipo = "R. Tienes una recomendaci??n. Te adaptas y aceptas trabajar con los dem??s, pero debes consideras que tu equipo de trabajo es vital para el cumplimiento de tus metas por ende debes dar lugar a las ideas y propuestas de los miembros de tu equipo."
        if resultado_trabajo_equipo < 9:
            respuesta_trabajo_equipo = "D. Tienes una debilidad. No te adaptas ni te esfuerzas en trabajar en equipo, no asimilas los cambios que tu equipo propone, y no aportas ideas de cambio o de mejora para tu equipo. Recuerda que puedes hacer de esta debilidad una oportunidad de mejora."

        if resultado_liderazgo >= 14 and resultado_liderazgo <= 20:
            respuesta_liderazgo = "F. Tienes una fortaleza, te sientes c??modo exponiendo tus ideas en conjunto, ejecut??ndolas y muestras aprecio por las contribuciones de los dem??s. ??Eres l??der!"
        if resultado_liderazgo >= 10 and resultado_liderazgo <= 13:
            respuesta_liderazgo = "R. Tienes una recomendaci??n. No debes subestimar las fortalezas y habilidades de los dem??s. De lo contrario debes procurar obtener los mejor de ellos."
        if resultado_liderazgo < 9:
            respuesta_liderazgo = "D. Tienes una debilidad. Aun no tienes la capacidad para impulsar y llevar a cabo tareas o actividades con otras personas, crees que los dem??s no pueden ayudarte, y sientes que la prioridad en la idea de negocio eres t??. Recuerda que puedes hacer de esta debilidad una oportunidad de mejora."

        if total >= 90 and total <= 100:
            respuesta = "Tu nivel emprendedor es alto lo que te lleva a tener un perfil emprendedor excelente con rasgos que se asemejan al de un empresario, as?? que es momento de que empieces a construir tu iniciativa e idea de negocio que tengas en mente. Continua con tu proceso emprendedor y demuestra de lo que eres capaz???"
        if total >= 75 and total <= 89:
            respuesta = "Tu nivel emprendedor es sobresaliente, re??nes bastantes capacidades emprendedoras, aunque cuentes con un perfil emprendedor sobresaliente, puedes mejorar ciertas falencias que no te permiten estar nivel pleno al de un emprendedor mediante una serie de metas que te propongas. Esto te llevara a que tengas un perfil emprendedor excelente con rasgos que se asemejan al de un empresario, te recomendamos que antes de comenzar con tu iniciativa o idea de negocio mejores tu nivel con nuestras lecturas. Continua con tu proceso emprendedor y demuestra de lo que eres capaz???"
        if total >= 50 and total <= 84:
            respuesta = "tu nivel emprendedor es regular, es decir cuentas con las suficientescapacidades emprendedoras para iniciar tu proceso emprendedor, aun no tienes la confianza y la determinaci??n que debe tener el perfil de un emprendedor, sin embargo, no debes preocuparte ya que puedes mejorar dichas capacidades a trav??s de las ayudas suministradas, por lo que debes entonces prepararte y luego si iniciar con la puesta en marcha de la idea que tienes en mente, ??prep??rate tu proceso emprendedor te espera!"
        if total < 49:
            respuesta = "Aun no cuentas con un nivel emprendedor, as?? que, si tienes una idea de negocio en mente, te queda camino por recorrer para mejorar tus capacidades, aunque posees ciertos rasgos emprendedores, no es suficiente para iniciar con tu proceso emprendedor, puede ser que poseas inseguridades y dudas que te impiden. Por eso te recomendamos que trabajes a diario en los componentes que conforman el perfil emprendedor y te capacites con la unidad de emprendimiento. ??prep??rate tu proceso emprendedor te espera!"

    else:
        return None
    return {'respuesta_total': respuesta, 'puntos_totales': total, 'respuesta_liderazgo': respuesta_liderazgo,
            'respuesta_trabajo_equipo': respuesta_trabajo_equipo, 'respuesta_creatividad': respuesta_creatividad,
            'respuesta_inovacion': respuesta_inovacion, 'respuesta_resilencia': respuesta_resilencia, }
