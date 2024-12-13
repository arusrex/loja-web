from django.shortcuts import render, redirect
from vendas.models import *
from produtos.models import *
from clientes.models import *
from .forms import *

def vendas(request):
    vendas = Venda.objects.all().order_by('-id')

    if vendas:
        for venda in vendas:
            venda.calcula_total()

    context = {
        'vendas': vendas,
    }
    return render(request, 'pages/vendas.html', context)

def alterar_venda(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    # venda_aberta = Venda.objects.filter(finalizada=False).first()

    # if venda_aberta:
    #     venda_aberta.finalizada = True
    #     venda_aberta.save()
    
    if venda:
        venda.finalizada = False
        venda.save()

    return pdv(request, venda_id)

def excluir_venda(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    venda.delete()

    return redirect('vendas:vendas')

def calcular_subtotal(quantidade, preco_unitario):
    subtotal = quantidade * preco_unitario
    return subtotal


def pdv(request, venda_id=None):
    produtos = Produto.objects.all().order_by('nome')
    clientes = Cliente.objects.all().order_by('nome')

    if venda_id:
        venda = Venda.objects.get(id=venda_id)
    else:
        venda = Venda.objects.filter(finalizada=False).first()

    if not venda:
        venda = Venda.objects.create(
            finalizada=False,            
        )

    form = VendaForm(request.POST or None, instance=venda)
    met_pgto = request.GET.get('pgto')

    if met_pgto:
        venda.metodo_pagamento = met_pgto
        venda.save()
        return redirect('vendas:pdv')

    venda.calcula_total()

    context = {
        'form': form,
        'venda': venda,
        'produtos': produtos,
        'clientes': clientes,
    }
    return render(request, 'pages/pdv.html', context)

def adicionar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    venda = Venda.objects.filter(finalizada=False).first()

    if not venda:
        venda = Venda.objects.create(
            cliente=cliente,
            finalizada=False,
        )
    else:
        venda.cliente = cliente
        venda.save()
    
    return redirect('vendas:pdv')

def alterar_cliente(request, cliente_id):
    cliente_novo = Cliente.objects.get(id=cliente_id)
    venda = Venda.objects.filter(finalizada=False).first()

    if venda:
        venda.cliente = cliente_novo
        venda.save()

    return redirect('vendas:pdv')

def adicionar(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    venda = Venda.objects.filter(finalizada=False).first()

    if not venda:
        venda = Venda.objects.create(
            finalizada=False
        )
    
    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade'))
        item_venda = venda.itens.filter(produto=produto).first() # type: ignore
        if item_venda:
            item_venda.quantidade += quantidade
            item_venda.subtotal = calcular_subtotal(item_venda.quantidade, produto.preco)
            item_venda.save()
        else:
            item = ItemVenda.objects.create(
                venda=venda,
                produto=produto,
                quantidade=quantidade,
                subtotal=calcular_subtotal(quantidade, produto.preco)
            )
            
            item.save()
        
    return redirect('vendas:pdv')    

def remover(request, item_id):
    venda = Venda.objects.filter(finalizada=False).first()
    itens = ItemVenda.objects.filter(venda=venda)

    for i in itens:
        if i.id == item_id: # type: ignore
            i.delete()
    
    if venda:
        venda.save()

    return redirect('vendas:pdv')

def finalizar(request):
    venda = Venda.objects.filter(finalizada=False).first()

    if venda:
        venda.finalizada = True
        venda.save()

    return redirect('vendas:pdv')

def aplicar_desconto(request):
    venda = Venda.objects.filter(finalizada=False).first()

    if request.method == 'POST':
        desconto = request.POST.get('desconto')
        if venda:
            venda.desconto_total = desconto
            venda.save()
    
    return redirect('vendas:pdv')
