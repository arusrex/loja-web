from django.shortcuts import render

def produtos(request):
    return render(request, 'pages/produtos.html')
