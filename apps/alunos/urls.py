from django.urls import path
from .views import homeAlunos, listarAlunos


#urls Alunos
urlpatterns = [
    path('',homeAlunos),
    path('listar_alunos',listarAlunos, name='listar_alunos'),
]

