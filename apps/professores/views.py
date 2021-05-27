from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Professor
from .form import ProfessorForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


@login_required
def listarProfessores(request):
    titulo = 'Professor'
    subtitle = 'Lista de Professores'
    professores = Professor.objects.all()
    return render(request, 'listar_professores.html', {'titulo': titulo, 'subtitle': subtitle, 'professores': professores})


@login_required
def criarProfessor(request):
    titulo = 'Professor'
    subtitle = 'Criar novo Professor(a)'
    messages.info(request, 'Preencha todos os campos obrigatórios!')
    form = ProfessorForm(request.POST or None)
    return render(request, 'criar_professores.html', {'titulo': titulo, 'subtitle': subtitle, 'form': form})


@login_required
def professorNovo(request):
    form = ProfessorForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Registro salvo com sucesso!')
        return redirect('listar_professores')
    else:
        messages.error(
            request, 'Registro não foi salvo! Verifique se existe alguma informação errada ou incompleta.')
        return redirect('listar_professores')


@login_required
def updateProfessor(request, ID_Professor):
    data = {}
    professor = Professor.objects.get(ID_Professor=ID_Professor)
    form = ProfessorForm(request.POST or None, instance=professor)
    data['professor'] = professor
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro modificado com sucesso!')
            return redirect('listar_professores')
    else:
        messages.info(request, 'Preencha todos os campos obrigatórios!')
        return render(request, 'update_professores.html', data)


@login_required
def deleteProfessor(request, ID_Professor):
    titulo = 'Professor'
    subtitle = 'Deletar Porfessor(a)'

    professor = Professor.objects.get(ID_Professor=ID_Professor)

    if request.method == 'POST':
        professor.delete()
        messages.success(request, 'Registro deletado com sucesso!')
        return redirect('listar_professores')
    else:
        return render(request, 'delete_professores.html', {'titulo': titulo, 'subtitle': subtitle, 'professor': professor})


@login_required
def visualizarProfessor(request, ID_Professor):
    data = {}
    professores = Professor.objects.get(ID_Professor=ID_Professor)
    form = ProfessorForm(request.POST or None, instance=professores)
    data['professores'] = professores
    data['form'] = form

    return render(request, 'visualizar_professor.html', data)
