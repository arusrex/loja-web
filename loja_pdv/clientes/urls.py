from django.urls import path
from .views import *

app_name = 'clientes'

urlpatterns = [
    path('gestao_clientes/', clientes, name='clientes'),
    path('edit_cliente/<int:id>/<str:tipo_cliente>/', edit_cliente, name="edit_cliente"),
    path('delete_cliente/<int:id>/<str:tipo_cliente>/', delete_cliente, name="delete_cliente"),
]
