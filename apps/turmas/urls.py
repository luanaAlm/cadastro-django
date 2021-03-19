from django.urls import path
from .views import homeTurmas, listarTurmas, criarTurmas, turmaNovo, updateTurma, deleteTurma, renascer, jardimDeus, render_pdf_view


#urls Turmas
urlpatterns = [
    path('',homeTurmas, name='home_turmas'),
    path('listar_turmas',listarTurmas, name='listar_turmas'),
    path('criar_turmas',criarTurmas, name='criar_turmas'),
    path('novo_turma',turmaNovo, name='novo_turma'),
    path('^update_turma/(?P<ID_Turma>\d+)/$', updateTurma, name='update_turma'),
    path('^delete_turma/(?P<ID_Turma>\d+)/$', deleteTurma, name='delete_turma'),
    #salas
    path('renascer/', renascer, name='renascer'),
    path('relatorio_renascer/', render_pdf_view, name='relatorio_renascer'),
    path('jardimDeus/', jardimDeus, name='jardimDeus'),

    
]

