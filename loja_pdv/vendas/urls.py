from django.urls import path
from .views import *

app_name = 'vendas'

urlpatterns = [
    path('gestao_vendas/', vendas, name='vendas'),
]
