from django.urls import path
from .views import *
from sat_nfe.report import *

app_name = 'sat_nfe'

urlpatterns = [
    path('sat_nfe/', sat_nfe, name='sat_nfe'),
    path('config_sat/', config_sat, name="config_sat"),
    path('gerar_sat/<int:venda_id>/', gerar_sat, name="gerar_sat"),
    path('imprimir_comprovante/<int:venda_id>/', imprimir_sat, name="imprimir_sat"),

]
