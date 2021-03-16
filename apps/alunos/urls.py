from django.urls import path
from .views import homeAlunos, listarAlunos, criarAluno, alunoNovo


#urls Alunos
urlpatterns = [
    path('',homeAlunos),
    path('listar_alunos',listarAlunos, name='listar_alunos'),
    path('criar_alunos',criarAluno, name='criar_alunos'),
    path('novo_aluno',alunoNovo, name='novo_aluno'),
]

