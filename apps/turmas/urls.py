from django.urls import path
from .views import homeTurmas, listarTurmas, updateTurma


# urls Turmas
urlpatterns = [
    path('home_turmas', homeTurmas, name='home_turmas'),

    path('listar_turmas/(?P<turma_id>\d+)/$',
         listarTurmas, name='listar_turmas'),

    path('^update_turma/(?P<ID_Turma>\d+)/$',
         updateTurma, name='update_turma'),


]
