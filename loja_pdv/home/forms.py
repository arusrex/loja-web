from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *
from django.core.exceptions import ValidationError

class DadosLojaForm(forms.ModelForm):
    class Meta:
        model = DadosLoja
        fields = '__all__'
    
        labels = {
            'nome_fantasia': 'Nome Fantasia',
            'razao_social': 'Razão Social',
            'cnpj': 'CNPJ',
            'inscricao_municipal': 'Inscrição Municipal',
            'inscricao_estadual': 'Inscrição Estadual',
            'inscricao_estadual_st': 'Inscrição Estadual ST',
            'inscricao_municipal': 'Inscrição Municipal',
            'endereco': 'Endereço',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'cep': 'CEP',
            'fone': 'Telefone',
            'email': 'E-mail',
            'logo': 'Logotipo'
        }

    def clean_cnpj(self):
        cnpj = self.cleaned_data["cnpj"]
        
        if cnpj:
            if len(cnpj) != 14:
                raise ValidationError('O CNPJ precisa conter exatamente 14 dígitos')
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
        labels = {
            'username': 'Nome de Usuário',
            'first_name': 'Primeiro Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
            'is_active': 'Ativo',
            'is_staff': 'Funcionário',
            'is_superuser': 'Superusuário',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].help_text = (
            '''
            <ul>
                <li><small>Obrigatório.</small></li>
                <li><small>150 caracteres ou menos.</small></li>
                <li><small>Letras, números e @/./+/-/_ apenas.</small></li>
            </ul>
            '''
        )

        self.fields['is_active'].help_text = (
            '<small>Marque para ativar usuário.</small>'
        )

        self.fields['is_staff'].help_text = (
            '<small>Marque para privilégios de funcionário.</small>'
        )

        self.fields['is_superuser'].help_text = (
            '<small>Marque para privilégios de Administrador.</small>'
        )

        self.fields['password1'].help_text = (
            '''
            <ul>
                <li><small>Sua senha não pode ser muito parecida com o resto das suas informações pessoais.</small></li>
                <li><small>Sua senha precisa conter pelo menos 8 caracteres.</small></li>
                <li><small>Sua senha não pode ser uma senha comumente utilizada.</small></li>
                <li><small>Sua senha não pode ser inteiramente numérica.</small></li>
            </ul>
            '''
        )

        self.fields['password2'].help_text = (
            '<small>Digite a senha novamente.</small>'
        )

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise ValidationError('E-mail já existe')
        
        return email

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']
        labels = {
            'username': 'Nome de Usuário',
            'first_name': 'Primeiro Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
            'is_active': 'Ativo',
            'is_staff': 'Funcionário',
            'is_superuser': 'Superusuário',
        }

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise ValidationError('Nome de Usuário já existe')
        
        return username

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise ValidationError('E-mail já existe')
        
        return email