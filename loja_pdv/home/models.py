from django.db import models

ESTADOS_CHOICES = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), 
    ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), 
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), 
    ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), 
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), 
    ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), 
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
]

class CFOP(models.Model):

    codigo = models.CharField(max_length=4, unique=True)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.codigo} - {self.descricao}'

class CST_CSOSN(models.Model):

    codigo = models.CharField(max_length=3, unique=True)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.codigo} - {self.descricao}'

class Unidades(models.Model):

    codigo = models.CharField(max_length=2)
    descricao = models.CharField(max_length=100)

    def __str__(self) :
        return f'{self.codigo} - {self.descricao}'
    
class DadosLoja(models.Model):
    
    nome_fantasia = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    inscricao_municipal = models.CharField(max_length=50, blank=True, null=True)
    inscricao_estadual = models.CharField(max_length=50)
    inscricao_estadual_st = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=ESTADOS_CHOICES)
    fone = models.CharField(max_length=11, blank=True)
    email = models.EmailField(blank=True, null=True)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)

    def __str__(self):
        return f'{self.nome_fantasia}'

