from django.urls import path
from .views import *

app_name = 'sat_nfe'

urlpatterns = [
    path('sat_nfe/', sat_nfe, name='sat_nfe'),
]
