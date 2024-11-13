from django import forms
from .models import *

class DadosLojaForm(forms.ModelForm):
    class Meta:
        model = DadosLoja
        fields = '__all__'

class CFOPForm(forms.ModelForm):
    class Meta:
        model = CFOP
        fields = '__all__'

class CST_CSOSNForm(forms.ModelForm):
    class Meta:
        model = CST_CSOSN
        fields = '__all__'

class UnidadesForm(forms.ModelForm):
    class Meta:
        model = Unidades
        fields = '__all__'