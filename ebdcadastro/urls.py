from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls')),
    path('turmas/', include('apps.turmas.urls')),
    path('alunos/', include('apps.alunos.urls')),
    path('professores/', include('apps.professores.urls')),
    path('colaboradores/', include('apps.colaboradores.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
