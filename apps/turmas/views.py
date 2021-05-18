from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Turma
from apps.alunos.models import Aluno
from apps.professores.models import Professor
from .form import TurmaForm
# pdf
from django.template.loader import get_template
from xhtml2pdf import pisa


# views Turmas
@login_required
def homeTurmas(request):
    return render(request, 'home_turmas.html')


@login_required
def listarTurmas(request):
    turmas = Turma.objects.all()
    return render(request, 'listar_turmas.html', {'turmas': turmas})


@login_required
def criarTurmas(request):
    titulo = 'Turma'
    subtitle = 'Criar nova Turma'

    form = TurmaForm()
    return render(request, 'criar_turmas.html', {'titulo': titulo, 'subtitle': subtitle, 'form': form})


@login_required
def turmaNovo(request):
    form = TurmaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('listar_turmas')


@login_required
def updateTurma(request, ID_Turma):
    data = {}
    turma = Turma.objects.get(ID_Turma=ID_Turma)
    form = TurmaForm(request.POST or None, instance=turma)
    data['turma'] = turma
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_turmas')
    else:
        return render(request, 'update_turmas.html', data)


@login_required
def deleteTurma(request, ID_Turma):
    turma = Turma.objects.get(ID_Turma=ID_Turma)

    if request.method == 'POST':
        turma.delete()
        return redirect('listar_turmas')
    else:
        return render(request, 'delete_turma.html', {'turma': turma})

# Turma Renascer


@login_required
def renascer(request):
    turmas = Turma.objects.filter(turma='Renascer')
    alunos = Aluno.objects.filter(turma_id='1')
    professores = Professor.objects.filter(turma_id='1')
    return render(request, 'turmas/renascer.html', {'turmas': turmas, 'alunos': alunos, 'professores': professores})

# Turma Renascer


@login_required
def jardimDeus(request):
    turmas = Turma.objects.filter(turma='Jardim de Deus')
    alunos = Aluno.objects.filter(turma_id='2')
    professores = Professor.objects.filter(turma_id='2')
    return render(request, 'turmas/jardim_deus.html', {'turmas': turmas, 'alunos': alunos, 'professores': professores})


# pdf
def render_pdf_view(request):
    template_path = 'pdf_turmas/relatorio_renascer.html'
    turmas = Turma.objects.filter(turma='Renascer')
    professores = Professor.objects.filter(turma_id='1')
    alunos = Aluno.objects.filter(turma_id='1')

    context = {'myvar': 'Turma', 'turmas': turmas,
               'professores': professores, 'alunos': alunos}
    response = HttpResponse(content_type='application/pdf')
    # dowload
    #response['Content-Disposition'] = 'attachment; filename="aluno.pdf"'
    # find the template and render it.
    # visualização
    response['Content-Disposition'] = 'filename="renascer.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
