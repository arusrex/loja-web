from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from vendas.models import *
import random
import ctypes
import xml.etree.ElementTree as ET
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pathlib import Path

@login_required
def sat_nfe(request):
    return render(request, 'pages/sat_nfe.html')

@login_required
def config_sat(request):
    config = ConfiguracaoSAT.objects.first()
    form = ConfiguracaoSATForm(request.POST or None, instance=config)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Configurações salvas com sucesso!')
        return redirect('sat_nfe:config_sat')

    context = {
        'config': config,
        'form': form,
    }

    return render(request, 'pages/config_sat.html', context)

def enviar_dados_simulados(request, xml_venda, numeroSessao, venda_id):
    venda = Venda.objects.get(id=venda_id)

    eeeee = f'06000'
    cccc = f'{random.randint(1000, 9999)}'
    mensagem = 'Emitido com sucesso + conteúdo notas.'
    cod = f'{random.randint(100, 999)}'
    mensagem_sefaz = 'Autorizado o uso do CFe'
    arquivoCFeBase64 = 'ExemploCFeBase64.txt...'
    timeStamp = '20110101170101'
    chaveConsulta = '35111202767579000148598583801050151865833992'
    valorTotalCFe = f'{venda.total}'
    CPFCNPJValue = f'{random.randint(10000000000, 99999999999)}'
    assinaturaQRCODE = 'ExemploAssinaturaQRCODE.txt...'

    retorno = [
        f'{numeroSessao}',
        eeeee,
        cccc,
        mensagem,
        cod,
        mensagem_sefaz,
        arquivoCFeBase64,
        timeStamp,
        chaveConsulta,
        valorTotalCFe,
        CPFCNPJValue,
        assinaturaQRCODE,
    ]
    
    if eeeee == retorno[1]:
        venda.numeroSessao = numeroSessao
        venda.eeeee = eeeee
        venda.cccc = cccc
        venda.mensagem = mensagem
        venda.cod = cod
        venda.mensagem_sefaz = mensagem_sefaz
        venda.arquivoCFeBase64 = arquivoCFeBase64
        venda.timeStamp = timeStamp
        venda.chaveConsulta = chaveConsulta
        venda.valorTotalCFe = valorTotalCFe
        venda.CPFCNPJValue = CPFCNPJValue
        venda.assinaturaQRCODE = assinaturaQRCODE
        venda.retornoSAT = '|'.join(retorno)
        venda.save()
        messages.success(request, 'CFe - SAT emitido com sucesso!')
    else:
        messages.error(request, f'Erro ao emitir CFe - SAT: {mensagem}')

    return redirect('vendas:vendas')

def enviar_dados_sat_real(request, xml_venda, numeroSessao, venda_id):
    venda = Venda.objects.get(id=venda_id)
    configuracao_sat = ConfiguracaoSAT.objects.first()

    if configuracao_sat:
        literal_caminho = configuracao_sat.caminho
        print(literal_caminho)
        # caminho = literal_caminho.replace('\\', '/') if literal_caminho else 'C:/Program Files (x86)/SAT/SAT.dll'
        caminho = (
            Path(literal_caminho).as_posix() if literal_caminho and Path(literal_caminho).exists()
            else 'C:/Program Files (x86)/SAT/SAT.dll'
        )
        print(caminho)
    else:
        caminho = 'C:/Program Files (x86)/SAT/SAT.dll'

    sat = ctypes.CDLL(caminho)
    retorno = sat.EnviarDadosVenda(numeroSessao.encode(), xml_venda.encode())

    retorno_str = ctypes.string_at(retorno).decode("utf-8")
    retorno_parts = retorno_str.split("|")

    nroSessao = retorno_parts[0]
    eeeee = retorno_parts[1]
    cccc = retorno_parts[2]
    mensagem = retorno_parts[3]
    cod = retorno_parts[4]
    mensagem_sefaz = retorno_parts[5]
    arquivoCFeBase64 = retorno_parts[6]
    timeStamp = retorno_parts[7]
    chaveConsulta = retorno_parts[8]
    valorTotalCFe = retorno_parts[9]
    CPFCNPJValue = retorno_parts[10]
    assinaturaQRCODE = retorno_parts[11]

    if eeeee == '06000':
        venda.numeroSessao = int(nroSessao)
        venda.eeeee = eeeee
        venda.cccc = cccc
        venda.mensagem = mensagem
        venda.cod = cod
        venda.mensagem_sefaz = mensagem_sefaz
        venda.arquivoCFeBase64 = arquivoCFeBase64
        venda.timeStamp = timeStamp
        venda.chaveConsulta = chaveConsulta
        venda.valorTotalCFe = valorTotalCFe
        venda.CPFCNPJValue = CPFCNPJValue
        venda.assinaturaQRCODE = assinaturaQRCODE
        venda.retornoSAT = retorno_str
        venda.save()
        messages.success(request, 'CFe - SAT emitido com sucesso!')
    else:
        messages.error(request, f'Erro ao emitir CFe - SAT: {mensagem}')

    return redirect('vendas:vendas')

def enviar_dados_sat(request, xml_venda, numeroSessao, venda_id):
    SAT_SIMULADO  = ConfiguracaoSAT.objects.first()

    if SAT_SIMULADO and SAT_SIMULADO.teste:
        return enviar_dados_simulados(request, xml_venda, numeroSessao, venda_id)
        
    else:
        return enviar_dados_sat_real(request, xml_venda, numeroSessao, venda_id)

def gerar_xml_venda(venda):

    loja = DadosLoja.objects.first()
    cfe = ET.Element("CFe")
    inf_cfe = ET.SubElement(cfe, "infCFe", {"versao": "0.08"})

    # Identificação da loja
    emit = ET.SubElement(inf_cfe, "emit")
    ET.SubElement(emit, "CNPJ").text = loja.cnpj # type: ignore
    ET.SubElement(emit, "IE").text = loja.inscricao_estadual # type: ignore
    ET.SubElement(emit, "xNome").text = loja.razao_social # type: ignore
    ET.SubElement(emit, "xFant").text = loja.nome_fantasia # type: ignore
    ET.SubElement(emit, "enderEmit").extend([
        ET.Element("xLgr", text=loja.endereco), # type: ignore
        ET.Element("xBairro", text=loja.bairro), # type: ignore
        ET.Element("CEP", text=loja.cep), # type: ignore
        ET.Element("xMun", text=loja.cidade), # type: ignore
        ET.Element("UF", text=loja.estado) # type: ignore
    ])

    if venda.cliente:
        # Identificação do consumidor
        dest = ET.SubElement(inf_cfe, "dest")
        if venda.cliente.cnpj:
            ET.SubElement(dest, "CNPJ").text = venda.cliente.cnpj
        elif venda.cliente.cpf:
            ET.SubElement(dest, "CPF").text = venda.cliente.cpf
        ET.SubElement(dest, "xNome").text = venda.cliente.nome
    else:
        dest = ET.SubElement(inf_cfe, "dest")
        ET.SubElement(dest, "xNome").text = 'Consumidor'

    # Dados da venda
    total_venda = 0
    for idx, item in enumerate(venda.itens.all(), start=1):
        det = ET.SubElement(inf_cfe, "det", {"nItem": str(idx)})

        # Informações do produto
        prod = ET.SubElement(det, "prod")
        ET.SubElement(prod, "cProd").text = item.produto.codigo
        ET.SubElement(prod, "xProd").text = item.produto.nome
        ET.SubElement(prod, "CFOP").text = item.produto.cfop
        ET.SubElement(prod, "uCom").text = item.produto.unidade
        ET.SubElement(prod, "qCom").text = f"{item.quantidade:.3f}"
        ET.SubElement(prod, "vUnCom").text = f"{item.produto.preco:.2f}"
        ET.SubElement(prod, "vProd").text = f"{item.quantidade * item.produto.preco:.2f}"
        ET.SubElement(prod, "cEAN").text = item.produto.ean or "SEM GTIN"
        ET.SubElement(prod, "NCM").text = item.produto.ncm

        # Impostos (ICMS, IPI, PIS, COFINS)
        imposto = ET.SubElement(det, "imposto")
        v_item = item.quantidade * item.produto.preco

        # ICMS
        icms = ET.SubElement(imposto, "ICMS")
        icms_det = ET.SubElement(icms, "ICMS00")
        ET.SubElement(icms_det, "orig").text = "0"  # Origem do produto (ajustar conforme necessário)
        ET.SubElement(icms_det, "CST").text = item.produto.cst or "00"
        ET.SubElement(icms_det, "modBC").text = "3"  # Base de cálculo
        ET.SubElement(icms_det, "vBC").text = f"{v_item:.2f}"  # Valor base de cálculo
        ET.SubElement(icms_det, "pICMS").text = f"{item.produto.icms:.2f}" if item.produto.icms else "0.00"
        ET.SubElement(icms_det, "vICMS").text = f"{(v_item * (item.produto.icms or 0) / 100):.2f}"

        # IPI
        ipi = ET.SubElement(imposto, "IPI")
        ipi_det = ET.SubElement(ipi, "IPITrib")
        ET.SubElement(ipi_det, "CST").text = "50"  # Código padrão (ajustar conforme necessário)
        ET.SubElement(ipi_det, "vBC").text = f"{v_item:.2f}"
        ET.SubElement(ipi_det, "pIPI").text = f"{item.produto.ipi:.2f}" if item.produto.ipi else "0.00"
        ET.SubElement(ipi_det, "vIPI").text = f"{(v_item * (item.produto.ipi or 0) / 100):.2f}"

        # PIS
        pis = ET.SubElement(imposto, "PIS")
        pis_det = ET.SubElement(pis, "PISAliq")
        ET.SubElement(pis_det, "CST").text = "01"  # Código padrão (ajustar conforme necessário)
        ET.SubElement(pis_det, "vBC").text = f"{v_item:.2f}"
        ET.SubElement(pis_det, "pPIS").text = f"{item.produto.pis:.2f}" if item.produto.pis else "0.00"
        ET.SubElement(pis_det, "vPIS").text = f"{(v_item * (item.produto.pis or 0) / 100):.2f}"

        # COFINS
        cofins = ET.SubElement(imposto, "COFINS")
        cofins_det = ET.SubElement(cofins, "COFINSAliq")
        ET.SubElement(cofins_det, "CST").text = "01"  # Código padrão (ajustar conforme necessário)
        ET.SubElement(cofins_det, "vBC").text = f"{v_item:.2f}"
        ET.SubElement(cofins_det, "pCOFINS").text = f"{item.produto.cofins:.2f}" if item.produto.cofins else "0.00"
        ET.SubElement(cofins_det, "vCOFINS").text = f"{(v_item * (item.produto.cofins or 0) / 100):.2f}"

        # Acumular total da venda
        total_venda += v_item
        
    total_com_desconto = total_venda - venda.desconto_total

    desconto = ET.SubElement(inf_cfe, "desconto")
    ET.SubElement(desconto, "vDesc").text = f"{venda.desconto_total:.2f}"
    
    # Totalização
    total = ET.SubElement(inf_cfe, "total")
    ET.SubElement(total, "vCFe").text = f"{total_com_desconto:.2f}"
    
    met_pgto = venda.metodo_pagamento if venda.metodo_pagamento else '01'

    # Pagamento (Exemplo: pagamento em dinheiro)
    pgto = ET.SubElement(inf_cfe, "pgto")
    ET.SubElement(pgto, "MP").text = met_pgto # Código para dinheiro
    ET.SubElement(pgto, "vMP").text = f"{total_com_desconto:.2f}"

    return ET.tostring(cfe, encoding="utf-8").decode("utf-8")
    
def gerar_sat(request, venda_id):
    configuracao = ConfiguracaoSAT.objects.first()
    venda = Venda.objects.get(id=venda_id)
    numeroSessao = random.randint(100000, 999999)

    if not configuracao:
        return JsonResponse({"status": "erro", "mensagem": "Configuração do SAT não encontrada."})

    try:
        xml = gerar_xml_venda(venda)
        return enviar_dados_sat(request, xml, numeroSessao, venda_id)

    except Exception as e:
        return JsonResponse({"status": "erro", "mensagem": str(e)})
