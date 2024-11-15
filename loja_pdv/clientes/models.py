from django.db import models
from utils.choices import ESTADOS_CHOICES

class PessoaFisica(models.Model):

    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=9, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)

    fone = models.CharField(max_length=11, blank=True)
    email = models.EmailField(blank=True, null=True)

    endereco = models.CharField(max_length=150, blank=True, null=True)
    numero = models.CharField(max_length=15, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=2, choices=ESTADOS_CHOICES)

class PessoaJuridica(models.Model):

    codigo = models.CharField(max_length=10, unique=True)
    nome_fantasia = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    inscricao_municipal = models.CharField(max_length=14, blank=True, null=True)
    inscricao_estadual = models.CharField(max_length=14)

    fone = models.CharField(max_length=11, blank=True)
    email = models.EmailField(blank=True, null=True)

    endereco = models.CharField(max_length=150, blank=True, null=True)
    numero = models.CharField(max_length=15, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=2, choices=ESTADOS_CHOICES)