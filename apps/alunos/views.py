from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Aluno
 
#views Alunos
@login_required
def homeAlunos(request):
    return render(request, 'home_alunos.html')

@login_required
def listarAlunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {'alunos': alunos})