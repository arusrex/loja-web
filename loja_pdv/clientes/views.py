from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
import logging

log = logging.getLogger(__name__)

def clientes(request):
    return form_clientes(request)

def edit_cliente(request, id):
    return form_clientes(request, id=id, is_edit=True)

def form_clientes(request, id=None, is_edit=False):
    objs = Cliente.objects.all().order_by('nome')
    cliente = None

    if is_edit:
        cliente = Cliente.objects.get(id=id)
        form = ClienteForm(request.POST or None, instance=cliente)
    else:
        form = ClienteForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente registrado com sucesso! ✅')
            log.info('Cliente registrado com sucesso!')
            return redirect('clientes:clientes')
        else:
            messages.error(request, 'Erro ao registrar cliente! ⛔')
            log.error('Erro ao registrar cliente!')
        
    context = {
        'form': form,
        'objs': objs,
        'is_edit': is_edit,
        'cliente': cliente,
    }

    return render(request, 'pages/clientes.html', context)

def delete_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    messages.success(request, f'Cliente {cliente.nome} excluído com sucesso')
    log.info('Cliente excluído com sucesso')
    return redirect('clientes:clientes')
