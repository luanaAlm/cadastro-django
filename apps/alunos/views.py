from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Aluno
from .form import AlunoForm

from django.views.decorators.csrf import csrf_protect

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

@login_required
def updateAluno(request, ID_Aluno):
    data = {}
    aluno = Aluno.objects.get(ID_Aluno=ID_Aluno)
    form = AlunoForm(request.POST or None, instance=aluno)
    data['aluno'] = aluno
    data['form'] = form

    if request.method == 'POST':
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
        return render(request, 'delete_alunos.html', {'aluno':aluno})

@login_required
@csrf_protect
def consulta(request):
	consulta = request.POST.get('consulta')
	campo = request.POST.get('campo')

	if campo   == 'nome':
		alunos = Aluno.objects.filter(nome__contains=consulta)

	return render(request, 'listar_alunos.html', {'alunos': alunos})
