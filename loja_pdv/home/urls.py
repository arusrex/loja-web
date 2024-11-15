from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', home, name="home"),
    # DADOS DA LOJA
    path('dados_loja/', dados_loja, name="dados_loja"),
    # USUÁRIOS
    path('users/', users, name='users'),
    path('edit_user/<int:id>/', edit_user, name='edit_user'),
    path('edit_user_password/<int:id>/', edit_user_password, name='edit_user_password'),
    path('delete_users/<int:id>', delete_user, name="delete_user")
]
