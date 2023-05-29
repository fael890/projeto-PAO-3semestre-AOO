from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='url_principal'),
    path('cadastro-promocao/', cadastrar_promocao, name='url_cadastro_promocao'),
    path('listagem-promocoes/', listar_promocoes, name='url_listagem_promocoes'),
    path('atualiza-promocao/<int:id>/', atualizar_promocao, name='url_atualiza_promocao'),
    path('excluir-promocao/<int:id>/', excluir_promocao, name='url_exclui_promocao'),
    path('cadastro-mercado/', cadastrar_mercado, name='url_cadastro_mercado'),
    path('listagem-mercados/', listar_mercados, name='url_listagem_mercados'),
    path('atualiza-mercado/<int:id>/', atualizar_mercado, name='url_atualiza_mercado'),
    path('excluir-mercado/<int:id>/', excluir_mercado, name='url_exclui_mercado'),
    path('cadastro-endereco/', cadastrar_endereco, name='url_cadastro_endereco'),
    path('listagem-enderecos/', listagem_enderecos, name='url_listagem_enderecos'),
    path('atualiza-endereco/<int:id>/', atualizar_endereco, name='url_atualiza_endereco'),
    path('excluir-endereco/<int:id>/', excluir_endereco, name='url_excluir_endereco'),
]
