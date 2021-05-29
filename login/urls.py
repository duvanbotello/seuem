from django.urls import path, reverse_lazy

from django.contrib.auth import views as auth_views

from login.views import LoginView, RegisterStudentView, DashboardView, login_user, desconectar, HomeView

app_name = 'login'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login_student'),
    path('registrar', RegisterStudentView.as_view(), name='register_student'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('login-session/', login_user, name='login_session'),
    path('desconectar', desconectar, name='desconectar'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html",
                                                                 email_template_name='password_reset_email.html',
                                                                 success_url=reverse_lazy(
                                                                     'login:password_reset_done')),
         name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html",
                                                     success_url=reverse_lazy(
                                                         'login:password_reset_complete')),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name='password_reset_complete')
]
