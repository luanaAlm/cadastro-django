from django.urls import path
from .views import criarColaborador, colaboradorNovo, listarColaboradores, consulta, updateColaborador

# urls Professores
urlpatterns = [
    path('criar_colaborador', criarColaborador, name='criar_colaborador'),
    path('novo_colaborador', colaboradorNovo, name='novo_colaborador'),
    path('listar_colaboradores', listarColaboradores,
         name='listar_colaboradores'),
    path('consulta/', consulta),
    path('^update_colaborador/(?P<ID_Adm>\d+)/$',
         updateColaborador, name='update_colaborador'),

]
