from django.db import models
from utils.choices import *


class Produtos(models.Model):
    # Informações básicas
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()

    # Informações fiscais
    cfop = models.CharField(max_length=4, choices=CFOP_CHOICES)
    cst = models.CharField(max_length=2, choices=CST_CHOICES, blank=True, null=True)
    csosn = models.CharField(max_length=3, choices=CSOSN_CHOICES, blank=True, null=True)
    unidade = models.CharField(max_length=2, choices=UNIDADES_CHOICES)
    ncm = models.CharField(max_length=8)

    icms = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ipi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pis = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cofins = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ean = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return f'{self.codigo} - {self.descricao}'