# Generated by Django 5.1.3 on 2024-11-29 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='cfop',
            field=models.CharField(choices=[('1102', '1102 - Compra para comercialização'), ('2102', '2102 - Compra para comercialização - Interestadual'), ('1401', '1401 - Devolução de venda de produção do estabelecimento'), ('2401', '2401 - Devolução de venda de produção do estabelecimento - Interestadual'), ('1403', '1403 - Devolução de venda de mercadoria adquirida de terceiros'), ('2403', '2403 - Devolução de venda de mercadoria adquirida de terceiros - Interestadual'), ('1556', '1556 - Compra de bem para o ativo imobilizado'), ('2556', '2556 - Compra de bem para o ativo imobilizado - Interestadual'), ('1949', '1949 - Outras entradas'), ('2949', '2949 - Outras entradas - Interestadual'), ('5102', '5102 - Venda de mercadoria adquirida ou recebida de terceiros'), ('6102', '6102 - Venda de mercadoria adquirida ou recebida de terceiros - Interestadual'), ('5403', '5403 - Venda de mercadoria adquirida para não contribuinte'), ('6403', '6403 - Venda de mercadoria adquirida para não contribuinte - Interestadual'), ('5405', '5405 - Venda de mercadoria adquirida para a Zona Franca de Manaus ou Áreas de Livre Comércio'), ('6405', '6405 - Venda de mercadoria adquirida para a Zona Franca de Manaus ou Áreas de Livre Comércio - Interestadual'), ('5949', '5949 - Outras saídas'), ('6949', '6949 - Outras saídas - Interestadual')], max_length=4),
        ),
        migrations.AlterField(
            model_name='produto',
            name='csosn',
            field=models.CharField(blank=True, choices=[('101', '101 - Tributada pelo Simples Nacional com permissão de crédito'), ('102', '102 - Tributada pelo Simples Nacional sem permissão de crédito'), ('103', '103 - Isenção do ICMS no Simples Nacional para faixa de receita bruta'), ('201', '201 - Tributada pelo Simples Nacional com permissão de crédito e com cobrança do ICMS por substituição tributária'), ('202', '202 - Tributada pelo Simples Nacional sem permissão de crédito e com cobrança do ICMS por substituição tributária'), ('203', '203 - Isenção do ICMS no Simples Nacional para faixa de receita bruta e com cobrança do ICMS por substituição tributária'), ('300', '300 - Imune'), ('400', '400 - Não tributada pelo Simples Nacional'), ('500', '500 - ICMS cobrado anteriormente por substituição tributária ou antecipação'), ('900', '900 - Outros')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='cst',
            field=models.CharField(blank=True, choices=[('00', '00 - Tributada integralmente'), ('10', '10 - Tributada e com cobrança do ICMS por substituição tributária'), ('20', '20 - Com redução de base de cálculo'), ('30', '30 - Isenta ou não tributada e com cobrança do ICMS por substituição tributária'), ('40', '40 - Isenta'), ('41', '41 - Não tributada'), ('50', '50 - Suspensão'), ('51', '51 - Diferimento'), ('60', '60 - ICMS cobrado anteriormente por substituição tributária'), ('70', '70 - Com redução de base de cálculo e cobrança do ICMS por substituição tributária'), ('90', '90 - Outras')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='unidade',
            field=models.CharField(choices=[('UN', 'UN - Unidade'), ('KG', 'KG - Quilograma'), ('G', 'G - Grama'), ('L', 'L - Litro'), ('ML', 'ML - Mililitro'), ('M', 'M - Metro'), ('M²', 'M² - Metro Quadrado'), ('CX', 'CX - Caixa'), ('FD', 'FD - Fardo'), ('ROLO', 'ROLO - Rolo'), ('PAR', 'PAR - Par')], max_length=4),
        ),
    ]
