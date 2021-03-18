from django.db import models


class Turma(models.Model):
    ID_Turma = models.AutoField(primary_key=True)
    turma = models.CharField(max_length=45)
    MODALIDADE_CHOICES = (
        ('Infantil', 'Infantil'),
        ('Pré Adolescentes', 'Pré Adolescentes'),
        ('Adolescentes', 'Adolescentes'),
        ('Juvenis', 'Juvenis'),
        ('Jovens', 'Jovens'),
        ('Adulto', 'Adulto'),
        ('Novos Convertidos', 'Novos Convertidos'),  
    )
    modalidade = models.CharField(max_length=100, choices=MODALIDADE_CHOICES)
    

    def __str__(self):
        return self.turma