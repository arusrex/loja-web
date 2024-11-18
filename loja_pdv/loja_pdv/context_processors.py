from home.models import DadosLoja

def dados_gerais(request):
    try:
        dados_loja = DadosLoja.objects.first()
    except DadosLoja.DoesNotExist:
        dados_loja = None

    context = {
        'dados_loja': dados_loja,
    }

    return context

    