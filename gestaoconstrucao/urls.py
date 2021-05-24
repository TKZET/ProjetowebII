from django.contrib import admin
from django.urls import path
from .views import VendaCreateView, EletricosCreateView, HidraulicoCreateView, ClienteCreateView, VidroCreateView
from .views import TintaCreateView, EsquadriaCreateView, MadeiraCreateView, PedraCreateView, MaquinaCreateView
from .views import CeramicaCreateView, CobertaCreateView, FerramentaCreateView, IluminacaoCreateView
from .views import PisoCreateView, VendaListView, VendaCorrecaoUpdateView, VendaAtualizarObservacaoView
from .views import VendaAtualizarClienteView, VendaDetailView, VendaView, EstruturaCreateView


urlpatterns = [
    path('cadastrar/Venda', VendaCreateView.as_view(), name='cadastrar_venda'),
    path('cadastrar/Eletricos', EletricosCreateView.as_view(), name='cadastrar_eletricos'),
    path('cadastrar/Hidraulico', HidraulicoCreateView.as_view(), name='cadastrar_hidraulico'),
    path('cadastrar/Cliente', ClienteCreateView.as_view(), name='cadastrar_cliente'),
    path('cadastrar/Vidro', VidroCreateView.as_view(), name='cadastrar_vidro'),
    path('cadastrar/Tinta', TintaCreateView.as_view(), name='cadastrar_tinta'),
    path('cadastrar/Esquadria', EsquadriaCreateView.as_view(), name='cadastrar_esquadria'),
    path('cadastrar/Madeira', MadeiraCreateView.as_view(), name='cadastrar_madeira'),
    path('cadastrar/Pedra', PedraCreateView.as_view(), name='cadastrar_pedra'),
    path('cadastrar/Maquina', MaquinaCreateView.as_view(), name='cadastrar_maquina'),
    path('cadastrar/Ceramica', CeramicaCreateView.as_view(), name='cadastrar_ceramica'),
    path('cadastrar/Coberta', CobertaCreateView.as_view(), name='cadastrar_coberta'),
    path('cadastrar/Ferramenta', FerramentaCreateView.as_view(), name='cadastrar_ferramenta'),
    path('cadastrar/Iluminacao', IluminacaoCreateView.as_view(), name='cadastrar_iluminacao'),
    path('cadastrar/Estrutura', EstruturaCreateView.as_view(), name='cadastrar_estrutura'),
    path('cadastrar/Piso', PisoCreateView.as_view(), name='cadastrar_piso'),
    path('listar/venda', VendaListView.as_view(), name='listar_venda'),
    path('atualizar/venda/<int:pk>', VendaCorrecaoUpdateView.as_view(), name='corrigir_venda'),
    path('atualizar/venda/observacao/<int:pk>', VendaAtualizarObservacaoView.as_view(),
         name='atualizar_observacao_venda'),
    path('atualizar/venda/cliente/<int:pk>', VendaAtualizarClienteView.as_view(), name='atualizar_cliente_venda'),
    path('ajax/desabilitar/venda/<int:pk>', VendaView.desabilitarVenda, name='ajax_desabilitar_venda'),
    path('ajax/habilitar/venda/<int:pk>', VendaView.habilitarVenda, name='ajax_habilitar_venda'),
    path('detalhes/venda/<int:pk>', VendaDetailView.as_view(), name='detalhes_venda'),
]
