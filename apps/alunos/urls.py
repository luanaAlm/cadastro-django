from django.urls import path
from .views import listarAlunos, criarAluno, alunoNovo, updateAluno, deleteAluno,consulta, render_pdf_view, render_pdf_view_id_aluno, visualizarAluno


#urls Alunos
urlpatterns = [
    path('listar_alunos',listarAlunos, name='listar_alunos'),
    path('criar_alunos',criarAluno, name='criar_alunos'),
    path('novo_aluno',alunoNovo, name='novo_aluno'),
    path('update_aluno/(?P<ID_Aluno>\d+)/$', updateAluno, name='update_aluno'),
    path('delete_aluno/(?P<ID_Aluno>\d+)/$', deleteAluno, name='delete_aluno'),
    path('visualizar_aluno/(?P<ID_Aluno>\d+)/$', visualizarAluno, name='visualizar_aluno'),
    
    #path('consulta/', consulta, name='consulta'),
    path('consulta/', consulta, name='consulta'),
    #PDFs
    path('relatorio_alunos/', render_pdf_view, name='relatorio_alunos'),
    path('relatorio_id_aluno/(?P<ID_Aluno>\d+)/$', render_pdf_view_id_aluno, name='relatorio_id_aluno'),
]

