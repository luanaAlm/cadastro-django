from django.db import models
from apps.turmas.models import Turma
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

    ID_Aluno = models.AutoField(primary_key=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    nome = models.CharField(max_length=45)
    sexo = models.CharField(max_length=100, choices=SEXO_CHOICES)
    data = models.DateField(max_length=8)
    cpf = CPFField(max_length=14)
    telefone = models.CharField(blank=False, null=False, max_length=11)
    email = models.EmailField(max_length=200, null=True)
    # endereço
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=100, blank=False, null=False)
    numero = models.IntegerField(null=True, blank=True)
    complemento = models.CharField(max_length=1000, null=True)
    bairro = models.CharField(max_length=100, blank=False, null=False)
    municipio = models.CharField(max_length=100, blank=False, null=False)
    estado = models.CharField(max_length=100, choices=STATE_CHOICES)
    # Responsavel
    nomeResp = models.CharField(
        "Em caso de emergência entrar em contato com?", max_length=45)
    telefoneResp = models.CharField(
        "Telefone do responsável", blank=False, null=False, max_length=11)
    # saude
    Saude = models.CharField("Possui algum problema de saúde?", max_length=100)
    Medicamento = models.CharField(
        "O aluno toma algum medicamento?", max_length=100)
    Deficiencia = models.CharField("Tem alguma deficiência?", max_length=100)
    RestricaoAlimentar = models.CharField(
        "Alguma alergia ou restrição alimentar?", max_length=100)
    # imagem
    imagem = models.ImageField(upload_to="img/%y")

    def __str__(self):
        return self.nome
