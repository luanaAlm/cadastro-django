from django.db import models
#from apps.turmas.models import Turma


class Professor(models.Model):
    ID_Professor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    data = models.DateField()
#    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.nome