from django.shortcuts import render, redirect
from core.forms import *
from core.models import *

def inicio(request):
    return render(request, 'core/index.html')

def cadastro_completo(request):
    form_usuario = FormUsuario(request.POST or None)
    form_endereco = FormEndereco(request.POST or None)
    if form_usuario.is_valid() and form_endereco.is_valid():
        endereco_usuario = form_endereco.save()
        usuario = form_usuario.save(commit=False)
        usuario.endereco = endereco_usuario
        usuario.save()
        return redirect('url_listagem_completa')
    contexto = {'form_usuario': form_usuario, 'form_endereco': form_endereco}
    return render(request, 'core/cadastro_completo.html', contexto)

def listagem_completa(request):
    dados_usuario = Usuario.objects.all()
    contexto = {'dados_usuario': dados_usuario}
    return render(request, 'core/listagem_completa.html', contexto)

'''
def cadastrar_usuario_completo(request):
    form = FormUsuarioCompleto(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_usuarios')
    contexto = {'form': form, 'txt_title': 'cad_prom', 'txt_descricao': 'Cadastro de Promoção'}
    return render(request, 'core/cadastro_usuario_completo.html', contexto)
'''

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

def cadastrar_usuario(request):
    form = FormUsuario(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_usuarios')
    contexto = {'form': form, 'txt_title': 'cad_user', 'txt_descricao': 'Cadastro de usuário'}
    return render(request, 'core/cadastro.html', contexto)

def listagem_usuarios(request):
    dados = Usuario.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/listagem_usuarios.html', contexto)

def atualizar_usuario(request, id):
    obj = Usuario.objects.get(id=id)
    form = FormUsuario(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_usuarios')
    contexto = {'form': form, 'txt_title': 'att_user', 'txt_descricao': 'Atualização de Usuário',
                'txt_button': 'Atualizar'}
    return render(request, 'core/cadastro.html', contexto)

def excluir_usuario(request, id):
    obj = Usuario.objects.get(id=id)
    obj.delete()
    return redirect('url_listagem_usuarios')

def cadastrar_lista_compras(request):
    form = FormListaCompras(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_lista_compras')
    contexto = {'form': form, 'txt_title': 'cad_lista', 'txt_descricao': 'Cadastro de lista de compras'}
    return render(request, 'core/cadastro.html', contexto)

def listagem_lista_compras(request):
    dados = ListaCompras.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/listagem_lista_compras.html', contexto)

def atualizar_lista_compras(request, id):
    obj = ListaCompras.objects.get(id=id)
    form = FormListaCompras(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_lista_compras')
    contexto = {'form': form, 'txt_title': 'cad_lista', 'txt_descricao': 'Cadastro de lista de compras', 'txt_button': 'Atualizar'}
    return render(request, 'core/cadastro.html', contexto)

def excluir_lista_compras(request, id):
    obj = ListaCompras.objects.get(id=id)
    obj.delete()
    return redirect('url_listagem_lista_compras')
