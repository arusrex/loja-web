from django.shortcuts import render, redirect
from vendas.models import *
from produtos.models import *

def vendas(request):
    objs = Venda.objects.all().order_by('-id')
    context = {
        'vendas': objs,
    }
    return render(request, 'pages/vendas.html', context)

def pdv(request):
    venda = Venda.objects.filter(finalizada=False).first()
    produtos = Produto.objects.all().order_by('nome')
    context = {
        'venda': venda,
        'produtos': produtos,
    }
    return render(request, 'pages/pdv.html', context)

def adicionar(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    venda, created = Venda.objects.get_or_create(
        finalizada=False
    )
    
    if request.method == 'POST':
        quantidade = request.POST.get('quantidade')
        subtotal = int(quantidade) * produto.preco

        item, item_created = ItemVenda.objects.get_or_create(
            venda=venda,
            produto=produto,
            quantidade=quantidade,
            subtotal=subtotal
        )

        if not item_created:
            item.quantidade += 1
            item.save()
        
        return redirect('vendas:pdv')
        

def remover(request, item_id):
    ...

def finalizar(request):
    ...