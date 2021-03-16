from django.db import models
#https://www.youtube.com/watch?v=aFelj2GJPzw&t=53s





    
class Aluno(models.Model):
    ID_Aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
