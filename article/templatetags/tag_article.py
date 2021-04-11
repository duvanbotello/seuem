from django import template

from article.models import Post
from student.models import ResultadosModulo1, EntregaArchivos, Convocatoria

register = template.Library()


@register.simple_tag()
def get_convocatoria():
    return Convocatoria.objects.last()


@register.simple_tag()
def get_entrega(estudiante):
    estudiante = EntregaArchivos.objects.filter(estudiante=estudiante).first()
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
        total = float(entregas_m2_linea.nota)
        if total >= 3:
            respuesta = True
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
            respuesta_resilencia = "F. Tienes una fortaleza. Tiene una capacidad de automotivación, tu confianza en ti mismo te hace sobreponerte a la adversidad haciendo de ti una persona más fuerte cada día. Eres realista y siempre esperar lo mejor."
        if resultado_resilencia >= 10 and resultado_resilencia <= 13:
            respuesta_resilencia = "R. Tienes una recomendación: Ves las situaciones adversas como una oportunidad, pero debes procurar ser más decisivo al momento de encontrar solución a esta, así que si consolidas tu perspectiva con iniciativa tendrás un nivel de resiliencia adecuado."
        if resultado_resilencia < 9:
            respuesta_resilencia = "D. Tienes una debilidad: Seguramente cuando estas en una adversidad o crisis no la soportas y las ves desde una perspectiva negativa, así mismo no te consideras apto para resistir y sobrellevar los obstáculos en situaciones de incertidumbre. Recuerda que puedes hacer de esta debilidad una oportunidad de mejora."

        if resultado_inovacion >= 14 and resultado_inovacion <= 20:
            respuesta_inovacion = "F. Tienes una fortaleza. Siempre quieres hacer de algo único y diferente a lo habitual, te esmeras en crear o mejorar cosas que se diferencien de las demás."
        if resultado_inovacion >= 10 and resultado_inovacion <= 13:
            respuesta_inovacion = "R.  Tienes una recomendación. Te esmeras en buscar algo nuevo y creativo, pero no eres persistente y paciente a la espera de resultados."
        if resultado_inovacion < 9:
            respuesta_inovacion = "D. Tienes una debilidad. No visualizas escenarios de cambio, ni te adaptas a ellos. Piensas que no tienes la imaginación para crear cosas nuevas.  Recuerda que puedes hacer de esta debilidad una oportunidad de mejora."

        if resultado_creatividad >= 14 and resultado_creatividad <= 20:
            respuesta_creatividad = "F. Tienes una fortaleza. Mantienes siempre una imaginación en toda situación o escenario, viendo en cada una de esas situaciones una oportunidad de mejora o de cambio."
        if resultado_creatividad >= 10 and resultado_creatividad <= 13:
            respuesta_creatividad = "R. Tienes una recomendación. Tienes buenas bases creativas, pero te falta impulso para llevarlas a cabo. No dejes que tus ideas no se hagan realidad"
        if resultado_creatividad < 9:
            respuesta_creatividad = "D. Tienes una debilidad. No te enfocas en crear oportunidades a cada situación o actividad en la que te encuentras, si no que te conformas con lo ya visto. Recuerda que puedes hacer de esta debilidad una oportunidad de mejora."

        if resultado_trabajo_equipo >= 14 and resultado_trabajo_equipo <= 20:
            respuesta_trabajo_equipo = ""
        if resultado_trabajo_equipo >= 10 and resultado_trabajo_equipo <= 13:
            respuesta_trabajo_equipo = ""
        if resultado_trabajo_equipo < 9:
            respuesta_trabajo_equipo = ""

        if resultado_trabajo_equipo >= 14 and resultado_trabajo_equipo <= 20:
            respuesta_trabajo_equipo = "F. Tienes una fortaleza. Eres flexible y adaptable en el trabajo, sabes escuchar a los demás y aceptar sus críticas, confías en el trabajo de los demás colaboras para que lo hagan mejor"
        if resultado_trabajo_equipo >= 10 and resultado_trabajo_equipo <= 13:
            respuesta_trabajo_equipo = "R. Tienes una recomendación. Te adaptas y aceptas trabajar con los demás, pero debes consideras que tu equipo de trabajo es vital para el cumplimiento de tus metas por ende debes dar lugar a las ideas y propuestas de los miembros de tu equipo."
        if resultado_trabajo_equipo < 9:
            respuesta_trabajo_equipo = "D. Tienes una debilidad. No te adaptas ni te esfuerzas en trabajar en equipo, no asimilas los cambios que tu equipo propone, y no aportas ideas de cambio o de mejora para tu equipo. Recuerda que puedes hacer de esta debilidad una oportunidad de mejora."

        if resultado_liderazgo >= 14 and resultado_liderazgo <= 20:
            respuesta_liderazgo = "F. Tienes una fortaleza, te sientes cómodo exponiendo tus ideas en conjunto, ejecutándolas y muestras aprecio por las contribuciones de los demás. ¡Eres líder!"
        if resultado_liderazgo >= 10 and resultado_liderazgo <= 13:
            respuesta_liderazgo = "R. Tienes una recomendación. No debes subestimar las fortalezas y habilidades de los demás. De lo contrario debes procurar obtener los mejor de ellos."
        if resultado_liderazgo < 9:
            respuesta_liderazgo = "D. Tienes una debilidad. Aun no tienes la capacidad para impulsar y llevar a cabo tareas o actividades con otras personas, crees que los demás no pueden ayudarte, y sientes que la prioridad en la idea de negocio eres tú. Recuerda que puedes hacer de esta debilidad una oportunidad de mejora."

        if total >= 90 and total <= 100:
            respuesta = "Tu nivel emprendedor es alto lo que te lleva a tener un perfil emprendedor excelente con rasgos que se asemejan al de un empresario, así que es momento de que empieces a construir tu iniciativa e idea de negocio que tengas en mente. Continua con tu proceso emprendedor y demuestra de lo que eres capaz…"
        if total >= 75 and total <= 89:
            respuesta = "Tu nivel emprendedor es sobresaliente, reúnes bastantes capacidades emprendedoras, aunque cuentes con un perfil emprendedor sobresaliente, puedes mejorar ciertas falencias que no te permiten estar nivel pleno al de un emprendedor mediante una serie de metas que te propongas. Esto te llevara a que tengas un perfil emprendedor excelente con rasgos que se asemejan al de un empresario, te recomendamos que antes de comenzar con tu iniciativa o idea de negocio mejores tu nivel con nuestras lecturas. Continua con tu proceso emprendedor y demuestra de lo que eres capaz…"
        if total >= 50 and total <= 84:
            respuesta = "tu nivel emprendedor es regular, es decir cuentas con las suficientescapacidades emprendedoras para iniciar tu proceso emprendedor, aun no tienes la confianza y la determinación que debe tener el perfil de un emprendedor, sin embargo, no debes preocuparte ya que puedes mejorar dichas capacidades a través de las ayudas suministradas, por lo que debes entonces prepararte y luego si iniciar con la puesta en marcha de la idea que tienes en mente, ¡prepárate tu proceso emprendedor te espera!"
        if total < 49:
            respuesta = "Aun no cuentas con un nivel emprendedor, así que, si tienes una idea de negocio en mente, te queda camino por recorrer para mejorar tus capacidades, aunque posees ciertos rasgos emprendedores, no es suficiente para iniciar con tu proceso emprendedor, puede ser que poseas inseguridades y dudas que te impiden. Por eso te recomendamos que trabajes a diario en los componentes que conforman el perfil emprendedor y te capacites con la unidad de emprendimiento. ¡prepárate tu proceso emprendedor te espera!"

    else:
        return None
    return {'respuesta_total': respuesta, 'puntos_totales': total, 'respuesta_liderazgo': respuesta_liderazgo,
            'respuesta_trabajo_equipo': respuesta_trabajo_equipo, 'respuesta_creatividad': respuesta_creatividad,
            'respuesta_inovacion': respuesta_inovacion, 'respuesta_resilencia': respuesta_resilencia, }
