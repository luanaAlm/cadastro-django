from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Aluno
from .form import AlunoForm

#views Alunos
@login_required
def homeAlunos(request):
    return render(request, 'home_alunos.html')

@login_required
def listarAlunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {'alunos': alunos})

@login_required
def criarAluno(request):
    form = AlunoForm()
    return render(request, 'criar_alunos.html', {'form': form})

@login_required
def alunoNovo(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('listar_alunos')