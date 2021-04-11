from django.contrib import admin

# Register your models here.
from student.models import Grade, Estudiantes, ResultadosModulo1, EntregaArchivos, Docentes

admin.site.register(Grade)
admin.site.register(Docentes)


@admin.register(EntregaArchivos)
class ArchivosModelAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'codigo_estudiante', 'formato_guia', 'nota', 'observaciones', 'rubrica',)
    search_fields = ('codigo_estudiante',)
    list_filter = ('codigo_estudiante',)


@admin.register(Estudiantes)
class EstudiantesModelAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'codigo_estudiante', 'correo', 'grado', 'edad')
    search_fields = ('nombres', 'apellidos', 'codigo_estudiante')
    list_filter = ('codigo_estudiante', 'grado')


@admin.register(ResultadosModulo1)
class ResultadosModelAdmin(admin.ModelAdmin):
    list_display = (
        'estudiante', 'codigo_estudiante', 'resultado_liderazgo', 'resultado_trabajo_equipo', 'resultado_resilencia',
        'resultado_inovacion',
        'resultado_creatividad', 'resultado_total')
    search_fields = ('codigo_estudiante',)
    list_filter = ('estudiante', 'resultado_total')
