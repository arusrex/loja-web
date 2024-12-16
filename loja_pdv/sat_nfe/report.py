# type:ignore
from vendas.models import Venda
from django.shortcuts import redirect
import qrcode
import win32print
import win32ui
from PIL import Image, ImageWin
import os


def gerar_cupom_fiscal_com_qrcode(venda, xml):
    largura_max = 42
    # Pegar a impressora padrão
    printer_name = win32print.GetDefaultPrinter()

    # Criar o QR Code
    chave_acesso = "CHAVE_DE_ACESSO_EXTRAIDA_DO_XML"
    url_consulta = "http://www.sefaz.sp.gov.br/qrcode"
    qr_code_text = f"{url_consulta}?p={chave_acesso}"

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
    line_height = 50

    # Imprimir o cabeçalho como texto
    cupom_texto = [
        "----------------------------------------",
        "        DOCUMENTO AUXILIAR DO CF-e SAT",
        "             NÃO É DOCUMENTO FISCAL",
        "----------------------------------------",
        f"Data: {venda.data.strftime('%d/%m/%Y %H:%M')}",
        f"Venda Nº: {venda.id}",
        f"Cliente: {venda.cliente.razao_social if venda.cliente else 'Consumidor Final'}",
        f"CNPJ: {venda.cliente.cnpj if venda.cliente else '---'}",
        "----------------------------------------",
        "Itens:",
    ]

    for linha in cupom_texto:
        linhas_quebradas = quebra_linhas(linha, largura_max)
        for l in linhas_quebradas:
            hdc.TextOut(start_x, start_y, l)
            start_y += line_height

    # Imprimir os itens da venda
    for item in venda.itens.all():
        texto_item = f"{item.produto.descricao[:30]} {item.quantidade} x {item.produto.preco:.2f} = {item.subtotal:.2f}"
        linhas_quebradas = quebra_linhas(texto_item, largura_max)
        for l in linhas_quebradas:
            hdc.TextOut(start_x, start_y, l)
            start_y += 50

    # Total e descontos
    totais = [
        f"TOTAL: R$ {venda.total:.2f}",
        f"Desconto: R$ {venda.desconto_total:.2f}",
        f"TOTAL FINAL: R$ {venda.calcular_desconto():.2f}",
    ]

    for linha in totais:
        linhas_quebradas = quebra_linhas(linha, largura_max)
        for l in linhas_quebradas:
            hdc.TextOut(start_x, start_y, l)
            start_y += 50

    # Inserir o QR Code
    dib = ImageWin.Dib(qr_image)
    dib.draw(hdc.GetHandleOutput(), (start_x, start_y, start_x + 900, start_y + 900))
    start_y += 950

    # Rodapé
    rodape = [
         f"Consulta: {qr_code_text}",
        "----------------------------------------",
        "OBRIGADO PELA PREFERÊNCIA!",
    ]

    for linha in rodape:
        linhas_quebradas = quebra_linhas(linha, largura_max)
        for l in linhas_quebradas:
            hdc.TextOut(start_x, start_y, l)
            start_y += 50

    # Finalizar a impressão
    hdc.EndPage()
    hdc.EndDoc()
    hdc.DeleteDC()
    win32print.ClosePrinter(hprinter)
    os.remove(qr_image_path)
    

def imprimir_sat(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    xml = venda.retorno_sat
    gerar_cupom_fiscal_com_qrcode(venda, xml)
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