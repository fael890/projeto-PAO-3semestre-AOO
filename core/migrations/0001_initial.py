# Generated by Django 4.2.1 on 2023-05-26 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=100, verbose_name='CEP')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('rua', models.CharField(max_length=100, verbose_name='Rua')),
                ('bairro', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro')),
                ('numero', models.IntegerField(blank=True, null=True, verbose_name='Número')),
            ],
        ),
        migrations.CreateModel(
            name='ListaCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True, null=True, verbose_name='Quantidade')),
            ],
        ),
        migrations.CreateModel(
            name='Mercado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=100, verbose_name='Razão Social')),
                ('cnpj', models.CharField(max_length=20, verbose_name='CNPJ')),
                ('id_endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.endereco', verbose_name='Endereço')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('telefone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='foto_cliente', verbose_name='')),
                ('id_endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.endereco', verbose_name='Endereço')),
                ('id_lista_compras', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.listacompras', verbose_name='ListaCompras')),
            ],
        ),
        migrations.CreateModel(
            name='Promocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=150, null=True, verbose_name='Descricao')),
                ('unidade', models.CharField(blank=True, max_length=20, null=True, verbose_name='Unidade')),
                ('categoria', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria')),
                ('preco_normal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço normal')),
                ('preco_promocao', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('data_inicio', models.DateField(verbose_name='Inicio')),
                ('data_fim', models.DateField(verbose_name='Fim')),
                ('distancia', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Distância')),
                ('id_mercado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mercado', verbose_name='Mercado')),
            ],
        ),
        migrations.AddField(
            model_name='listacompras',
            name='id_promocao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.promocao', verbose_name='Promoção'),
        ),
    ]
