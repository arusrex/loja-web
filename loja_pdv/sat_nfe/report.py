import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from vendas.models import *
from django.shortcuts import redirect
from pathlib import Path
from django.http import FileResponse, HttpResponse
from home.models import DadosLoja


BASE_DIR = Path(__file__).resolve().parent.parent

def gerar_comprovante(venda, xml):
    loja = DadosLoja.objects.first()
    output_dir = "comprovantes/"
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{output_dir}comprovante_venda_{venda.id}.pdf"

    # Iniciar o PDF
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    if venda.retorno_sat and venda.codigo_retorno == "06000":
        # Títulos
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, height - 50, f"CF-e SAT nº {venda.sat_cfe}")
        c.setFont("Helvetica", 10)
        c.drawString(50, height - 70, loja.nome_fantasia if loja else 'ArusTI')
    else:
        # Títulos
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, height - 50, "DOCUMENTO AUXILIAR DO CF-e SAT")
        c.setFont("Helvetica", 10)
        c.drawString(50, height - 70, "Não é válido como nota fiscal")

    # Dados do Emitente
    c.setFont("Helvetica-Bold", 10)
    emitente = height - 100
    c.drawString(50, emitente, "Emitente:")
    c.setFont("Helvetica", 10)
    c.drawString(50, emitente - 15, f"Razão Social: {loja.razao_social if loja else 'ArusTI'}")
    c.drawString(50, emitente - 30, f"CNPJ: {loja.cnpj if loja else '---'}")
    
    if venda.cliente:
        if venda.cliente.cnpj:
            cnpj_cpf = venda.cliente.cnpj
        elif venda.cliente.cpf:
            cnpj_cpf = venda.cliente.cpf
        else:
            cnpj_cpf = '---'

        # Dados do Destinatário PJ
        c.setFont("Helvetica-Bold", 10)
        destinatario = emitente - 60
        c.drawString(50, destinatario, "Destinatário:")
        c.setFont("Helvetica", 10)
        c.drawString(
                50,
                destinatario - 15,
                f"Cliente: {venda.cliente.nome if venda.cliente else 'Consumidor Final'}"
            )
        c.drawString(50, destinatario - 30, f"CNPJ/CPF: {cnpj_cpf}")
    else:
        # Sem dados de Cliente
        c.setFont("Helvetica-Bold", 10)
        destinatario = emitente - 60
        c.drawString(50, destinatario, "Destinatário:")
        c.setFont("Helvetica", 10)
        c.drawString(50, destinatario - 15, f"Cliente: Consumidor Final")

    # Dados da Venda
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, height - 220, "Itens da Venda:")
    y_position = height - 235
    for item in venda.itens.all():
        c.setFont("Helvetica", 9)
        c.drawString(50, y_position, f"{item.produto.descricao} - {item.quantidade} x {item.produto.preco:.2f} = {item.subtotal:.2f}")
        y_position -= 15
        if y_position < 100:  # Nova página se necessário
            c.showPage()
            y_position = height - 50

    # Totalização
    c.setFont("Helvetica-Bold", 10)
    y_position -= 20
    c.drawString(50, y_position, f"Total: R$ {venda.total:.2f}")
    c.drawString(50, y_position - 15, f"Desconto: R$ {venda.desconto_total:.2f}")
    c.drawString(50, y_position - 30, f"Total Final: R$ {venda.calcular_desconto():.2f}")

    # QR Code
    qr_code_text = gerar_qrcode(xml)
    qr_code = qr.QrCodeWidget(qr_code_text)
    bounds = qr_code.getBounds()
    qr_width = bounds[2] - bounds[0]
    qr_height = bounds[3] - bounds[1]
    d = Drawing(100, 100)
    d.add(qr_code)
    renderPDF.draw(d, c, 400, y_position - 80)

    # Mensagem final
    c.setFont("Helvetica", 8)
    c.drawString(50, y_position - 120, "Consulta pública disponível no site da SEFAZ com o QR Code acima.")

    # Salvar PDF
    c.save()
    return filename


def gerar_qrcode(xml):
    chave_acesso = "CHAVE_DE_ACESSO_EXTRAIDA_DO_XML"
    url_consulta = "http://www.sefaz.sp.gov.br/qrcode"
    return f"{url_consulta}?p={chave_acesso}"


def imprimir_comprovante(filename, venda_id):
    try:
        caminho_pdf = BASE_DIR / filename.replace('\\', '/')
        print(caminho_pdf)

        if not os.path.exists(caminho_pdf):
            raise FileNotFoundError(f"O arquivo {caminho_pdf} não foi encontrado.")
        
        response = FileResponse(open(caminho_pdf, "rb"), content_type="application/pdf")
        response["Content-Disposition"] = f"inline; filename=comprovante_venda_{venda_id}.pdf"
        return response

    except Exception as e:
        return HttpResponse(f"Erro ao gerar comprovante: {str(e)}")

def imprimir_sat(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    xml = venda.retorno_sat
    filename = gerar_comprovante(venda, xml)
    return imprimir_comprovante(filename, venda_id)
