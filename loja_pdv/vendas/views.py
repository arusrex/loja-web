from django.shortcuts import render, redirect
from vendas.models import *
from produtos.models import *

def vendas(request):
    objs = Venda.objects.all().order_by('-id')
    context = {
        'vendas': objs,
    }
    return render(request, 'pages/vendas.html', context)

def calcular_subtotal(quantidade, preco_unitario):
    subtotal = quantidade * preco_unitario
    return subtotal

def pdv(request):
    venda = Venda.objects.filter(finalizada=False).first()
    produtos = Produto.objects.all().order_by('nome')

    for item in venda.itens.all():
        venda.total += item.subtotal

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
        item_venda = venda.itens.filter(produto=produto).first()
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
        if i.id == item_id:
            i.delete()
    return redirect('vendas:pdv')

def finalizar(request):
    ...