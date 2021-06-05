from django.contrib import admin

# Register your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe

from student.models import Grade, Estudiantes, ResultadosModulo1, EntregaArchivos, Docentes, Convocatoria, \
    EntregaArchivosModulo3, EntidadFinanciera


@admin.register(Convocatoria)
class ConvocatoriaModelAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_convocatoria', 'fecha_apertura', 'fecha_cierre')


@admin.register(Docentes)
class DocentesModelAdmin(admin.ModelAdmin):
    list_display = (
        'nombres', 'apellidos', 'documento', 'edad', 'titulo',
        'area_desempeno',
        'entidad', 'telefono_contacto')
    search_fields = ('nombres', 'apellidos', 'edad')
    list_filter = ('documento', 'edad')


@admin.register(ResultadosModulo1)
class ResultadosModelAdmin(admin.ModelAdmin):
    list_display = (
        'estudiante', 'codigo_estudiante', 'resultado_liderazgo', 'resultado_trabajo_equipo', 'resultado_resilencia',
        'resultado_inovacion',
        'resultado_creatividad', 'resultado_total')
    search_fields = ('codigo_estudiante',)
    list_filter = ('estudiante', 'resultado_total')


@admin.register(EntidadFinanciera)
class ArchivosModelAdmin(admin.ModelAdmin):
    list_display = ('nombre_entidad', 'informacion', 'url', 'direccion', 'correo_electronico',)
    search_fields = ('nombre_entidad',)
    list_filter = ('nombre_entidad',)


@admin.register(EntregaArchivos)
class ArchivosModelAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'codigo_estudiante', 'formato_guia', 'nota', 'observaciones', 'rubrica',)
    search_fields = ('codigo_estudiante',)
    list_filter = ('codigo_estudiante',)


@admin.register(EntregaArchivosModulo3)
class EntregaArchivosM3(admin.ModelAdmin):
    list_display = ('estudiante', 'codigo_estudiante', 'formato_guia', 'nota', 'observaciones', 'rubrica',)
    search_fields = ('codigo_estudiante',)
    list_filter = ('codigo_estudiante',)


@admin.register(Estudiantes)
class EstudiantesModelAdmin(admin.ModelAdmin):
    list_display = (
        'nombres', 'apellidos', 'codigo_estudiante', 'correo', 'grado', 'edad', 'docente', 'idea_negocio',
        'proceso_link')
    search_fields = ('nombres', 'apellidos', 'codigo_estudiante')
    list_filter = ('codigo_estudiante', 'grado')

    readonly_fields = ('proceso_link',)

    def proceso_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("student:ver_proceso", args=(obj.user.estudiantes.codigo_estudiante,)),
            'Ver proceso'
        ))

    proceso_link.short_description = 'Proceso'


admin.site.register(Grade)
