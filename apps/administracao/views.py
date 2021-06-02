from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Administracao
from .form import ColaboradorForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.http import HttpResponse
# Excel
from django.views.generic import View
import xlwt
# pdf
from django.template.loader import get_template
from xhtml2pdf import pisa


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


class colaboradoresCSV(View):
    def get(self, request, ):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="colaboradores-ebd.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        # this will make a sheet named Users Data
        ws = wb.add_sheet('Colaboradores')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['Matricula', 'Funcao', 'Data Nasc.',
                   'Nome', 'Sexo', 'CPF', 'Telefone',
                   'Email', 'CEP', 'Endereco', 'Numero', 'Complemento',
                   'Bairro', 'Municipio', 'Estado']

        for col_num in range(len(columns)):
            # at 0 row 0 column
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = Administracao.objects.all().values_list(
            'ID_Adm', 'funcao', 'data', 'nome', 'sexo', 'cpf', 'telefone', 'email', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'municipio', 'estado')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response


# pdf
def pdfColaborador(request, ID_Adm):
    colaboradores = Administracao.objects.filter(ID_Adm=ID_Adm)

    template_path = 'pdf/pdf_colaborador.html'
    context = {'colaboradores': colaboradores}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # attachment;
    response['Content-Disposition'] = 'filename="pdf_colaborador.pdf"'
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
