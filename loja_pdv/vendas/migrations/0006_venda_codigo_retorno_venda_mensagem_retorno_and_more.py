# Generated by Django 5.1.3 on 2024-12-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0005_venda_xml_cfe'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='codigo_retorno',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venda',
            name='mensagem_retorno',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venda',
            name='sat_cfe',
            field=models.TextField(blank=True, null=True),
        ),
    ]
