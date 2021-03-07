from django.contrib import admin

# Register your models here.
from student.models import Grade, Estudiantes

admin.site.register(Grade)


@admin.register(Estudiantes)
class EstudiantesModelAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'codigo_estudiante', 'correo', 'grado', 'edad')
    search_fields = ('nombres','apellidos', 'codigo_estudiante')
    list_filter = ('codigo_estudiante', 'grado')