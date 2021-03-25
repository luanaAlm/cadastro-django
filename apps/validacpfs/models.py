from django.db import models
from cpf_field.models import CPFField

class ValidaCpf(models.Model):
    cpf = CPFField()

    def __str__(self):
        return self.cpf
