from django.db import models
from home.models import CFOP, CST_CSOSN, Unidades

class Produtos(models.Model):
    # Informações básicas
    codigo = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()

    cfop = models.ForeignKey(CFOP, on_delete=models.SET_NULL, null=True)
    cst_csosn = models.ForeignKey(CST_CSOSN, on_delete=models.SET_NULL, null=True)
    unidade = models.ForeignKey(Unidades, on_delete=models.SET_NULL, null=True)

    ncm = models.CharField(max_length=8)
    icms = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ipi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pis = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cofins = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ean = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return f'{self.codigo} - {self.descricao}'