from django import template
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from xhtml2pdf import context
from .models import Turma
# Aluno
from apps.alunos.models import Aluno
# Professor
from apps.professores.models import Professor
# pdf
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


@login_required
def homeTurmas(request):
    turmas = Turma.objects.all().order_by("modalidade")
    return render(request, 'home_turmas.html', {'turmas': turmas})


@login_required
def listarTurmas(request, turma_id):
    titulos = Turma.objects.filter(ID_Turma=turma_id)
    alunos = Aluno.objects.filter(turma_id=turma_id).order_by("nome")
    professores = Professor.objects.filter(turma_id=turma_id).order_by("nome")
    return render(request, 'listar_turmas.html', {'titulos': titulos, 'alunos': alunos, 'professores': professores})


def pdfDiarioClasse(request, turma_id):
    titulos = Turma.objects.filter(ID_Turma=turma_id)
    alunos = Aluno.objects.filter(turma_id=turma_id).order_by("nome")
    professores = Professor.objects.filter(turma_id=turma_id).order_by("nome")

    template_path = 'pdf/pdf_diario_classe.html'
    context = {'titulos': titulos, 'alunos': alunos,
               'professores': professores}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
