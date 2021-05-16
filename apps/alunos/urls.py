from django.urls import path
from .views import listarAlunos, criarAluno, alunoNovo, updateAluno, deleteAluno, consulta, visualizarAluno


# urls Alunos
urlpatterns = [
    path('listar_alunos', listarAlunos, name='listar_alunos'),
    path('criar_alunos', criarAluno, name='criar_alunos'),
    path('novo_aluno', alunoNovo, name='novo_aluno'),
    path('update_aluno/<int:ID_Aluno>/', updateAluno, name='update_aluno'),
    path('delete_aluno/<int:ID_Aluno>/', deleteAluno, name='delete_aluno'),
    path('visualizar_aluno/<int:ID_Aluno>/',
         visualizarAluno, name='visualizar_aluno'),
    path('consulta/', consulta),
]
