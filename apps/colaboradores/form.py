from django.forms import ModelForm
from .models import Colaborador

class ColaboradorForm(ModelForm):
    class Meta:
        model = Colaborador
        fields = '__all__'