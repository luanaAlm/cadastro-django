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
# Excel
from django.views.generic import View
import xlwt


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

# pdf


def pdfDiarioClasse(request, turma_id):
    titulos = Turma.objects.filter(ID_Turma=turma_id)
    alunos = Aluno.objects.filter(turma_id=turma_id).order_by("nome")
    professores = Professor.objects.filter(turma_id=turma_id).order_by("nome")

    template_path = 'pdf/pdf_diario_classe.html'
    context = {'titulos': titulos, 'alunos': alunos,
               'professores': professores}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # attachment;
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

# excel


class turmaExl(View):
    def get(self, request, turma_id):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="turma_ebd.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        # this will make a sheet named Users Data
        ws = wb.add_sheet('Alunos')

        # Sheet header, first row
        row_num = 1

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Matricula', 'Data Nasc.', 'Nome']

        for col_num in range(len(columns)):
            # at 0 row 0 column
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        alunos = Aluno.objects.filter(turma_id=turma_id).order_by(
            "nome").values_list('ID_Aluno', 'data', 'nome')
        for aluno in alunos:
            row_num += 1
            for col_num in range(len(aluno)):
                ws.write(row_num, col_num, aluno[col_num], font_style)

        wb.save(response)
        return response
