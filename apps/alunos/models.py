from django.db import models


from  apps.turmas.models import Turma
class Aluno(models.Model):
    ID_Aluno = models.AutoField(primary_key=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    nome = models.CharField(max_length=45)
        
    def __str__(self):
        return self.nome
