from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
import logging

log = logging.getLogger(__name__)

def clientes(request):
    objs = PessoaFisica.objects.all().order_by('nome')
    form = PessoaFisicaForm(request.POST or None)
    tipo_cliente = request.POST.get('tipo-pessoa', '1')

    if tipo_cliente == '2':
        objs = PessoaJuridica.objects.all().order_by('razao_social')
        form = PessoaJuridicaForm(request.POST or None)


    if request.method == 'POST' and request.POST.get('btn-form') and form.is_valid():
        form.save()
        messages.success(request, 'Cliente registrado com sucesso')
        log.info('Cliente registrado com sucesso')
        return redirect('clientes:clientes')

    context = {
        'objs': objs,
        'form': form,
        'tipo_cliente': tipo_cliente,
    }

    return render(request, 'pages/clientes.html', context)


def form_clientes(request, id=None, action=None):
    ...
