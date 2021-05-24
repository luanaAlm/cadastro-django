from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Administracao
from .form import ColaboradorForm
from django.views.decorators.csrf import csrf_protect


@login_required
def listarColaboradores(request):
    titulo = 'Colaborador'
    subtitle = 'Lista de Colaboradores'
    termo_busca = request.GET.get('pesquisa', None)
    if termo_busca:
        colaboradores = Administracao.objects.all()
        colaboradores = Administracao.filter(nome__contains=termo_busca)
    else:
        colaboradores = Administracao.objects.all()
    return render(request, 'listar_colaboradores.html', {'titulo': titulo, 'subtitle': subtitle, 'colaboradores': colaboradores})


@login_required
@csrf_protect
def consulta(request):
    consulta = request.POST.get('consulta')
    campo = request.POST.get('campo')

    if campo == 'nome':
        colaboradores = Administracao.objects.filter(nome__contains=consulta)
    elif campo == 'funcao':
        colaboradores = Administracao.objects.filter(funcao__contains=consulta)

    return render(request, 'listar_colaboradores.html', {'colaboradores': colaboradores})


@login_required
def criarColaborador(request):
    titulo = 'Colaborador'
    subtitle = 'Novo Colaborador'
    form = ColaboradorForm(request.POST or None)
    return render(request, 'criar_colaborador.html', {'titulo': titulo, 'subtitle': subtitle, 'form': form})


@login_required
def colaboradorNovo(request):
    form = ColaboradorForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect('listar_colaboradores')
