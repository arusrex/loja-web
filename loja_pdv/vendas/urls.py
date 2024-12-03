from django.urls import path
from .views import *

app_name = 'vendas'

urlpatterns = [
    path('gestao_vendas/', vendas, name='vendas'),
    path('pdv/', pdv, name='pdv'),
    path('adicionar/<int:produto_id>/', adicionar, name='adicionar'),
    # path('remover/<int:item_id>/', remover, name='remover'),
    # path('finalizar/', finalizar, name='finalizar'),
]
