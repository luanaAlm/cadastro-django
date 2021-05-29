from django.urls import path
from .views import homeTurmas, listarTurmas


# urls Turmas
urlpatterns = [
    path('home_turmas', homeTurmas, name='home_turmas'),

    path('listar_turmas/(?P<turma_id>\d+)/$',
         listarTurmas, name='listar_turmas'),
]
