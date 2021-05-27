from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Aluno
from .form import AlunoForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


@login_required
@csrf_protect
def listarAlunos(request):
    titulo = 'Alunos'
    subtitle = 'Lista de alunos'
    alunos = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {'titulo': titulo, 'subtitle': subtitle, 'alunos': alunos})


@login_required
def criarAluno(request):
    titulo = 'Aluno'
    subtitle = 'Criar novo Aluno(a)'
    messages.info(request, 'Preencha todos os campos obrigatórios!')
    form = AlunoForm(request.POST or None)
    return render(request, 'criar_alunos.html', {'titulo': titulo, 'subtitle': subtitle, 'form': form})


@login_required
def alunoNovo(request):
    form = AlunoForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Registro salvo com sucesso!')
        return redirect('listar_alunos')
    else:
        messages.error(
            request, 'Registro não foi salvo! Verifique se existe alguma informação errada ou incompleta.')
        return redirect('listar_alunos')


@login_required
def updateAluno(request, ID_Aluno):
    data = {}
    aluno = Aluno.objects.get(ID_Aluno=ID_Aluno)
    form = AlunoForm(instance=aluno)

    data['aluno'] = aluno
    data['form'] = form

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro modificado com sucesso!')
            return redirect('listar_alunos')
    else:
        messages.info(request, 'Preencha todos os campos obrigatórios!')
        return render(request, 'update_alunos.html', data)


@login_required
def deleteAluno(request, ID_Aluno):
    titulo = 'Aluno'
    subtitle = 'Deletar Aluno(a)'
    aluno = Aluno.objects.get(ID_Aluno=ID_Aluno)

    if request.method == 'POST':
        aluno.delete()
        messages.success(request, 'Registro deletado com sucesso!')
        return redirect('listar_alunos')
    else:
        return render(request, 'delete_alunos.html', {'titulo': titulo, 'subtitle': subtitle, 'aluno': aluno})


@login_required
def visualizarAluno(request, ID_Aluno):
    data = {}
    aluno = Aluno.objects.get(ID_Aluno=ID_Aluno)
    form = AlunoForm(request.POST or None, instance=aluno)
    data['aluno'] = aluno
    data['form'] = form

    return render(request, 'visualizar_alunos.html', data)
