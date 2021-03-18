from django.db import models

# Create your models here.
class Turma(models.Model):
    ID_Turma = models.AutoField(primary_key=True)
    turma = models.CharField(max_length=45)
    MODALIDADE_CHOICES = (
        ('Adolescentes', 'Adolescentes'),
        ('Adulto', 'Adulto'),
        ('Infantil', 'Infantil'),
        ('Jovens', 'Jovens'),
        ('Juvenis','Juvenis'),
        ('Pré-Adolescentes', 'Pré-Adolescentes'),
    )
    modalidade = models.CharField(max_length=100, choices=MODALIDADE_CHOICES)
    
    
    def __str__(self):
        return self.turma
