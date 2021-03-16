from django.urls import path
from .views import home


#urls core
urlpatterns = [
    path('',home),
]
