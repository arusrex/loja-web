from django.db import models
from home.models import *

class ConfiguracaoSAT(models.Model):
    loja = models.OneToOneField(DadosLoja, on_delete=models.CASCADE)
    codigo_ativacao = models.CharField(max_length=16)
    tipo_certificado = models.IntegerField(choices=[(1, 'A1'), (2, 'A3')])
    numero_caixa = models.CharField(max_length=3)
    teste = models.BooleanField(default=True)
    caminho = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f'Configuração SAT - {self.loja.nome_fantasia}'