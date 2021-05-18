from django import forms
from django.forms import ModelForm
from .models import Professor
from django.forms.widgets import ClearableFileInput


class ProfessorForm(ModelForm):

    imagem = forms.ImageField(widget=ClearableFileInput)

    class Meta:
        model = Professor
        fields = '__all__'
