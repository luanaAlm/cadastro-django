from django.urls import path
from .views import listarAlunos, criarAluno, alunoNovo, updateAluno, deleteAluno,consulta


#urls Alunos
urlpatterns = [
    path('listar_alunos',listarAlunos, name='listar_alunos'),
    path('criar_alunos',criarAluno, name='criar_alunos'),
    path('novo_aluno',alunoNovo, name='novo_aluno'),
    path('^update_aluno/(?P<ID_Aluno>\d+)/$', updateAluno, name='update_aluno'),
    path('^delete_aluno/(?P<ID_Aluno>\d+)/$', deleteAluno, name='delete_aluno'),
    path('consulta/', consulta, name='consulta'),
]

