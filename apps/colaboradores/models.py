from django.db import models
from django.contrib.auth.models import User


class Colaborador(models.Model):
    ID_colaborador = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=45)
    
    def __str__(self):
        return self.nome
