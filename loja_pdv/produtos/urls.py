from django.urls import path
from .views import *

app_name = 'produtos'

urlpatterns = [
    path('produtos/', produtos, name='produtos'),
]
