from django.urls import path
from .views import *

app_name = 'clientes'

urlpatterns = [
    path('clientes/', clientes, name='clientes'),
]
