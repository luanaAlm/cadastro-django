from django.db import models


class Professor(models.Model):
    ID_Professor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    data = models.DateField()
    
    def __str__(self):
        return self.nome


