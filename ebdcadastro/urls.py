from django.contrib import admin
from django.urls import path, include

#urls geral
urlpatterns = [
    path('', include('apps.core.urls')),
    path('colaboradores/', include('apps.colaboradores.urls')),
    path('admin/', admin.site.urls),
]
