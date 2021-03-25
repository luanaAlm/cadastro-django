from django.db import models
from  apps.turmas.models import Turma
from cpf_field.models import CPFField

class Aluno(models.Model):
    SEXO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    )
    ID_Aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    cpf = CPFField()
    sexo = models.CharField(max_length=100, choices=SEXO_CHOICES)
    data = models.DateField()
    imagem = models.ImageField(upload_to='alunos')
    telefone = models.IntegerField(blank=False, null=False)
    email = models.EmailField(max_length=200, blank=True)
	

    
    def __str__(self):
        return self.nome
