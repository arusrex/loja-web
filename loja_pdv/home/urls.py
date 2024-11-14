from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', home, name="home"),
    # DADOS DA LOJA
    path('dados_loja/', dados_loja, name="dados_loja"),
    # USUÁRIOS
    path('users/<int:id>/', users, name='users'),
    path('delete_users/<int:id>', delete_user, name="delete_user")
]
