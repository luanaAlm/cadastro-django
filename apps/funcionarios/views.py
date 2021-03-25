from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Funcionario
from .form import FuncionarioForm

 
#views Funcionarios
@login_required
def homeFuncionarios(request):
    return render(request, 'home_funcionario.html')

@login_required
def listarFuncionarios(request):
    funcionario = Funcionario.objects.all()
    return render(request, 'listar_funcionarios.html', {'funcionario': funcionario})

@login_required
def criarFuncionario(request):
    form = FuncionarioForm()
    return render(request, 'criar_funcionarios.html', {'form': form})

@login_required
def FuncionarioNovo(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('listar_funcionarios')

@login_required
def updateFuncionario(request, ID_funcionario):
    data = {}
    funcionario = Funcionario.objects.get(ID_funcionario=ID_funcionario)
    form = FuncionarioForm(request.POST or None, instance=funcionario)
    data['funcionario'] = funcionario
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_funcionarios')
    else:
        return render(request, 'update_funcionarios.html', data)

@login_required
def deleteFuncionario(request, ID_funcionario):
    aluno = Funcionario.objects.get(ID_funcionario=ID_funcionario)

    if request.method == 'POST':
        funcionario.delete()
        return redirect('listar_funcionarios')
    else:
        return render(request, 'delete_funcionarios.html', {'funcionario':funcionario})