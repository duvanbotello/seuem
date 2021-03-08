from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View


class TestView(LoginRequiredMixin, View):
    template_name = 'student/test.html'
    login_url = reverse_lazy('login:login_student')
    redirect_field_name = None

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ResultadosView(LoginRequiredMixin, View):
    template_name = 'student/resultados.html'
    login_url = reverse_lazy('login:login_student')
    redirect_field_name = None

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
