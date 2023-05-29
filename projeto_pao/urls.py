from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='url_principal'),
    path('cadastro-promocao/', cadastrar_promocao, name='url_cadastro_promocao'),
    path('listagem-promocoes/', listar_promocoes, name='url_listagem_promocoes'),
    path('atualiza-promocao/', atualizar_promocao, name='url_atualiza_promocao'),
    path('excluir-promocao/', excluir_promocao, name='url_exclui_promocao'),
]
