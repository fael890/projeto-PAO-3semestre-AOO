from django.forms import ModelForm
from core.models import *

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
        fields = ['nome', 'email', 'telefone', 'foto', 'id_lista_compras']

class FormListaCompras(ModelForm):
    class Meta:
        model = ListaCompras
        fields = "__all__"


