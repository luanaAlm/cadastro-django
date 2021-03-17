from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Colaborador
from .form import ColaboradorForm

 
#views colaboradores
@login_required
def homeColaboradores(request):
    return render(request, 'home_colaborador.html')

@login_required
def listarColaboradores(request):
    colaborador = Colaborador.objects.all()
    return render(request, 'listar_colaboradores.html', {'colaborador': colaborador})

@login_required
def criarColaborador(request):
    form = ColaboradorForm()
    return render(request, 'criar_colaboradores.html', {'form': form})

@login_required
def ColaboradorNovo(request):
    form = ColaboradorForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('listar_colaboradores')

@login_required
def updateColaborador(request, ID_colaborador):
    data = {}
    colaborador = Colaborador.objects.get(ID_colaborador=ID_colaborador)
    form = ColaboradorForm(request.POST or None, instance=colaborador)
    data['colaborador'] = colaborador
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_colaboradores')
    else:
        return render(request, 'update_colaboradores.html', data)

@login_required
def deleteColaborador(request, ID_colaborador):
    aluno = Colaborador.objects.get(ID_colaborador=ID_colaborador)

    if request.method == 'POST':
        colaborador.delete()
        return redirect('listar_colaboradores')
    else:
        return render(request, 'delete_colaboradores.html', {'colaborador':colaborador})