from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Turma 
from .form import TurmaForm

#views Turmas
@login_required
def homeTurmas(request):
    return render(request, 'home_turmas.html')

@login_required
def listarTurmas(request):
    turmas = Turma.objects.all()
    return render(request, 'listar_turmas.html', {'turmas': turmas})

@login_required 
def criarTurmas(request):
    form = TurmaForm()
    return render(request, 'criar_turmas.html', {'form': form})

@login_required
def turmaNovo(request):
    form = TurmaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('listar_turmas')

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
def deleteTurma(request, ID_Turma):
    turma = Turma.objects.get(ID_Turma=ID_Turma)

    if request.method == 'POST':
        turma.delete()
        return redirect('listar_turmas')
    else:
        return render(request, 'delete_turma.html', {'turma':turma})

@login_required
def renascer(request):
    turmas = Turma.objects.filter(turma='Renascer')
    return render(request, 'renascer.html', {'turmas': turmas})
