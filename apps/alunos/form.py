# from django.forms import ModelForm
from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [ 'turma','nome', 'sexo', 'data', 'cpf', 'telefone', 'email', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'municipio', 'estado']

