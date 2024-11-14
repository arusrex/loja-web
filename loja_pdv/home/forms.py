from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *
from django.core.exceptions import ValidationError

class DadosLojaForm(forms.ModelForm):
    class Meta:
        model = DadosLoja
        fields = '__all__'

    def clean_cnpj(self):
        cnpj = self.cleaned_data["cnpj"]
        
        if cnpj:
            if len(cnpj) != 14:
                raise ValidationError('O CNPJ preciso conter exatamente 14 dígitos')
            elif not cnpj.isdigit():
                raise ValidationError('Digite apenas números')

        return cnpj
    
    def clean_ie(self):
        ie = self.cleaned_data["inscricao_estadual"]
        
        if ie:
            if len(ie) != 14:
                raise ValidationError('A Inscrição Estadual precisa conter exatamente 14 dígitos')
            elif not ie.isdigit():
                raise ValidationError('Digite apenas números')

        return ie
    

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']

class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']