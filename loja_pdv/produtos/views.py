from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
import logging

log = logging.getLogger()

def produtos(request):
    return form_produtos(request)

def form_produtos(request, id=None, action=None):
    objs = Produto.objects.all().order_by('nome')
    form = ProdutoForm(request.POST or None)
    produto = None

    if action == 'edit_produto':
        produto = Produto.objects.get(id=id)
        form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Produto registrado com sucesso')
        log.info('Produto registrado com sucesso')
        return redirect('produtos:produtos')
    else:
        log.error('Produto não registrado')

    context = {
        'objs': objs,
        'form': form,
        'produto': produto,
        'action': action,
    }

    return render(request, 'pages/produtos.html', context)
