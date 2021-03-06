from django.shortcuts import render

# Create your views here.
from django.views import View

from student.models import Grade


class LoginView(View):
    template_name = 'login/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RegisterStudentView(View):
    template_name = 'login/sign-up.html'

    def get(self, request, *args, **kwargs):
        grados = Grade.objects.all()
        return render(request, self.template_name, {'grados': grados})
