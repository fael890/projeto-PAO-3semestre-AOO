from django.shortcuts import render, redirect
from core.forms import *
from core.models import *

def inicio(request):
    return render(request, 'core/index.html')

def cadastrar_promocao(request):
    form = FormPromocao(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_obter_promocoes')
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
    contexto = {'form': form, 'txt_title': 'Atualização de Promoção', 'txt_descricao': 'Atualização de Promoção', 'txt_button': 'Atualizar'}
    return render(request, 'core/cadastro.html', contexto)

def excluir_promocao(request, id):
    obj = Promocao.objects.get(id=id)
    obj.delete()
    return redirect('url_exclui_promocao')