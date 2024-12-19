from django.urls import path
from .views import *
from sat_nfe.report import imprimir_comprovante

app_name = 'vendas'

urlpatterns = [
    path('gestao_vendas/', vendas, name='vendas'),
    path('alterar_venda/<int:venda_id>/', alterar_venda, name='alterar_venda'),
    path('excluir_venda/<int:venda_id>/', excluir_venda, name='excluir_venda'),
    path('pdv/', pdv, name='pdv'),
    path('aplicar_desconto/', aplicar_desconto, name='aplicar_desconto'),
    path('adicionar_cliente/<int:cliente_id>/', adicionar_cliente, name='adicionar_cliente'),
    path('altera_cliente/<int:cliente_id>/', alterar_cliente, name='alterar_cliente'),
    path('adicionar/<int:produto_id>/', adicionar, name='adicionar'),
    path('remover/<int:item_id>/', remover, name='remover'),
    path('finalizar/', finalizar, name='finalizar'),
    path('imprimir_comprovante/<int:venda_id>/', imprimir_comprovante, name='imprimir_comprovante'),
]
