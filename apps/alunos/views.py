from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Aluno
from .form import AlunoForm
from django.views.decorators.csrf import csrf_protect


@login_required
@csrf_protect
def listarAlunos(request):
    titulo = 'Alunos'
    subtitle = 'Lista'
    termo_busca = request.GET.get('pesquisa', None)
    if termo_busca:
        alunos = Aluno.objects.all()
        alunos = alunos.filter(nome__contains=termo_busca)
    else:
        alunos = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {'titulo': titulo, 'subtitle': subtitle, 'alunos': alunos})


@login_required
def criarAluno(request):
    titulo = 'Aluno'
    subtitle = 'Criar novo Aluno'
    form = AlunoForm(request.POST or None)
    return render(request, 'criar_alunos.html', {'titulo': titulo, 'subtitle': subtitle, 'form': form})


@login_required
def alunoNovo(request):
    form = AlunoForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
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
            return redirect('listar_alunos')
    else:
        return render(request, 'update_alunos.html', data)


@login_required
def deleteAluno(request, ID_Aluno):
    aluno = Aluno.objects.get(ID_Aluno=ID_Aluno)

    if request.method == 'POST':
        aluno.delete()
        return redirect('listar_alunos')
    else:
        return render(request, 'delete_alunos.html', {'aluno': aluno})


@login_required
def visualizarAluno(request, ID_Aluno):
    data = {}
    aluno = Aluno.objects.get(ID_Aluno=ID_Aluno)
    form = AlunoForm(request.POST or None, instance=aluno)
    data['aluno'] = aluno
    data['form'] = form

    return render(request, 'visualizar_alunos.html', data)


@login_required
@csrf_protect
def consulta(request):
    consulta = request.POST.get('consulta')
    campo = request.POST.get('campo')

    if campo == 'nome':
        alunos = Aluno.objects.filter(nome__contains=consulta)
    elif campo == 'cpf':
        alunos = Aluno.objects.filter(cpf__contains=consulta)
    elif campo == 'endereco':
        alunos = Aluno.objects.filter(endereco__contains=consulta)
    elif campo == 'bairro':
        alunos = Aluno.objects.filter(bairro__contains=consulta)

    return render(request, 'listar_alunos.html', {'alunos': alunos})


_campo = ''


def ordenacao(request, campo):
    global _campo
    if campo == _campo:
        alunos = Aluno.objects.all().order_by(campo).reverse()
        _campo = ''
    else:
        alunos = Aluno.objects.all().order_by(campo)
        _campo = campo
    return render(request, 'listar_alunos.html', {'alunos': alunos})
