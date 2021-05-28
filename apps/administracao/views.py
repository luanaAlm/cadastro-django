from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Administracao
from .form import ColaboradorForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


@login_required
@csrf_protect
def listarColaboradores(request):
    titulo = 'Colaborador'
    subtitle = 'Lista de Colaboradores'
    colaboradores = Administracao.objects.all()
    return render(request, 'listar_colaboradores.html', {'titulo': titulo, 'subtitle': subtitle, 'colaboradores': colaboradores})


@login_required
def criarColaborador(request):
    titulo = 'Colaborador'
    subtitle = 'Criar novo Colaborador(a)'
    messages.info(request, 'Preencha todos os campos obrigatórios!')
    form = ColaboradorForm(request.POST or None)
    return render(request, 'criar_colaborador.html', {'titulo': titulo, 'subtitle': subtitle, 'form': form})


@login_required
def colaboradorNovo(request):
    form = ColaboradorForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Registro salvo com sucesso!')
        return redirect('listar_colaboradores')
    else:
        messages.error(
            request, 'Registro não foi salvo! Verifique se existe alguma informação errada ou incompleta.')
        return redirect('listar_colaboradores')


@login_required
def updateColaborador(request, ID_Adm):
    data = {}
    colaborador = Administracao.objects.get(ID_Adm=ID_Adm)
    form = ColaboradorForm(request.POST or None, instance=colaborador)
    data['colaborador'] = colaborador
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro modificado com sucesso!')
            return redirect('listar_colaboradores')
    else:
        messages.info(request, 'Preencha todos os campos obrigatórios!')
        return render(request, 'update_colaborador.html', data)


@login_required
def deleteColaborador(request, ID_Adm):
    titulo = 'Colaborador'
    subtitle = 'Deletar Colaborador(a)'

    colaborador = Administracao.objects.get(ID_Adm=ID_Adm)

    if request.method == 'POST':
        colaborador.delete()
        messages.success(request, 'Registro deletado com sucesso!')
        return redirect('listar_colaboradores')
    else:
        return render(request, 'delete_colaborador.html', {'titulo': titulo, 'subtitle': subtitle, 'colaborador': colaborador})


@login_required
def visualizarColaborador(request, ID_Adm):
    data = {}
    colaboradores = Administracao.objects.get(ID_Adm=ID_Adm)
    form = ColaboradorForm(request.POST or None, instance=colaboradores)
    data['colaboradores'] = colaboradores
    data['form'] = form

    return render(request, 'visualizar_colaborador.html', data)
