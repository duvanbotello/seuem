from django.urls import path

from login.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='login_student'),
    path('/registrar', LoginView.as_view(), name='register_student'),
]
