from django.shortcuts import render, redirect
from core.forms import *
from core.models import *

def inicio(request):
    return render(request, 'core/index.html')

def cadastrar_promocao(request):
    form = FormPromocao(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_promocoes')
    contexto = {'form': form, 'txt_title': 'cad_prom', 'txt_descricao': 'Cadastro de Promoção'}
    return render(request, 'core/cadastro.html', contexto)
def listar_promocoes(request):
    dados = Promocao.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/listagem_promocoes.html', contexto)

def atualizar_promocao(request, id):
    obj = Promocao.objects.get(id=id)
    form = FormPromocao(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('url_atualiza_promocao')
    contexto = {'form': form, 'txt_title': 'att_prom', 'txt_descricao': 'Atualização de Promoção', 'txt_button': 'Atualizar'}
    return render(request, 'core/cadastro.html', contexto)

def excluir_promocao(request, id):
    obj = Promocao.objects.get(id=id)
    obj.delete()
    return redirect('url_listagem_promocoes')

def cadastrar_mercado(request):
    form = FormMercado(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_mercados')
    contexto = {'form': form, 'txt_title': 'cad_merc', 'txt_descrição': 'Cadastro de mercado'}
    return render(request, 'core/cadastro.html', contexto)

def listar_mercados(request):
    dados = Mercado.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/listagem_mercados.html', contexto)

def atualizar_mercado(request, id):
    obj = Mercado.objects.get(id=id)
    form = FormMercado(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('url_atualiza_mercado')
    contexto = {'form': form, 'txt_title': 'att_merc', 'txt_descricao': 'Atualização de Mercado', 'txt_button': 'Atualizar'}
    return render(request, 'core/cadastro.html', contexto)

def excluir_mercado(request, id):
    obj = Mercado.objects.get(id=id)
    obj.delete()
    return redirect('url_listagem_mercados')

def cadastrar_endereco(request):
    form = FormEndereco(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_enderecos')
    contexto = {'form': form, 'txt_title': 'cad_end', 'txt_descricao': 'Cadastro de endereço'}
    return render(request, 'core/cadastro.html', contexto)

def listagem_enderecos(request):
    dados = Endereco.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/listagem_enderecos.html', contexto)

def atualizar_endereco(request, id):
    obj = Endereco.objects.get(id=id)
    form = FormEndereco(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_enderecos')
    contexto = {'form': form, 'txt_title': 'att_end', 'txt_descricao': 'Atualização de Endereço', 'txt_button': 'Atualizar'}
    return render(request, 'core/cadastro.html', contexto)

def excluir_endereco(request, id):
    obj = Endereco.objects.get(id=id)
    obj.delete()
    return redirect('url_listagem_enderecos')