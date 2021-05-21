from django.db import models
from cpf_field.models import CPFField


class Administracao(models.Model):
    FUNCAO_CHOICES = (
        ('Coordenador(a) Infantil', 'Coordenador(a) Infantil'),
        ('Coordenador(a) de Adultos', 'Coordenador(a) de Adultos'),
        ('Superintendente', 'Superintendente'),
        ('Tesoureiro(a)', 'Tesoureiro(a)'),
        ('Secretário(a)', 'Secretário(a)'),
    )
    SEXO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    )
    STATE_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', ' Maranhão '),
        (' MT ', ' Mato Grosso '),
        (' MS ', ' Mato Grosso do Sul '),
        (' MG ', ' Minas Gerais '),
        (' PA ', ' Pará '),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima '),
        (' SC ', ' Santa Catarina '),
        (' SP ', ' São Paulo '),
        (' SE ', ' Sergipe '),
        (' TO ', ' Tocantins ')
    )

    ID_Adm = models.AutoField(primary_key=True)

    funcao = models.CharField(max_length=100, choices=FUNCAO_CHOICES)
    nome = models.CharField(max_length=45)
    sexo = models.CharField(max_length=100, choices=SEXO_CHOICES)
    data = models.DateField(max_length=8)
    cpf = CPFField(max_length=14)
    telefone = models.IntegerField(blank=False, null=False, max_length=16)
    email = models.EmailField(max_length=200, null=True)
    # endereço
    cep = models.IntegerField(max_length=8)
    endereco = models.CharField(max_length=100, blank=False, null=False)
    numero = models.IntegerField(null=True, blank=True)
    complemento = models.CharField(max_length=1000, null=True)
    bairro = models.CharField(max_length=100, blank=False, null=False)
    municipio = models.CharField(max_length=100, blank=False, null=False)
    estado = models.CharField(max_length=100, choices=STATE_CHOICES)
    # imagem
    imagem = models.ImageField(upload_to="img/%y")

    def __str__(self):
        return self.nome
