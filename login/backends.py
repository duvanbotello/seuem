from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from student.models import Estudiantes


class SettingsBackend(BaseBackend):
    def authenticate(self, request, codigo_estudiante=None, password=None):
        estudiante = Estudiantes.objects.filter(codigo_estudiante=codigo_estudiante).first()
        print(estudiante.codigo_estudiante)
        if estudiante:
            login_valid = (estudiante.codigo_estudiante == codigo_estudiante)
            pwd_valid = check_password(password, estudiante.password)
            if login_valid and pwd_valid:
                estudiante = Estudiantes.objects.get(codigo_estudiante=codigo_estudiante)
                return estudiante
        return None

    def get_estudiante(self, estudiante_id):
        try:
            return Estudiantes.objects.get(pk=estudiante_id)
        except User.DoesNotExist:
            return None
