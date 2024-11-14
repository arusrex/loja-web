from django import forms
from .models import *
from django.core.exceptions import ValidationError

class PessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = '__all__'

    def clean_cpf(self):
        cpf = self.cleaned_data["cpf"]
        
        if cpf:
            if len(cpf) != 11:
                raise ValidationError('O CPF é comsposto por 11 dígitos')
            elif not cpf.isdigit():
                raise ValidationError('Digite apenas números')

        return cpf
        
class PessoaJuridicaForm(forms.ModelForm):
    class Meta:
        model = PessoaJuridica
        fields = '__all__'

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get("cnpj")

        if cnpj:
            if len(cnpj) != 14:
                raise ValidationError('O CNPJ é composto por 14 dígitos')
            elif not cnpj.isdigit():
                raise ValidationError('Digite apenas números')
        
        return cnpj
    
    def clean_ie(self):
        ie = self.cleaned_data.get('inscricao_estadual')

        if ie:
            if len(ie) != 14:
                raise ValidationError('A Inscrição Estadual é composta por 14 dígitos')
            elif not ie.isdigit():
                raise ValidationError('Digite apenas números')
            
        return ie
    
