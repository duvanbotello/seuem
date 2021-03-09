from django.contrib import admin

# Register your models here.
from student.models import Grade, Estudiantes, ResultadosModulo1

admin.site.register(Grade)


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
