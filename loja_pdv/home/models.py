from django.db import models
from utils.choices import ESTADOS_CHOICES
    
class DadosLoja(models.Model):
    
    nome_fantasia = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    inscricao_municipal = models.CharField(max_length=14, blank=True, null=True)
    inscricao_estadual = models.CharField(max_length=14)
    inscricao_estadual_st = models.CharField(max_length=14, blank=True, null=True)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=ESTADOS_CHOICES)
    fone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)

    def __str__(self):
        return f'{self.nome_fantasia}'

