from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Professor
from .form import ProfessorForm

# views Professores


@login_required
def homeProfessores(request):
    return render(request, 'home_professores.html')


@login_required
def listarProfessores(request):
    titulo = 'Professor'
    subtitle = 'Lista de Professores'
    professores = Professor.objects.all()
    return render(request, 'listar_professores.html', {'titulo': titulo, 'subtitle': subtitle, 'professores': professores})


@login_required
def criarProfessor(request):
    form = ProfessorForm()
    return render(request, 'criar_professores.html', {'form': form})


@login_required
def visualizarProfessor(request, ID_Professor):
    data = {}
    professores = Professor.objects.get(ID_Professor=ID_Professor)
    form = ProfessorForm(request.POST or None, instance=professores)
    data['professores'] = professores
    data['form'] = form

    return render(request, 'visualizar_professor.html', data)


@login_required
def professorNovo(request):
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
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
            return redirect('listar_professores')
    else:
        return render(request, 'update_professores.html', data)


@login_required
def deleteProfessor(request, ID_Professor):
    professor = Professor.objects.get(ID_Professor=ID_Professor)

    if request.method == 'POST':
        professor.delete()
        return redirect('listar_professores')
    else:
        return render(request, 'delete_professores.html', {'professor': professor})
