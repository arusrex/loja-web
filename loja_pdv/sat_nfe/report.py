# type:ignore
from vendas.models import Venda
from home.models import DadosLoja
from django.shortcuts import redirect
import qrcode
import win32print
import win32ui
from PIL import Image, ImageWin
import os


def gerar_cupom_fiscal_com_qrcode(venda, xml):
    dados = xml.split('|')
    loja = DadosLoja.objects.first()
    largura_max = 40
    # Pegar a impressora padrão
    printer_name = win32print.GetDefaultPrinter()

    # Criar o QR Code
    chave_acesso = dados[8]
    valor_total_cfe = dados[9]
    time_stamp = dados[7]
    assinatura_qrcode = dados[11]
    url_consulta = "http://www.sefaz.sp.gov.br/qrcode"
    qr_code_text = f"{url_consulta}?p={chave_acesso}|{valor_total_cfe}|{time_stamp}|{assinatura_qrcode}"

    qr = qrcode.QRCode(version=1, box_size=5, border=2)
    qr.add_data(qr_code_text)
    qr.make(fit=True)

    # Salvar QR Code como imagem
    qr_image_path = "qr_code.bmp"
    qr.make_image(fill="black", back_color="white").save(qr_image_path)

    # Abrir a imagem do QR Code
    qr_image = Image.open(qr_image_path)

    # Configurar a impressora
    hprinter = win32print.OpenPrinter(printer_name)
    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(printer_name)

    hdc.StartDoc("Cupom Fiscal SAT")
    hdc.StartPage()

    # Definir a posição inicial (em pontos gráficos)
    start_x, start_y = 100, 100
    line_height = 100

    # Imprimir o cabeçalho como texto
    cupom_texto = [
        "----------------------------------------",
        "                CF-e SAT",
        f"    Numero de Serie: {dados[0]}",
        "----------------------------------------",
        f"{loja.nome_fantasia}",
        f"CNPJ: {loja.cnpj}",
        f"IE: {loja.inscricao_estadual}",
        f"End.: {loja.endereco} - {loja.cidade}",
        f"CEP: {loja.cep} - {loja.estado}",
        f"Telefone: {loja.fone}",
        "----------------------------------------",
        f"Data: {venda.data.strftime('%d/%m/%Y %H:%M')}",
        f"Venda Nº: {venda.id}",
        f"Cliente: {venda.cliente.razao_social if venda.cliente else 'Consumidor Final'}",
        f"CNPJ: {venda.cliente.cnpj if venda.cliente else '---'}",
        "----------------------------------------",
        "Itens:",
        "COD|PROD|QT|PREC|SUBT",
    ]

    for linha in cupom_texto:
        linhas_quebradas = quebra_linhas(linha, largura_max)
        for l in linhas_quebradas:
            hdc.TextOut(start_x, start_y, l)
            start_y += line_height

    # Imprimir os itens da venda
    for item in venda.itens.all():
        texto_item = f"{item.produto.codigo} {item.produto.nome[:30]} {item.quantidade} x {item.produto.preco:.2f} = {item.subtotal:.2f}"
        linhas_quebradas = quebra_linhas(texto_item, largura_max)
        for l in linhas_quebradas:
            hdc.TextOut(start_x, start_y, l)
            start_y += line_height

    # Total e descontos
    totais = [
        f"TOTAL: R$ {venda.total:.2f}",
        f"Desconto: R$ {venda.desconto_total:.2f}",
        f"TOTAL FINAL: R$ {venda.calcular_desconto():.2f}",
        f"PGTO: {venda.metodo_pagamento if venda.metodo_pagamento else " Dinheiro"}",
        f"----------------------------------------",
    ]

    for linha in totais:
        linhas_quebradas = quebra_linhas(linha, largura_max)
        for l in linhas_quebradas:
            hdc.TextOut(start_x, start_y, l)
            start_y += line_height

    posicao = (largura_max - -600) // 2
    
    # Inserir o QR Code
    dib = ImageWin.Dib(qr_image)
    dib.draw(hdc.GetHandleOutput(), (posicao, start_y, posicao + 800, start_y + 800))
    start_y += 950

    # Rodapé
    rodape = [
        "----------------------------------------",
         f"Consulta: {qr_code_text}",
        "----------------------------------------",
        "OBRIGADO PELA PREFERÊNCIA!",
    ]

    for linha in rodape:
        linhas_quebradas = quebra_linhas(linha, largura_max)
        for l in linhas_quebradas:
            hdc.TextOut(start_x, start_y, l)
            start_y += line_height

    # Finalizar a impressão
    hdc.EndPage()
    hdc.EndDoc()
    hdc.DeleteDC()
    win32print.ClosePrinter(hprinter)
    os.remove(qr_image_path)

def gerar_comprovante(venda):
    loja = DadosLoja.objects.first()
    largura_max = 40
    # Pegar a impressora padrão
    printer_name = win32print.GetDefaultPrinter()

    # Criar o QR Code
    qr_code_text = f"www.luelueletronicos.com.br"

    qr = qrcode.QRCode(version=1, box_size=5, border=2)
    qr.add_data(qr_code_text)
    qr.make(fit=True)

    # Salvar QR Code como imagem
    qr_image_path = "qr_code.bmp"
    qr.make_image(fill="black", back_color="white").save(qr_image_path)

    # Abrir a imagem do QR Code
    qr_image = Image.open(qr_image_path)

    # Configurar a impressora
    hprinter = win32print.OpenPrinter(printer_name)
    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(printer_name)

    hdc.StartDoc("Comprovante de Venda")
    hdc.StartPage()

    # Definir a posição inicial (em pontos gráficos)
    start_x, start_y = 100, 100
    line_height = 100

    # Imprimir o cabeçalho como texto
    cupom_texto = [
        "----------------------------------------",
        "           Comprovante de Venda",
        "              Sem valor fiscal",
        "----------------------------------------",
        f"{loja.nome_fantasia}",
        f"End.: {loja.endereco} - {loja.cidade}",
        f"Telefone: {loja.fone}",
        "----------------------------------------",
        f"Data: {venda.data.strftime('%d/%m/%Y %H:%M')}",
        f"Venda Nº: {venda.id}",
        f"Cliente: {venda.cliente.razao_social if venda.cliente else 'Consumidor Final'}",
        f"CNPJ: {venda.cliente.cnpj if venda.cliente else '---'}",
        "----------------------------------------",
        "Itens:",
        "PROD|QTD|PRECO|SUBTOTAL",
    ]

    for linha in cupom_texto:
        linhas_quebradas = quebra_linhas(linha, largura_max)
        for l in linhas_quebradas:
            hdc.TextOut(start_x, start_y, l)
            start_y += line_height

    # Imprimir os itens da venda
    for item in venda.itens.all():
        texto_item = f" {item.produto.nome[:30]} {item.quantidade} x {item.produto.preco:.2f} = {item.subtotal:.2f}"
        linhas_quebradas = quebra_linhas(texto_item, largura_max)
        for l in linhas_quebradas:
            hdc.TextOut(start_x, start_y, l)
            start_y += line_height 

    # Total e descontos
    totais = [
        f"TOTAL: R$ {venda.total:.2f}",
        f"Desconto: R$ {venda.desconto_total:.2f}",
        f"TOTAL FINAL: R$ {venda.calcular_desconto():.2f}",
        f"----------------------------------------",
    ]

    for linha in totais:
        linhas_quebradas = quebra_linhas(linha, largura_max)
        for l in linhas_quebradas:
            hdc.TextOut(start_x, start_y, l)
            start_y += line_height

    posicao = (largura_max - -600) // 2
    
    # Inserir o QR Code
    dib = ImageWin.Dib(qr_image)
    dib.draw(hdc.GetHandleOutput(), (posicao, start_y, posicao + 800, start_y + 800))
    start_y += (line_height + 950)

    # Rodapé
    rodape = [
        "----------------------------------------",
        "OBRIGADO PELA PREFERÊNCIA!",
    ]

    for linha in rodape:
        linhas_quebradas = quebra_linhas(linha, largura_max)
        for l in linhas_quebradas:
            hdc.TextOut(start_x, start_y, l)
            start_y += line_height

    # Finalizar a impressão
    hdc.EndPage()
    hdc.EndDoc()
    hdc.DeleteDC()
    win32print.ClosePrinter(hprinter)
    if qr_image_path:
        os.remove(qr_image_path)

def imprimir_sat(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    xml = venda.retornoSAT
    gerar_cupom_fiscal_com_qrcode(venda, xml)
    return redirect('vendas:vendas')

def imprimir_comprovante(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    gerar_comprovante(venda)
    return redirect('vendas:vendas')

def quebra_linhas(texto, largura_max):
    linhas = []
    while len(texto) > largura_max:
        corte = texto.rfind(" ", 0, largura_max)
        if corte == -1:
            corte = largura_max
        linhas.append(texto[:corte])
        texto = texto[corte:].strip()
    linhas.append(texto)
    return linhas