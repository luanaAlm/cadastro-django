from django.urls import path
from .views import homeProfessores, listarProfessores, criarProfessor, professorNovo, updateProfessor, deleteProfessor, visualizarProfessor


# urls Professores
urlpatterns = [
    path('', homeProfessores, name='home_professores'),
    path('listar_professores', listarProfessores, name='listar_professores'),
    path('criar_professores', criarProfessor, name='criar_professores'),
    path('novo_professor', professorNovo, name='novo_professor'),
    path('visualizar_professor/(?P<ID_Professor>\d+)/$', visualizarProfessor,
         name='visualizar_professor'),
    path('^update_professor/(?P<ID_Professor>\d+)/$',
         updateProfessor, name='update_professor'),
    path('^delete_professor/(?P<ID_Professor>\d+)/$',
         deleteProfessor, name='delete_professor'),
]
