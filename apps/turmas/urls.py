from django.urls import path
from .views import homeTurmas, listarTurmas, pdfDiarioClasse


# urls Turmas
urlpatterns = [
    path('home_turmas', homeTurmas, name='home_turmas'),

    path('listar_turmas/(?P<turma_id>\d+)/$',
         listarTurmas, name='listar_turmas'),
    path('pdf_diario_classe/(?P<turma_id>\d+)/$',
         pdfDiarioClasse, name='pdf_diario_classe'),
]
