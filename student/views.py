from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from student.models import ResultadosModulo1


class TestView(LoginRequiredMixin, View):
    template_name = 'student/test.html'
    login_url = reverse_lazy('login:login_student')
    redirect_field_name = None

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        total_liderazgo = int(request.POST['p1']) + int(request.POST['p2']) + int(request.POST['p3']) + int(
            request.POST['p4']) + int(request.POST['p5'])
        total_creatividad = int(request.POST['p6']) + int(request.POST['p7']) + int(request.POST['p8']) + int(
            request.POST['p9']) + int(request.POST['p10'])
        total_inovacion = int(request.POST['p11']) + int(request.POST['p12']) + int(request.POST['p13']) + int(
            request.POST['p14']) + int(request.POST['p15'])
        total_equipo = int(request.POST['p16']) + int(request.POST['p17']) + int(request.POST['p18']) + int(
            request.POST['p19']) + int(request.POST['p20'])
        total_resilencia = int(request.POST['p21']) + int(request.POST['p22']) + int(request.POST['p23']) + int(
            request.POST['p24']) + int(request.POST['p25'])
        total_test = total_equipo + total_creatividad + total_liderazgo + total_inovacion + total_resilencia

        resultado = ResultadosModulo1(
            estudiante=request.user.estudiantes,
            codigo_estudiante=request.user.estudiantes.codigo_estudiante,
            resultado_liderazgo=total_liderazgo,
            resultado_trabajo_equipo=total_equipo,
            resultado_resilencia=total_resilencia,
            resultado_inovacion=total_inovacion,
            resultado_creatividad=total_creatividad,
            resultado_total=total_test
        )
        resultado.save()

        return redirect(reverse_lazy('student:resultados'))


class ResultadosView(LoginRequiredMixin, View):
    template_name = 'student/resultados.html'
    login_url = reverse_lazy('login:login_student')
    redirect_field_name = None

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class TallerM2View(LoginRequiredMixin, View):
    template_name = 'student/taller_m2.html'
    login_url = reverse_lazy('login:login_student')
    redirect_field_name = None

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class PlantillaM2View(LoginRequiredMixin, View):
    template_name = 'student/plantilla_m2.html'
    login_url = reverse_lazy('login:login_student')
    redirect_field_name = None

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ResultadosM2View(LoginRequiredMixin, View):
    template_name = 'student/resultados_m2.html'
    login_url = reverse_lazy('login:login_student')
    redirect_field_name = None

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
