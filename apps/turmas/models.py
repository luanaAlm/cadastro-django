from django.db import models

# Create your models here.
class Turma(models.Model):
    ID_Turma = models.AutoField(primary_key=True)
    turma = models.CharField(max_length=45)

    def __str__(self):
        return self.turma
