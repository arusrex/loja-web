from django.db import models
from clientes.models import PessoaFisica, PessoaJuridica

def get_default_pessoa_juridica():
    return PessoaJuridica.objects.get_or_create(
        codigo= "consjur",
        defaults={
            "nome_fantasia": "Consumidor",
            "razao_social": "Consumidor",
            "cnpj": "12345678901234",
            "inscricao_estadual": "12345678901234",
            "estado": "SP",
        })[0].id

def get_default_pessoa_fisica():
    return PessoaFisica.objects.get_or_create(
        codigo= "consfis",
        defaults={
            "nome": "Consumidor",
            "estado": "SP",
        })[0].id

class Venda(models.Model):
    cliente_pessoa_fisica = models.ForeignKey(PessoaFisica, on_delete=models.SET_DEFAULT, default=get_default_pessoa_fisica)
    cliente_pessoa_juridica = models.ForeignKey(PessoaJuridica, on_delete=models.SET_DEFAULT, default=get_default_pessoa_juridica)
    
