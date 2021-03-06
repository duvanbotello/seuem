from django.db import models


# Create your models here.
class Grade(models.Model):
    nombre_grado = models.CharField(max_length=200, null=True, blank=False, verbose_name='Nombres')

    def __str__(self):
        return self.nombre_grado

    class Meta:
        verbose_name = 'Grado'
        verbose_name_plural = 'Grados'
