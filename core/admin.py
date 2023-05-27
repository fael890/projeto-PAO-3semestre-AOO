from django.contrib import admin
from core.models import Promocao, Mercado, Usuario, Endereco, ListaCompras

# Register your models here.
admin.site.register(Promocao)
admin.site.register(Mercado)
admin.site.register(Usuario)
admin.site.register(Endereco)
admin.site.register(ListaCompras)
