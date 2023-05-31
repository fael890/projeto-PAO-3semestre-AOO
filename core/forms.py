from django.forms import ModelForm
from core.models import *

'''
class FormUsuarioCompleto(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'foto','id_endereco__cep', 'id_endereco__estado', 'id_endereco__cidade', 'id_endereco__rua', 'id_endereco__bairro', 'id_endereco__numero']
'''
class FormPromocao(ModelForm):
    class Meta:
        model = Promocao
        fields = "__all__"

class FormMercado(ModelForm):
    class Meta:
        model = Mercado
        fields = "__all__"

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


