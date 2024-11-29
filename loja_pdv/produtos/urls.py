from django.urls import path
from .views import *

app_name = 'produtos'

urlpatterns = [
    path('gestao-produtos/', produtos, name='produtos'),
    path('edit_produtos/<int:id>/', edit_produto, name="edit_produto"),
    path('delete_produto/<int:id>/', delete_produto, name="delete_produto"),
]
