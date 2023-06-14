from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from core.models import *
from django import forms
from django.contrib.auth.models import User

class FormPromocao(ModelForm):
    class Meta:
        model = Promocao
        fields = "__all__"

class FormMercado(ModelForm):
    class Meta:
        model = Mercado
        fields = ['razao_social', 'cnpj']

class FormEndereco(ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'estado', 'cidade', 'rua', 'bairro', 'numero']

class FormUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'imagem', 'id_lista_compras']

class FormListaCompras(ModelForm):
    class Meta:
        model = ListaCompras
        fields = "__all__"


