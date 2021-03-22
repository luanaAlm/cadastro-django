from django.db import models
from  apps.turmas.models import Turma


class Aluno(models.Model):
    SEXO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    )
    ID_Aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    sexo = models.CharField(max_length=100, choices=SEXO_CHOICES)
    data = models.DateField()

    def __str__(self):
        return self.nome
