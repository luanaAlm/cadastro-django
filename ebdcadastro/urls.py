from django.contrib import admin
from django.urls import path, include
# imagens
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.core.urls')),
    path('turmas/', include('apps.turmas.urls')),
    path('alunos/', include('apps.alunos.urls')),
    path('professores/', include('apps.professores.urls')),
    path('administracao/', include('apps.administracao.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
# media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
