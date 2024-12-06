from django.urls import path
from .views import *

app_name = 'vendas'

urlpatterns = [
    path('gestao_vendas/', vendas, name='vendas'),
    path('alterar_venda/<int:venda_id>/', alterar_venda, name='alterar_venda'),
    path('excluir_venda/<int:venda_id>/', excluir_venda, name='excluir_venda'),
    path('pdv/', pdv, name='pdv'),
    path('adicionar/<int:produto_id>/', adicionar, name='adicionar'),
    path('remover/<int:item_id>/', remover, name='remover'),
    # path('finalizar/', finalizar, name='finalizar'),
]
