from django import forms
from .models import *
from django.core.exceptions import ValidationError

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

    def clean_ncm(self):
        ncm = self.cleaned_data["ncm"]

        if len(ncm) != 8:
            raise ValidationError("O campo NCM deve ter 8 caracteres")
        elif not ncm.isdigit():
            raise ValidationError("O campo NCM deve conter apenas números")
        
        return ncm
    
    def clean_ean(self):
        ean = self.cleaned_data['ean']
        if ean:
            if not ean.isdigit():
                raise ValidationError("O campo EAN deve conter apenas números")

        return ean
    