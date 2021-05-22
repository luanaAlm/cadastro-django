from django import forms
from django.forms import ModelForm
from .models import Administracao
from django.forms.widgets import ClearableFileInput


class ColaboradorForm(ModelForm):

    imagem = forms.ImageField(widget=ClearableFileInput)

    class Meta:
        model = Administracao
        fields = '__all__'
