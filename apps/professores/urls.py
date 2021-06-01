from django.urls import path
from .views import listarProfessores, criarProfessor, professorNovo, updateProfessor, deleteProfessor, visualizarProfessor, professoresEXL, pdfProfessor


# urls Professores
urlpatterns = [
    path('listar_professores', listarProfessores, name='listar_professores'),
    path('criar_professores', criarProfessor, name='criar_professores'),
    path('novo_professor', professorNovo, name='novo_professor'),
    path('visualizar_professor/(?P<ID_Professor>\d+)/$', visualizarProfessor,
         name='visualizar_professor'),
    path('^update_professor/(?P<ID_Professor>\d+)/$',
         updateProfessor, name='update_professor'),
    path('^delete_professor/(?P<ID_Professor>\d+)/$',
         deleteProfessor, name='delete_professor'),
    # excel
    path('professores_exportar_exl', professoresEXL.as_view(),
         name='professores_exportar_exl'),
    # pdf
    path('pdf_professor/(?P<ID_Professor>\d+)/$',
         pdfProfessor, name='pdf_professor'),


]
