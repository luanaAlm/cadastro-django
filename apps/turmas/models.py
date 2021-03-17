from django.db import models
#from apps.professores.models import Professor

class Turma(models.Model):
    ID_Turma = models.AutoField(primary_key=True)
    turma = models.CharField(max_length=45)
    #Professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.turma
