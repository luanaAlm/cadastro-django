from django import forms
from django.forms import widgets
from django.forms.widgets import ClearableFileInput
from django.forms import ModelForm
from .models import Aluno


class AlunoForm(ModelForm):

    imageAluno = forms.ImageField(widget=ClearableFileInput)

    class Meta:
        model = Aluno
        fields = '__all__'
