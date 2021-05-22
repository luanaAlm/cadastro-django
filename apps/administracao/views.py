from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Administracao
from .form import ColaboradorForm


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
    return redirect('home')
