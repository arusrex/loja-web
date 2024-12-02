from django.db import models
from clientes.models import Cliente
from produtos.models import Produto

def get_default_cliente():
    return Cliente.objects.get_or_create(
        codigo= "cons001",
        defaults={
            "nome": "Consumidor",
            "razao_social": "Consumidor",
        })[0].id # type: ignore

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_DEFAULT, default=get_default_cliente)
    data = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0) # type: ignore
    desconto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0) # type: ignore
    finalizada = models.BooleanField(default=False)

    def calcular_total(self):
        total_itens = sum(item.subtotal_com_desconto() for item in self.itens.all()) # type: ignore
        return total_itens - self.desconto_total
    
    def __str__(self):
        return f'Venda {self.id} - {self.data}' # type: ignore

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0) # type: ignore

    def subtotal(self):
        return self.quantidade * self.preco_unitario
    
    def subtotal_com_desconto(self):
        return self.subtotal() - self.desconto # type: ignore
    
    def __str__(self):
        return f'{self.produto.nome} (x {self.quantidade})'
    