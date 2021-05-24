from django.urls import path
from .views import criarColaborador, colaboradorNovo, listarColaboradores, consulta

# urls Professores
urlpatterns = [
    path('criar_colaborador', criarColaborador, name='criar_colaborador'),
    path('novo_colaborador', colaboradorNovo, name='novo_colaborador'),
    path('listar_colaboradores', listarColaboradores,
         name='listar_colaboradores'),
    path('consulta/', consulta),

]
