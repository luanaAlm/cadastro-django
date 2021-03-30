from django.db import models
from  apps.turmas.models import Turma
from cpf_field.models import CPFField


class Aluno(models.Model):
    SEXO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    )
    STATE_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia' ),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', ' Maranhão '),
        (' MT ',' Mato Grosso '),
        (' MS ',' Mato Grosso do Sul '),
        (' MG ',' Minas Gerais '),
        (' PA ',' Pará '),
        ( 'PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima '),
        (' SC ',' Santa Catarina '),
        (' SP ',' São Paulo '),
        (' SE ',' Sergipe '),
        (' TO ',' Tocantins ')
    )
    ID_Aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    cpf = CPFField(max_length=14)
    sexo = models.CharField(max_length=100, choices=SEXO_CHOICES)
    data = models.DateField(max_length=8)
    telefone = models.IntegerField(blank=False, null=False, max_length=16)
    email = models.EmailField(max_length=200)
    #endereço
    cep = models.IntegerField(max_length=8)
    endereco = models.CharField(max_length=100, blank=False, null=False)
    numero = models.IntegerField(null=True, blank=True)
    complemento = models.CharField(max_length=1000, null=True)
    bairro = models.CharField(max_length=100, blank=False, null=False)
    municipio = models.CharField(max_length=100, blank=False, null=False)
    estado = models.CharField(max_length=100, choices=STATE_CHOICES)
	#imagem
    imagem = models.ImageField(upload_to="imagem/%y")
    
    def __str__(self):
        return self.nome
