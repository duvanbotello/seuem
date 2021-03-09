from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from login.forms import FormularioRegistrar
from student.models import Estudiantes


@login_required(login_url=reverse_lazy('login:login_student'), redirect_field_name=None)
def login_user(request):
    return redirect(reverse_lazy('login:dashboard'))


def desconectar(request):
    logout(request)
    return redirect('/')


class LoginView(View):
    template_name = 'login/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('login:dashboard'))
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        codigo_estudiante = request.POST['codigo_estudiante']
        password = request.POST['password']
        if codigo_estudiante:
            if password:
                user = authenticate(username=codigo_estudiante, password=password)
                if user is not None:
                    login(request, user)
                else:
                    return render(request, self.template_name,
                                  {'message': 'Codigo de Estudiante o contraseña invalida'})
            else:
                return render(request, self.template_name,
                              {'message': 'Ingrese Contraseña'})
        else:
            return render(request, self.template_name,
                          {'message': 'Ingrese codigo del estudiante'})
        return redirect(reverse_lazy('login:login_session'))


class DashboardView(LoginRequiredMixin, View):
    template_name = 'login/dashboard.html'
    login_url = reverse_lazy('login:login_student')
    redirect_field_name = None

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RegisterStudentView(CreateView):
    model = Estudiantes
    form_class = FormularioRegistrar
    template_name = 'login/sign-up.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data.get('codigo_estudiante'),
                form.cleaned_data.get('correo'),
                form.cleaned_data.get('password1'))

            nuevo_estudiante = Estudiantes(
                user=user,
                nombres=form.cleaned_data.get('nombres'),
                apellidos=form.cleaned_data.get('apellidos'),
                codigo_estudiante=form.cleaned_data.get('codigo_estudiante'),
                grado=form.cleaned_data.get('grado'),
                edad=form.cleaned_data.get('edad'),
                nombre_acudiente=form.cleaned_data.get('nombre_acudiente'),
                telefono_contacto=form.cleaned_data.get('telefono_contacto'),
                correo=form.cleaned_data.get('correo')
            )

            # password1 = form.cleaned_data.get('password1')
            # nuevo_estudiante.password = make_password(password1)
            nuevo_estudiante.save()
            return redirect('login:login_student')
        else:
            return render(request, self.template_name, {'form': form})
