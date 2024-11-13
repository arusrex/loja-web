from django.urls import path
from .views import *

app_name = 'vendas'

urlpatterns = [
    path('vendas/', vendas, name='vendas'),
]
