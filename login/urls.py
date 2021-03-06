from django.urls import path

from login.views import LoginView, RegisterStudentView

app_name = 'login'
urlpatterns = [
    path('', LoginView.as_view(), name='login_student'),
    path('/registrar', RegisterStudentView.as_view(), name='register_student'),
]
