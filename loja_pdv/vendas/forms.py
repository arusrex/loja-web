from .models import *
from django import forms

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'