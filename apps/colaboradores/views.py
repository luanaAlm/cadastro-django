from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

 
#views colaboradores
@login_required
def home(request):
    return HttpResponse('olá')