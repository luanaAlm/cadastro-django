from django.shortcuts import render
from django.http import HttpResponse

#views colaboradores
def home(request):
    return HttpResponse('olá')