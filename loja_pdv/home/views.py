from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
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

def dados_fiscais(request):
    cfop_objs = CFOP.objects.all().order_by('-id')
    cst_csosn_objs = CST_CSOSN.objects.all().order_by('-id')
    unidades = Unidades.objects.all().order_by('-id')

    if request.POST.get('submit') == 'cfop_form':
        form_cfop = CFOPForm(request.POST)
        if form_cfop.is_valid():
            form_cfop.save()
            messages.success(request, 'CFOP salvo')
            log.info('CFOP registrado no sistema')
            return redirect('home:dados_fiscais')
        else:
            messages.error(request, 'Erro ao salvar CFOP')
            log.error(f'Erro ao salvar CFOP: {form_cfop.errors}')

    elif request.POST.get('submit') == 'cst_csosn_form':
        form_cst_csosn = CST_CSOSNForm(request.POST)
        if form_cst_csosn.is_valid():
            form_cst_csosn.save()
            messages.success(request, 'CST CSOSN salvo')
            log.info('CST CSOSN registrado no sistema')
            return redirect('home:dados_fiscais')
        else:
            messages.error(request, 'Erro ao salvar CST CSOSN')
            log.error(f'Erro ao salvar CFOP: {form_cst_csosn.errors}')

    elif request.POST.get('submit') == 'unidades_form':
        form_unidades = UnidadesForm(request.POST)
        if form_unidades.is_valid():
            form_unidades.save()
            messages.success(request, 'Unidades salvo')
            log.info('Unidades registrado no sistema')
            return redirect('home:dados_fiscais')
        else:
            messages.error(request, 'Erro ao salvar Unidades')
            log.error(f'Erro ao salvar CFOP: {form_unidades.errors}')
    
    form_cfop = CFOPForm()
    form_cst_csosn = CST_CSOSNForm()
    form_unidades = UnidadesForm()

    context = {
        'form_cfop': form_cfop,
        'form_cst_csosn': form_cst_csosn,
        'form_unidades': form_unidades
    }

    return render(request, 'pages/dados_fiscais.html', context)
