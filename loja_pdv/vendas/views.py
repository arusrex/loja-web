from django.shortcuts import render

def vendas(request):
    return render(request, 'pages/vendas.html')
