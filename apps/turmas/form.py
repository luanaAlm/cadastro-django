from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Turma


class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'
