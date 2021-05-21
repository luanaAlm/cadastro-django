from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Turma
# Aluno
from apps.alunos.models import Aluno
# Professor
from apps.professores.models import Professor


@login_required
def homeTurmas(request):
    turmas = Turma.objects.all()
    return render(request, 'home_turmas.html', {'turmas': turmas})


@login_required
def listarTurmas(request, turma_id):
    alunos = Aluno.objects.filter(turma_id=turma_id)
    professores = Professor.objects.filter(turma_id=turma_id)
    return render(request, 'listar_turmas.html', {'alunos': alunos, 'professores': professores})
