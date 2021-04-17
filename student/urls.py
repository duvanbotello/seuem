from django.urls import path

from student.views import TestView, ResultadosView, TallerM2View, PlantillaM2View, ResultadosM2View, CapacitacionView, \
    PlantillaM3View, GuiaM3View, ResultadosM3View, Modulo4View

app_name = 'student'
urlpatterns = [
    path('test', TestView.as_view(), name='test_emprendedor'),
    path('resultados', ResultadosView.as_view(), name='resultados'),
    path('tallerm2', TallerM2View.as_view(), name='taller_m2'),
    path('platillam2', PlantillaM2View.as_view(), name='plantilla_2'),
    path('resultadosm2', ResultadosM2View.as_view(), name='resultadosm2'),
    path('capacitacionm1', CapacitacionView.as_view(), name='capacitacionm1'),
    path('guia-modulo-3', GuiaM3View.as_view(), name='guia_modulo_3'),
    path('plantilla-modulo-3', PlantillaM3View.as_view(), name='plantilla_3'),
    path('resultados-modulo-3', ResultadosM3View.as_view(), name='resultados_m3'),
    path('entidades-financieras', Modulo4View.as_view(), name='entidades-financieras'),
]
