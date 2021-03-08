from django.urls import path

from login.views import LoginView, RegisterStudentView, DashboardView, login_user, desconectar

app_name = 'login'
urlpatterns = [
    path('', LoginView.as_view(), name='login_student'),
    path('registrar', RegisterStudentView.as_view(), name='register_student'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('login-session/', login_user, name='login_session'),
    path('desconectar', desconectar, name='desconectar'),
]
