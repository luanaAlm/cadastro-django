from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Turma
from .form import TurmaForm
# Aluno
from apps.alunos.models import Aluno
# Professor
from apps.professores.models import Professor


@login_required
def homeTurmas(request):
    turmas = Turma.objects.all()
    return render(request, 'home_turmas.html', {'turmas': turmas})


@login_required
def updateTurma(request, ID_Turma):
    data = {}
    turma = Turma.objects.get(ID_Turma=ID_Turma)
    form = TurmaForm(request.POST or None, instance=turma)
    data['turma'] = turma
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_turmas')
    else:
        return render(request, 'update_turmas.html', data)


@login_required
def listarTurmas(request, turma_id):
    #turmas = Turma.objects.filter()
    alunos = Aluno.objects.filter(turma_id=turma_id)
    professores = Professor.objects.filter(turma_id=turma_id)
    # 'turmas': turmas,
    return render(request, 'listar_turmas.html', {'alunos': alunos, 'professores': professores})
