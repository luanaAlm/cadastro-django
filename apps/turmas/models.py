from django.db import models


class Turma(models.Model):
    ID_Turma = models.AutoField(primary_key=True)
    turma = models.CharField(max_length=45)
    Professor = models.ManyToManyField(Professor)

    def __str__(self):
        return self.turma
