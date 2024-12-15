from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from vendas.models import Venda
import logging


log = logging.getLogger(__name__)

@login_required
def home(request):
    vendas = Venda.objects.all().order_by('-id')[:10]
    vendas_total = []
    for venda in vendas:
        vendas_total.append(float(venda.total))
    context = {
        'vendas': vendas,
        'vendas_total': vendas_total,
    }

    return render(request, 'pages/index.html', context)

@login_required
def dados_loja(request):
    dados = DadosLoja.objects.first() or None
    
    if request.method == 'POST':
        form = DadosLojaForm(request.POST, request.FILES, instance=dados)

        if form.is_valid():
            form.save()
            messages.success(request, 'Dados da empresa salvos !')
            log.info('Dados da empresa salvos')
            return redirect('home:dados_loja')
        else:
            messages.error(request, 'Erro ao salvar !')
            log.error(f'Erro ao salvar os dados da empresa: {form.errors}')
    else:
        form = DadosLojaForm(instance=dados)

    context = {
        'form': form,
        'dados': dados,
    }

    return render(request, 'pages/dados_loja.html', context)

@login_required
def users(request):
    return user_form(request)

@login_required
def edit_user(request, id):
    action = 'edit_user'
    return user_form(request, id, action)

@login_required
def edit_user_password(request, id):
    action = 'edit_user_password'
    return user_form(request, id, action)

@login_required
def user_form(request, user_id=None, action=None):

    all_users = User.objects.all().order_by('first_name')

    if user_id and action == 'edit_user':
        log.info('Entrou em editar usuário')
        user_data = User.objects.get(id=user_id)
        form = EditUserForm(request.POST or None, instance=user_data)
    elif user_id and action == 'edit_user_password':
        log.info('Entrou em alterar senha')
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
        'all_users': all_users,
        'action': action,
    }

    return render(request, 'pages/users.html', context)

@login_required
def delete_user(request, user_id):
    user_data = User.objects.get(id=user_id)
    user_data.delete()
    messages.success(request, f'Usuário {user_data.get_full_name()} excluído')
    log.info(f'Usuário {user_data.get_full_name()} excluído')
    return redirect('home:users')

def entrar(request):
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['senha']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Bom trabalho, {user.get_full_name()}')
            return redirect('home:home')
        else:
            messages.error(request, 'Credenciais inválidas')
            return redirect('home:entrar')
        

    return render(request, 'pages/login.html')

@login_required
def sair(request):
    logout(request)
    return redirect('home:entrar')
