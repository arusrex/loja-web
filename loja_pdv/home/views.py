from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
import logging


log = logging.getLogger(__name__)

def home(request):
    return render(request, 'pages/index.html')

def dados_loja(request):
    dados = DadosLoja.objects.first()
    
    if request.method == 'POST':
        form = DadosLojaForm(request.POST, instance=dados)

        if form.is_valid():
            form.save()
            messages.success(request, 'Dados da empresa salvos !')
            log.info('Dados da empresa salvos')
            return redirect('home:dados_loja')
        else:
            messages.error(request, 'Erro ao salvar !')
            log.error(f'Erro ao salvar os dados da empresa: {form.errors}')

    form = DadosLojaForm(instance=dados)

    context = {
        'form': form,
    }

    return render(request, 'pages/dados_loja.html', context)

def users(request):
    return user_form(request)

def edit_user(request, user_id, action='edit_user'):
    return user_form(request, user_id, action)

def edit_user_password(request, user_id, action='edit_user_password'):
    return user_form(request, user_id, action)

def user_form(request, user_id=None, action=None):

    all_users = User.objects.all().order_by('first_name')

    if user_id and action == 'edit_user':
        user_data = User.objects.get(id=user_id)
        form = EditUserForm(request.POST or None, instance=user_data)
    elif user_id and action == 'edit_user_password':
        user_data = User.objects.get(id=user_id)
        form = SetPasswordForm(user_data, request.POST or None)
    else:
        form = NewUserForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        if action == 'edit_user':
            messages.success(request, 'Usuário editado')
            log.info(f'Usuário {user_data.get_full_name()} editado com sucesso')
        elif action == 'edit_user_password':
            messages.success(request, 'Senha do usuário editada')
            log.info(f'Senha do usuário {user_data.get_full_name()} editada com sucesso')
        else:
            messages.success(request, 'Usuário criado')
            log.info(f'Usuário criado com sucesso')
        return redirect('home:users')
    
    context = {
        'form': form,
        'all_users': all_users
    }

    return render(request, 'pages/users.html', context)

def delete_user(request, user_id):
    user_data = User.objects.get(id=user_id)
    user_data.delete()
    messages.success(request, f'Usuário {user_data.get_full_name()} excluído')
    log.info(f'Usuário {user_data.get_full_name()} excluído')
    return redirect('home:users')

