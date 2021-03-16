from django.urls import path
from .views import home


#urls colaboradores
urlpatterns = [
    path('',home),
]
