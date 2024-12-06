from django.shortcuts import render, redirect
from vendas.models import *
from produtos.models import *

def vendas(request):
    vendas = Venda.objects.all().order_by('-id')

    for venda in vendas:
        for item in venda.itens.all(): # type: ignore
            venda.total += item.subtotal

    context = {
        'vendas': vendas,
    }
    return render(request, 'pages/vendas.html', context)

def alterar_venda(request, venda_id):
    return redirect('vendas:vendas')

def excluir_venda(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    venda.delete()

    return redirect('vendas:vendas')

def calcular_subtotal(quantidade, preco_unitario):
    subtotal = quantidade * preco_unitario
    return subtotal

def pdv(request):
    venda = Venda.objects.filter(finalizada=False).first()
    produtos = Produto.objects.all().order_by('nome')

    for item in venda.itens.all(): # type: ignore
        venda.total += item.subtotal # type: ignore

    context = {
        'venda': venda,
        'produtos': produtos,
    }
    return render(request, 'pages/pdv.html', context)

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
    return redirect('vendas:pdv')

def finalizar(request):
    ...