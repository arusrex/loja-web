# Importações necessárias
from vendas.models import Venda
from home.models import DadosLoja
from sat_nfe.models import ConfiguracaoSAT
from django.shortcuts import redirect
from django.contrib import messages
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from barcode import Code128
from barcode.writer import ImageWriter
from io import BytesIO
from django.http import HttpResponse
from PIL import Image
import qrcode
import tempfile
import os

def gerar_pdf_cupom_fiscal(venda, xml):
    # Dividir os dados do XML
    dados = xml.split('|')
    loja = DadosLoja.objects.first()
    sat = ConfiguracaoSAT.objects.first()

    buffer = BytesIO()

    chave_acesso = dados[8]

    # Configurações do PDF
    c = canvas.Canvas(buffer, pagesize=letter)

    largura, altura = letter

    # Cabeçalho do cupom
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, altura - 50, f"CF-e SAT - Extrato Nº {venda.id}")
    c.setFont("Helvetica", 8)
    if loja:
        c.drawString(50, altura - 70, f"{loja.nome_fantasia}")
        c.drawString(50, altura - 80, f"CNPJ: {loja.cnpj} | IE: {loja.inscricao_estadual}")
        c.drawString(50, altura - 90, f"End.: {loja.endereco}, {loja.cidade} - {loja.estado}")
        c.drawString(50, altura - 100, f"CEP: {loja.cep} | Tel: {loja.fone}")
    else:
        c.drawString(50, altura - 70, "Loja não configurada")

    # Dados do cliente
    c.drawString(50, altura - 115, f"Cliente: {venda.cliente.nome if venda.cliente else 'Consumidor Final'}")
    if venda.cliente and venda.cliente.cnpj:
        c.drawString(50, altura - 130, f"CNPJ/CPF: {venda.cliente.cnpj}")
    elif venda.cliente and venda.cliente.cpf:
        c.drawString(50, altura - 130, f"CPF: {venda.cliente.cpf}")
    else:
        c.drawString(50, altura - 130, f"CPF: ---")


    # Lista de itens da venda
    y_position = altura - 150
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, y_position, "Itens:")
    c.setFont("Helvetica", 8)
    c.drawString(50, y_position - 15, f"COD | NOME | xQtd | Med | ValorUnit | SubTotal")
    y_position -= 10
    for item in venda.itens.all():
        c.drawString(50, y_position - 20, f"{item.produto.codigo} {item.produto.nome[:20]} x{item.quantidade} {item.produto.unidade} R${item.produto.preco:.2f} = R${item.subtotal:.2f}")
        y_position -= 20

    # Totais
    y_position -= 20
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, y_position, f"TOTAL: R$ {venda.total:.2f}")
    y_position -= 10
    c.drawString(50, y_position, f"Desconto: R$ {venda.desconto_total:.2f}")
    y_position -= 10
    c.drawString(50, y_position, f"TOTAL FINAL: R$ {venda.calcular_desconto():.2f}")

    # Criar QR Code
    qr_code_text = f"http://www.sefaz.sp.gov.br/qrcode?p={dados[8]}|{dados[9]}|{dados[7]}|{dados[11]}"
    qr = qrcode.QRCode(version=1, box_size=5, border=2)
    qr.add_data(qr_code_text)
    qr.make(fit=True)
    qr_image = qr.make_image(fill="black", back_color="white")

    qr_buffer = BytesIO()
    qr_image.save(qr_buffer)
    qr_buffer.seek(0)

    qr_pil_image = Image.open(qr_buffer)

    temp_dir = tempfile.gettempdir()
    qr_image_path = os.path.join(temp_dir, "qr_image.png")
    qr_pil_image.save(qr_image_path)
    c.drawImage(qr_image_path, 110, y_position - 120, width=100, height=100)

    # Cria código de barras
    barcode_buffer = BytesIO()
    barcode_writer = ImageWriter()
    barcode_instance = Code128(chave_acesso, writer=barcode_writer)
    barcode_instance.default_writer_options['write_text'] = False
    barcode_instance.write(barcode_buffer)
    barcode_buffer.seek(0)

    barcode_image = Image.open(barcode_buffer)
    barcode_image_path = os.path.join(temp_dir, "barcode_image.png")
    barcode_image.save(barcode_image_path)
    c.drawImage(barcode_image_path, 50, y_position - 170, width=230, height=35)

    # Rodapé
    y_position -= 190
    c.setFont("Helvetica", 8)
    c.drawString(50, y_position, f"{chave_acesso}")
    c.setFont("Helvetica-Bold", 8)
    c.drawString(50, y_position - 20, f"SAT nº série: {sat.numero_sat}") #type:ignore
    c.setFont("Helvetica", 8)
    c.drawString(50, y_position - 30, "Consulta: http://www.sefaz.sp.gov.br/qrcode")
    c.drawString(50, y_position - 40, "OBRIGADO PELA PREFERÊNCIA!")

    # Finalizar o PDF
    c.save()

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="cupom_fiscal_venda_{venda.id}.pdf"'

    return response

def imprimir_sat(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    xml = venda.retornoSAT
    response = gerar_pdf_cupom_fiscal(venda, xml)
    messages.success(request, f"Cupom Fiscal gerado com sucesso!")
    return response

def gerar_pdf_comprovante(venda):
    loja = DadosLoja.objects.first()

    buffer = BytesIO()

    # Configurações do PDF
    pdf_path = f"comprovante_venda_{venda.id}.pdf"
    c = canvas.Canvas(buffer, pagesize=letter)
    largura, altura = letter

    # Cabeçalho do comprovante
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, altura - 50, f"Comprovante de Venda Nº {venda.id}")
    c.setFont("Helvetica", 10)
    if loja:
        c.drawString(50, altura - 70, f"{loja.nome_fantasia}")
        c.drawString(50, altura - 90, f"End.: {loja.endereco}, {loja.cidade} - {loja.estado}")
        c.drawString(50, altura - 110, f"Tel: {loja.fone}")
    else:
        c.drawString(50, altura - 70, "Loja não configurada")


    # Lista de itens
    y_position = altura - 140
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, y_position, "Itens:")
    c.setFont("Helvetica", 10)
    y_position -= 20
    for item in venda.itens.all():
        c.drawString(50, y_position, f"{item.produto.nome[:30]} x{item.quantidade} R${item.produto.preco:.2f} = R${item.subtotal:.2f}")
        y_position -= 20

    # Totais
    y_position -= 20
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, y_position, f"TOTAL: R$ {venda.total:.2f}")
    y_position -= 20
    c.drawString(50, y_position, f"Desconto: R$ {venda.desconto_total:.2f}")
    y_position -= 20
    c.drawString(50, y_position, f"TOTAL FINAL: R$ {venda.calcular_desconto():.2f}")

    # Rodapé
    y_position -= 40
    c.setFont("Helvetica", 10)
    c.drawString(50, y_position, "OBRIGADO PELA PREFERÊNCIA!")

    # Finalizar o PDF
    c.save()
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="comprovante_venda_{venda.id}.pdf"'

    return response

def imprimir_comprovante(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    response = gerar_pdf_comprovante(venda)
    messages.success(request, f"Comprovante gerado com sucesso!")
    return response
