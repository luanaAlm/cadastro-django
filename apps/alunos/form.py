# from django.forms import ModelForm
from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'turma', 'sexo', 'data', 'cpf', 'telefone', 'email']

'''
    widgets = {
        'nome': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Digite o seu nome'}),
        'data': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Digite o seu nome'}),
        'cpf': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Digite o seu nome'}),

    }
'''