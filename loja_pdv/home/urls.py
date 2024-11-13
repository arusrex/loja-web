from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('home/', home, name="home"),

    path('dados_loja/', dados_loja, name="dados_loja"),

    path('dados_fiscais/<int:id>/', dados_fiscais, name="dados_fiscais")

]
