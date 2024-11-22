from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
import logging

log = logging.getLogger(__name__)


def clientes(request):
    return form_clientes(request)

def edit_cliente(request, id, tipo_cliente):
    return form_clientes(request, id=id, tipo_cliente=tipo_cliente, is_edit=True)

def form_clientes(request, id=None, tipo_cliente='1', is_edit=False):
    cliente = None

    if not is_edit:
        tipo_cliente = request.GET.get('tipo-pessoa', '1')
    
    if tipo_cliente == '1':
        objs = PessoaFisica.objects.all().order_by('nome')
        form = PessoaFisicaForm(request.POST or None)
        # obj = PessoaFisica()
        # campos = [field.name for field in obj._meta.get_fields()] # type: ignore
        if is_edit:
            cliente = PessoaFisica.objects.get(id=id)
            form = PessoaFisicaForm(request.POST or None, instance=cliente)
            print(f'edit fisico: {cliente}')

    elif tipo_cliente == '2':
        objs = PessoaJuridica.objects.all().order_by('razao_social')
        form = PessoaJuridicaForm(request.POST or None)
        # obj = PessoaJuridica()
        # campos = [field.name for field in obj._meta.get_fields()] # type: ignore
        if is_edit:
            cliente = PessoaJuridica.objects.get(id=id)
            form = PessoaJuridicaForm(request.POST or None, instance=cliente)
            print(f'edit juridico: {cliente}')

    else:
        return redirect('clientes:clientes')

    if request.method == 'POST' and request.POST.get('btn-form') and is_edit:
        print(f'entrou no post edit: {cliente}')
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente editado com sucesso')
            log.info('Cliente editado com sucesso')
            return redirect('clientes:edit_user', id=cliente.id) # type: ignore
    
    if request.method == 'POST' and not is_edit:
        print('entrou no post new')
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente registrado com sucesso')
            log.info('Cliente registrado com sucesso')
            return redirect('clientes:clientes')

    context = {
        'form': form,
        'objs': objs,
        'tipo_cliente': tipo_cliente,
        'is_edit': is_edit,
        'cliente': cliente,
        # 'campos': campos,
    }

    return render(request, 'pages/clientes.html', context)

def delete_cliente(request, id):
    tipo_cliente = request.GET.get('tipo_pessoa', '1')
    cliente = PessoaFisica.objects.get(id=id)
    if tipo_cliente == '2':
        cliente = PessoaJuridica.objects.get(id=id)
        cliente.delete()
        messages.success(request, f'Cliente {cliente.nome_fantasia} excluído com sucesso')
        log.info('Cliente pessoa jurídica excluída com sucesso')
        return redirect('cliente:clientes')
    else:
        cliente.delete()
        messages.success(request, f'Cliente {cliente.nome} excluído com sucesso')
        log.info(f'Cliente {cliente.nome} excluído com sucesso')
        return redirect('clientes:clientes')
