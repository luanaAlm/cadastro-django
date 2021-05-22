from django.urls import path
from .views import criarColaborador, colaboradorNovo

# urls Professores
urlpatterns = [
    path('criar_colaborador', criarColaborador, name='criar_colaborador'),
    path('novo_colaborador', colaboradorNovo, name='novo_colaborador'),

]
