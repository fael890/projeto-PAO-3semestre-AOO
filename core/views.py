from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from core.forms import *
from core.models import *
from django.contrib.auth.forms import UserCreationForm

def inicio(request):
    categorias = ['padaria', 'hortifruti', 'acougue', 'bebidas']
    promocoes = []
    for categoria in categorias:
        promocoes.append(Promocao.objects.filter(categoria=categoria))
    return render(request, 'core/index.html', {'promocoes': promocoes})

def logout_usuario(request):
    logout(request)
    return redirect('url_principal')

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('url_principal')
        else:
            return redirect('url_login_usuario')
    else:
        return render(request, 'authenticate/login.html', {'contador': 0})

def registrar(request):
    if request.method == 'POST':
        form_autenticao = UserCreationForm(request.POST)
        form_usuario = FormUsuario(request.POST)
        form_endereco = FormEndereco(request.POST)
        if form_autenticao.is_valid() and form_usuario.is_valid() and form_endereco.is_valid():
            endereco = form_endereco.save()
            autenticao = form_autenticao.save()
            usuario = form_usuario.save(commit='False')
            usuario.endereco = endereco
            usuario.autenticacao = autenticao
            usuario.save()
            return redirect('url_principal')
    else:
        form_autenticao = UserCreationForm()
        form_usuario = FormUsuario()
        form_endereco = FormEndereco()
    contexto = {'form_autenticao': form_autenticao, 'form_usuario': form_usuario, 'form_endereco': form_endereco}
    return render(request, 'authenticate/registrar.html', contexto)

def itens_lista_compras(request):
    itens = ListaCompras.objects.all()
    return render(request, 'core/lista_compras.html', {'itens': itens})

def adicionar_item_lista(request, id):
    promocao_selecionada = Promocao.objects.get(id=id)
    item_lista = ListaCompras(id_promocao=promocao_selecionada)
    item_lista.save()
    return redirect('url_lista_compras')

def excluir_item_lista(request, id):
    obj = ListaCompras.objects.get(id=id)
    obj.delete()
    return redirect('url_lista_compras')

def exibir_perfil(request):
    usuario_logado = request.user
    perfil = Usuario.objects.get(autenticacao=usuario_logado)
    return render(request, 'core/perfil.html', {'perfil': perfil})

def listar_promocoes(request):
    if request.POST and request.POST['input_promocao']:
        dados = Promocao.objects.filter(descricao__contains=request.POST['input_promocao'])
    else:
        dados = Promocao.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/listagem_promocoes.html', contexto)

def listar_promocao(request, id):
    promocao = Promocao.objects.get(id=id)
    return render(request, 'core/listagem_promocao.html', {'promocao': promocao})

def cadastro_completo(request):
    form = FormUsuario(request.POST or None)
    form_endereco = FormEndereco(request.POST or None)
    if form.is_valid() and form_endereco.is_valid():
        endereco_usuario = form_endereco.save()
        usuario = form.save(commit=False)
        usuario.endereco = endereco_usuario
        usuario.save()
        return redirect('url_listagem_completa')
    contexto = {'form': form, 'form_endereco': form_endereco}
    return render(request, 'core/cadastro_completo.html', contexto)

def listagem_completa(request):
    dados_usuario = Usuario.objects.all()
    contexto = {'dados_usuario': dados_usuario}
    return render(request, 'core/listagem_completa.html', contexto)

def cadastrar_promocao(request):
    form = FormPromocao(request.POST or None)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_promocoes')
    contexto = {'form': form, 'txt_title': 'cad_prom', 'txt_descricao': 'Cadastro de Promoção'}
    return render(request, 'core/cadastro.html', contexto)


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
    form_endereco = FormEndereco(request.POST or None)
    if form.is_valid() and form_endereco.is_valid():
        endereco = form_endereco.save()
        print(endereco)
        mercado = form.save(commit=False)
        mercado.endereco = endereco
        mercado.save()
        return redirect('url_listagem_mercados')
    contexto = {'form': form, 'form_endereco': form_endereco}
    return render(request, 'core/cadastro_completo.html', contexto)

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
