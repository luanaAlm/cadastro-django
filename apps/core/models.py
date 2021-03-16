from django.db import models
#https://www.youtube.com/watch?v=aFelj2GJPzw&t=53s



class Professor(models.Model):
    ID_Professor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    data = models.DateField()

    def __str__(self):
        return self.nome


class Turma(models.Model):
    ID_Turma = models.AutoField(primary_key=True)
    turma = models.CharField(max_length=45)
    Professor = models.ManyToManyField(Professor)

    def __str__(self):
        return self.turma

    
class Aluno(models.Model):
    ID_Aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
