from django.urls import path

from student.views import TestView, ResultadosView

app_name = 'student'
urlpatterns = [
    path('test', TestView.as_view(), name='test_emprendedor'),
    path('resultados', ResultadosView.as_view(), name='resultados'),
]
