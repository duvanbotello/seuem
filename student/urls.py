from django.urls import path

from student.views import TestView, ResultadosView, TallerM2View, PlantillaM2View, ResultadosM2View

app_name = 'student'
urlpatterns = [
    path('test', TestView.as_view(), name='test_emprendedor'),
    path('resultados', ResultadosView.as_view(), name='resultados'),
    path('tallerm2', TallerM2View.as_view(), name='taller_m2'),
    path('platillam2', PlantillaM2View.as_view(), name='plantilla_2'),
    path('resultadosm2', ResultadosM2View.as_view(), name='resultadosm2'),
]
