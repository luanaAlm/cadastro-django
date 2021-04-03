from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Aluno
from .form import AlunoForm
from django.views.decorators.csrf import csrf_protect

#pdf
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView , View


#views Alunos
#@login_required
#def homeAlunos(request):
#    return render(request, 'home_alunos.html')

@login_required
@csrf_protect
def listarAlunos(request):
    termo_busca = request.GET.get('pesquisa', None)
    if termo_busca:
        alunos = Aluno.objects.all()
        alunos = alunos.filter(nome__contains=termo_busca)
    else:
        alunos = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {'alunos': alunos})

@login_required
def criarAluno(request):
    form = AlunoForm()
    return render(request, 'criar_alunos.html', {'form': form})

@login_required
def alunoNovo(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('listar_alunos')

@login_required
def updateAluno(request, ID_Aluno):
    data = {}
    aluno = Aluno.objects.get(ID_Aluno=ID_Aluno)
    form = AlunoForm(request.POST or None, instance=aluno)
    data['aluno'] = aluno
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        return render(request, 'update_alunos.html', data)

@login_required
def deleteAluno(request, ID_Aluno):
    aluno = Aluno.objects.get(ID_Aluno=ID_Aluno)

    if request.method == 'POST':
        aluno.delete()
        return redirect('listar_alunos')
    else:
        return render(request, 'delete_alunos.html', {'aluno':aluno})

@login_required
def visualizarAluno(request, ID_Aluno):
    data = {}
    aluno = Aluno.objects.get(ID_Aluno=ID_Aluno)
    form = AlunoForm(request.POST or None, instance=aluno)
    data['aluno'] = aluno
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        return render(request, 'visualizar_alunos.html', data)


@csrf_protect
def consulta(request):
	consulta = request.POST.get('consulta')
	campo = request.POST.get('campo')

	if campo   == 'nome':
		alunos = Aluno.objects.filter(nome__contains=consulta)
	return render(request, 'listar_alunos.html', {'alunos': alunos})

#pdf
def render_pdf_view(request):
    template_path = 'pdfs/relatorio_alunos.html'
    alunos = Aluno.objects.all()
    context = {'myvar': 'Alunos', 'alunos': alunos}
    response = HttpResponse(content_type='application/pdf')
    #dowload
    #response['Content-Disposition'] = 'attachment; filename="aluno.pdf"'
    # find the template and render it.
    #visualização
    response['Content-Disposition'] = 'filename="aluno.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

