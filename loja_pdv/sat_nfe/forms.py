from .models import *
from django import forms
from django.core.exceptions import ValidationError

class ConfiguracaoSATForm(forms.ModelForm):
    class Meta:
        model = ConfiguracaoSAT
        fields = '__all__'

        widgets = {
            'caminho': forms.TextInput(),
        }
    
    def clean_codigo_ativacao(self):
        codigo_ativacao = self.cleaned_data['codigo_ativacao']

        if len(codigo_ativacao) > 16:
            raise ValidationError('O código de ativação deve ter no máximo 16 caracteres')
        
        return codigo_ativacao