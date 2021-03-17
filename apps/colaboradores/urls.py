from django.urls import path
from .views import homeColaboradores, listarColaboradores, criarColaborador, ColaboradorNovo, updateColaborador, deleteColaborador


#urls colaboradores
urlpatterns = [
    path('',homeColaboradores, name='home_colaboradores'),
    path('listar_colaboradores',listarColaboradores, name='listar_colaboradores'),
    path('criar_colaboradores',criarColaborador, name='criar_colaboradores'),
    path('novo_colaborador',ColaboradorNovo, name='novo_colaborador'),
    path('^update_colaborador/(?P<ID_Colaborador>\d+)/$', updateColaborador, name='update_colaborador'),
    path('^delete_colaborador/(?P<ID_Colaborador>\d+)/$', deleteColaborador, name='delete_colaborador'),
]
