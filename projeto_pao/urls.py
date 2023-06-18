from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('core/', include('django.contrib.auth.urls')),
    path('accounts/login_usuario/', login_usuario, name='url_login_usuario'),
    path('accounts/logout_usuario/', logout_usuario, name='url_logout_usuario'),
    path('accounts/registrar/', registrar, name='url_registrar'),

    path('', inicio, name='url_principal'),
    path('lista-compras/', itens_lista_compras, name='url_lista_compras'),
    path('lista-compras/<int:id>', adicionar_item_lista, name='url_adicionar_item'),
    path('lista-compras/excluir/<int:id>', excluir_item_lista, name='url_excluir_item'),

    path('listagem-promocoes/', listar_promocoes, name='url_listagem_promocoes'),
    path('listagem-promocao/<int:id>/', listar_promocao, name='url_listagem_promocao_id'),

    path('perfil/', exibir_perfil, name='url_perfil'),

    path('cadastro-promocao/', cadastrar_promocao, name='url_cadastro_promocao'),
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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
