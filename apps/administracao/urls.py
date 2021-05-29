from django.urls import path
from .views import criarColaborador, colaboradorNovo, listarColaboradores, updateColaborador, deleteColaborador, visualizarColaborador, colaboradoresCSV


# urls Professores
urlpatterns = [
    path('criar_colaborador', criarColaborador, name='criar_colaborador'),
    path('novo_colaborador', colaboradorNovo, name='novo_colaborador'),
    path('listar_colaboradores', listarColaboradores,
         name='listar_colaboradores'),
    path('^update_colaborador/(?P<ID_Adm>\d+)/$',
         updateColaborador, name='update_colaborador'),
    path('^delete_colaborador/(?P<ID_Adm>\d+)/$',
         deleteColaborador, name='delete_colaborador'),
    path('visualizar_colaborador/(?P<ID_Adm>\d+)/$', visualizarColaborador,
         name='visualizar_colaborador'),
    # excel
    path('colaboradores_exportar_csv', colaboradoresCSV.as_view(),
         name='colaboradores_exportar_csv'),





]
