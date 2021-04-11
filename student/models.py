from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Grade(models.Model):
    nombre_grado = models.CharField(max_length=200, null=True, blank=False, verbose_name='Nombres')

    def __str__(self):
        return self.nombre_grado

    class Meta:
        verbose_name = 'Grado'
        verbose_name_plural = 'Grados'


class Docentes(models.Model):
    nombres = models.CharField(max_length=100, null=True, blank=False, verbose_name=('Nombres'))
    apellidos = models.CharField(max_length=100, null=True, blank=False, verbose_name=('Apellidos'))
    documento = models.CharField(max_length=100, unique=True, null=True, blank=False,
                                 verbose_name=('Documento identidad'))
    edad = models.CharField(max_length=10, null=True, blank=False, verbose_name=('Edad'))
    titulo = models.CharField(max_length=100, null=True, blank=False, verbose_name=('Titulo academico'))
    telefono_contacto = models.CharField(max_length=100, null=True, blank=False, verbose_name=('Contacto'))
    correo = models.EmailField(verbose_name=('Correo Electronico'))

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'


class Estudiantes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombres = models.CharField(max_length=100, null=True, blank=False, verbose_name=('Nombres'))
    apellidos = models.CharField(max_length=100, null=True, blank=False, verbose_name=('Apellidos'))
    codigo_estudiante = models.CharField(max_length=100, unique=True, null=True, blank=False,
                                         verbose_name=('Codigo Estudiantil'))
    grado = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name='Asigne un grado',
                              related_name='Grado', help_text='Seleccione un grado y asignelo')
    edad = models.CharField(max_length=10, null=True, blank=False, verbose_name=('Edad'))
    nombre_acudiente = models.CharField(max_length=100, null=True, blank=False, verbose_name=('Nombre del acudiente'))
    telefono_contacto = models.CharField(max_length=100, null=True, blank=False, verbose_name=('Contacto'))
    correo = models.EmailField(verbose_name=('Correo Electronico'))
    docente = models.OneToOneField(Docentes, on_delete=models.SET_NULL, null=True, blank=True, default=None,
                                   verbose_name='Asigne un docente',
                                   related_name='Docente', help_text='Seleccione un docente y asignelo')

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'


class ResultadosModulo1(models.Model):
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
    codigo_estudiante = models.CharField(max_length=100, null=True, blank=False,
                                         verbose_name=('Codigo Estudiantil'))
    resultado_liderazgo = models.CharField(max_length=10, null=True, blank=False, verbose_name=('Resultado liderazgo'))
    resultado_trabajo_equipo = models.CharField(max_length=10, null=True, blank=False,
                                                verbose_name=('Resultado trabajo en equipo'))
    resultado_resilencia = models.CharField(max_length=10, null=True, blank=False,
                                            verbose_name=('Resultado resilencia'))
    resultado_inovacion = models.CharField(max_length=10, null=True, blank=False, verbose_name=('Resultado inovacion'))
    resultado_creatividad = models.CharField(max_length=10, null=True, blank=False,
                                             verbose_name=('Resultado creatividad'))
    resultado_total = models.CharField(max_length=10, null=True, blank=False, verbose_name=('Resultado Total'))

    def __str__(self):
        return self.estudiante.nombres + ' ' + self.estudiante.apellidos

    class Meta:
        verbose_name = 'Resultado'
        verbose_name_plural = 'Resultados'


class EntregaArchivos(models.Model):
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
    codigo_estudiante = models.CharField(max_length=100, null=True, blank=False,
                                         verbose_name=('Codigo Estudiantil'), unique=True)
    formato_guia = models.FileField(upload_to="archivos/", null=True, blank=True,
                                    verbose_name=('Plantilla Guia'))
    nota = models.CharField(max_length=10, null=True, blank=False, verbose_name=('Ingrese Nota'))
    observaciones = models.TextField(null=True, blank=False, verbose_name=('Ingrese Observaciones'))
    rubrica = models.FileField(upload_to="archivos/", null=True, blank=True,
                                    verbose_name=('Rebrica de calificacion'))

    def __str__(self):
        return self.estudiante.nombres + ' ' + self.estudiante.apellidos

    class Meta:
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'
