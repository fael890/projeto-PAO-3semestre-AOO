from django.forms import ModelForm
from core.models import *

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
        fields = "__all__"

class FormUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class FormListaCompras(ModelForm):
    class Meta:
        model = ListaCompras
        fields = "__all__"


