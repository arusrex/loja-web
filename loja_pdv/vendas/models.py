from django.db import models
from clientes.models import Cliente
from produtos.models import Produto

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0) # type: ignore
    desconto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0) # type: ignore
    finalizada = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Venda {self.id} - {self.data}' # type: ignore

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.produto.nome} (x {self.quantidade})'
    