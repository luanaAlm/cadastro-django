from django.urls import path
from .views import homeFuncionarios, listarFuncionarios, criarFuncionario, FuncionarioNovo, updateFuncionario, deleteFuncionario


#urls funcionarios
urlpatterns = [
    path('',homeFuncionarios, name='home_funcionario'),
    path('listar_funcionarios',listarFuncionarios, name='listar_funcionarios'),
    path('criar_funcionarios',criarFuncionario, name='criar_funcionarios'),
    path('novo_funcionario',FuncionarioNovo, name='novo_funcionario'),
    path('^update_funcionario/(?P<ID_funcionario>\d+)/$', updateFuncionario, name='update_funcionario'),
    path('^delete_funcionario/(?P<ID_funcionario>\d+)/$', deleteFuncionario, name='delete_funcionario'),
]
