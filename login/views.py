from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import CreateView

from login.forms import FormularioRegistrar
from student.models import Estudiantes


class LoginView(View):
    template_name = 'login/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RegisterStudentView(CreateView):
    model = Estudiantes
    form_class = FormularioRegistrar
    template_name = 'login/sign-up.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_estudiante = Estudiantes(
                nombres=form.cleaned_data.get('nombres'),
                apellidos=form.cleaned_data.get('apellidos'),
                codigo_estudiante=form.cleaned_data.get('codigo_estudiante'),
                grado=form.cleaned_data.get('grado'),
                edad=form.cleaned_data.get('edad'),
                nombre_acudiente=form.cleaned_data.get('nombre_acudiente'),
                telefono_contacto=form.cleaned_data.get('telefono_contacto'),
                correo=form.cleaned_data.get('correo')
            )
            nuevo_estudiante.password = make_password('password2')
            nuevo_estudiante.save()
            return redirect('login:login_student')
        else:
            return render(request, self.template_name, {'form': form})
