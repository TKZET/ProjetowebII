from django.contrib import admin
from django.urls import path
from .views import VendaCreateView, EletricosCreateView, HidraulicoCreateView, ClienteCreateView, VidroCreateView, \
    EletricosUpdateView, HidraulicoUpdateView, VidroUpdateView, TintaUpdateView, EsquadriaUpdateView, \
    MadeiraUpdateView, PedraUpdateView, MaquinaUpdateView, CeramicaUpdateView, FerramentaUpdateView, \
    IluminacaoUpdateView, EstruturaUpdateView, PisoUpdateView, \
    EletricosPDFDetailView, HidraulicoPDFDetailView, ClientePDFDetailView, VidroPDFDetailView, TintaPDFDetailView, \
    EsquadriaPDFDetailView, MadeiraPDFDetailView, PedraPDFDetailView, MaquinaPDFDetailView, CeramicaPDFDetailView, \
    FerramentaPDFDetailView, IluminacaoPDFDetailView, PisoPDFDetailView
from .views import TintaCreateView, EsquadriaCreateView, MadeiraCreateView, PedraCreateView, MaquinaCreateView
from .views import CeramicaCreateView, CobertaCreateView, FerramentaCreateView, IluminacaoCreateView
from .views import PisoCreateView, VendaListView, VendaCorrecaoUpdateView, VendaAtualizarObservacaoView
from .views import VendaAtualizarClienteView, VendaDetailView, VendaView, EstruturaCreateView, VendaPDFDetailView,  \
    EletricosListView, CobertaListView, EsquadriaListView, EstruturaListView, FerramentaListView, MadeiraListView, \
    MaquinaListView, PedraListView, PisoListView, TintaListView, IluminacaoListView, CeramicaListView, ClienteListView

urlpatterns = [
    path('cadastrar/Venda', VendaCreateView.as_view(), name='cadastrar_venda'),
    path('cadastrar/eletricos', EletricosCreateView.as_view(), name='cadastrar_eletricos'),
    path('cadastrar/hidraulico', HidraulicoCreateView.as_view(), name='cadastrar_hidraulico'),
    path('cadastrar/cliente', ClienteCreateView.as_view(), name='cadastrar_cliente'),
    path('cadastrar/vidro', VidroCreateView.as_view(), name='cadastrar_vidro'),
    path('cadastrar/tinta', TintaCreateView.as_view(), name='cadastrar_tinta'),
    path('cadastrar/esquadria', EsquadriaCreateView.as_view(), name='cadastrar_esquadria'),
    path('cadastrar/madeira', MadeiraCreateView.as_view(), name='cadastrar_madeira'),
    path('cadastrar/pedra', PedraCreateView.as_view(), name='cadastrar_pedra'),
    path('cadastrar/maquina', MaquinaCreateView.as_view(), name='cadastrar_maquina'),
    path('cadastrar/ceramica', CeramicaCreateView.as_view(), name='cadastrar_ceramica'),
    path('cadastrar/coberta', CobertaCreateView.as_view(), name='cadastrar_coberta'),
    path('cadastrar/Ferramenta', FerramentaCreateView.as_view(), name='cadastrar_ferramenta'),
    path('cadastrar/Iluminacao', IluminacaoCreateView.as_view(), name='cadastrar_iluminacao'),
    path('cadastrar/Estrutura', EstruturaCreateView.as_view(), name='cadastrar_estrutura'),
    path('cadastrar/Piso', PisoCreateView.as_view(), name='cadastrar_piso'),
    path('listar/venda', VendaListView.as_view(), name='listar_venda'),
    path('listar/ceramica', CeramicaListView.as_view(), name='listar_ceramica'),
    path('listar/cliente', ClienteListView.as_view(), name='listar_cliente'),
    path('listar/eletricos', EletricosListView.as_view(), name='listar_eletricos'),
    path('listar/coberta', CobertaListView.as_view(), name='listar_coberta'),
    path('listar/esquadria', EsquadriaListView.as_view(), name='listar_esquadria'),
    path('listar/estrutura', EstruturaListView.as_view(), name='listar_estrutura'),
    path('listar/ferramenta', FerramentaListView.as_view(), name='listar_ferramenta'),
    path('listar/iluminacao', IluminacaoListView.as_view(), name='listar_iluminacao'),
    path('listar/madeira', MadeiraListView.as_view(), name='listar_madeira'),
    path('listar/maquina', MaquinaListView.as_view(), name='listar_maquina'),
    path('listar/pedra', PedraListView.as_view(), name='listar_pedra'),
    path('listar/piso', PisoListView.as_view(), name='listar_piso'),
    path('listar/tinta', TintaListView.as_view(), name='listar_tinta'),
    path('atualizar/venda/<int:pk>', VendaCorrecaoUpdateView.as_view(), name='corrigir_venda'),
    path('atualizar/eletricos', EletricosUpdateView.as_view(), name='atualizar_eletricos'),
    path('atualizar/hidraulico', HidraulicoUpdateView.as_view(), name='atualizar_hidraulico'),
    path('atualizar/vidro', VidroUpdateView.as_view(), name='atualizar_vidro'),
    path('atualizar/tinta', TintaUpdateView.as_view(), name='atualizar_tinta'),
    path('atualizar/esquadria', EsquadriaUpdateView.as_view(), name='atualizar_esquadria'),
    path('atualizar/madeira', MadeiraUpdateView.as_view(), name='atualizar_madeira'),
    path('atualizar/pedra', PedraUpdateView.as_view(), name='atualizar_pedra'),
    path('atualizar/maquina', MaquinaUpdateView.as_view(), name='atualizar_maquina'),
    path('atualizar/ceramica', CeramicaUpdateView.as_view(), name='atualizar_ceramica'),
    path('atualizar/ferramenta', FerramentaUpdateView.as_view(), name='atualizar_ferramenta'),
    path('atualizar/iluminacao', IluminacaoUpdateView.as_view(), name='atualizar_iluminacao'),
    path('atualizar/venda/observacao/<int:pk>', VendaAtualizarObservacaoView.as_view(),
         name='atualizar_observacao_venda'),
    path('atualizar/estrutura', EstruturaUpdateView.as_view(), name='atualizar_estrutura'),
    path('atualizar/piso', PisoUpdateView.as_view(), name='atualizar_piso'),
    path('atualizar/venda/cliente/<int:pk>', VendaAtualizarClienteView.as_view(), name='atualizar_cliente_venda'),
    path('ajax/desabilitar/venda/<int:pk>', VendaView.desabilitarVenda, name='ajax_desabilitar_venda'),
    path('ajax/habilitar/venda/<int:pk>', VendaView.habilitarVenda, name='ajax_habilitar_venda'),
    path('detalhes/venda/<int:pk>', VendaDetailView.as_view(), name='detalhes_venda'),
    path('pdf/venda/<int:pk>', VendaPDFDetailView.as_view(), name='pdf_venda'),
    path('pdf/eletricos/<int:pk>', EletricosPDFDetailView.as_view(), name='pdf_eletricos'),
    path('pdf/hidraulico/<int:pk>', HidraulicoPDFDetailView.as_view(), name='pdf_hidraulico'),
    path('pdf/cliente/<int:pk>', ClientePDFDetailView.as_view(), name='pdf_cliente'),
    path('pdf/vidro/<int:pk>', VidroPDFDetailView.as_view(), name='pdf_vidro'),
    path('pdf/tinta/<int:pk>', TintaPDFDetailView.as_view(), name='pdf_tinta'),
    path('pdf/esquadria/<int:pk>', EsquadriaPDFDetailView.as_view(), name='pdf_esquadria'),
    path('pdf/madeira/<int:pk>', MadeiraPDFDetailView.as_view(), name='pdf_madeira'),
    path('pdf/pedra/<int:pk>', PedraPDFDetailView.as_view(), name='pdf_pedra'),
    path('pdf/maquina/<int:pk>', MaquinaPDFDetailView.as_view(), name='pdf_maquina'),
    path('pdf/ceramica/<int:pk>', CeramicaPDFDetailView.as_view(), name='pdf_ceramica'),
    path('pdf/ferramenta/<int:pk>', FerramentaPDFDetailView.as_view(), name='pdf_ferramenta'),
    path('pdf/iluminacao/<int:pk>', IluminacaoPDFDetailView.as_view(), name='pdf_iluminacao'),
    path('pdf/piso/<int:pk>', PisoPDFDetailView.as_view(), name='pdf_piso'),

]
