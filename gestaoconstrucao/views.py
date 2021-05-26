from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from easy_pdf.views import PDFTemplateResponseMixin
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from .forms import VendaForm, VendaObservacaoForm, VendaClienteForm, EletricosForm, HidraulicoForm, VidroForm, \
    TintaForm, EsquadriaForm, MadeiraForm, PedraForm, CeramicaForm, CobertaForm, MaquinaForm, FerramentaForm, \
    IluminacaoForm, EstruturaForm, PisoForm
from .models import Venda, Eletricos, Hidraulico, Cliente, Vidro, Tinta, Esquadria, Madeira, Pedra, Maquina
from .models import Ceramica, Coberta, Ferramenta, Iluminacao, Estrutura, Piso



#______________________________________CreateView_____________________________________

class VendaCreateView(CreateView):
    form_class = VendaForm
    template_name = 'cadastrar/Venda.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda cadastrada com suceso!')
        return reverse_lazy('listar_venda')


class EletricosCreateView(CreateView):
    model = Eletricos
    form_class = EletricosForm
    template_name = 'cadastrar/eletricos.html'

    def get_success_url(self):
        messages.success(self.request, 'Eletrico cadastrado com suceso!')
        return reverse_lazy('listar_eletricos')


class HidraulicoCreateView(CreateView):
    model = Hidraulico
    form_class = HidraulicoForm
    template_name = 'cadastrar/hidraulico.html'

    def get_success_url(self):
        messages.success(self.request, 'Hidraulico cadastrado com suceso!')
        return reverse_lazy('listar_hidraulico')


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cadastrar/cliente.html'

    def get_success_url(self):
        messages.success(self.request, 'Cliente cadastrado com suceso!')
        return reverse_lazy('listar_cliente')


class VidroCreateView(CreateView):
    model = Vidro
    form_class = VidroForm
    template_name = 'cadastrar/vidro.html'

    def get_success_url(self):
        messages.success(self.request, 'Vidro cadastrado com suceso!')
        return reverse_lazy('listar_vidro')


class TintaCreateView(CreateView):
    model = Tinta
    form_class = TintaForm
    template_name = 'cadastrar/tinta.html'

    def get_success_url(self):
        messages.success(self.request, 'Tinta cadastrado com suceso!')
        return reverse_lazy('listar_tinta')


class EsquadriaCreateView(CreateView):
    model = Esquadria
    form_class = EsquadriaForm
    template_name = 'cadastrar/esquadria.html'

    def get_success_url(self):
        messages.success(self.request, 'Esquadria cadastrada com suceso!')
        return reverse_lazy('listar_esquadria')


class MadeiraCreateView(CreateView):
    model = Madeira
    form_class = MadeiraForm
    template_name = 'cadastrar/madeira.html'

    def get_success_url(self):
        messages.success(self.request, 'Madeira cadastrada com suceso!')
        return reverse_lazy('listar_madeira')


class PedraCreateView(CreateView):
    model = Pedra
    form_class = PedraForm
    template_name = 'cadastrar/pedra.html'

    def get_success_url(self):
        messages.success(self.request, 'Pedra cadastrada com suceso!')
        return reverse_lazy('listar_pedra')


class MaquinaCreateView(CreateView):
    model = Maquina
    form_class = MaquinaForm
    template_name = 'cadastrar/maquina.html'

    def get_success_url(self):
        messages.success(self.request, 'Maquina cadastrada com suceso!')
        return reverse_lazy('listar_maquina')


class CeramicaCreateView(CreateView):
    model = Ceramica
    form_class = CeramicaForm
    template_name = 'cadastrar/ceramica.html'

    def get_success_url(self):
        messages.success(self.request, 'Ceramica cadastrada com suceso!')
        return reverse_lazy('listar_ceramica')


class CobertaCreateView(CreateView):
    model = Coberta
    form_class = CobertaForm
    template_name = 'cadastrar/coberta.html'

    def get_success_url(self):
        messages.success(self.request, 'Coberta cadastrada com suceso!')
        return reverse_lazy('listar_coberta')


class FerramentaCreateView(CreateView):
    model = Ferramenta
    form_class = FerramentaForm
    template_name = 'cadastrar/ferramenta.html'

    def get_success_url(self):
        messages.success(self.request, 'Ferramenta cadastrada com suceso!')
        return reverse_lazy('listar_ferramenta')


class IluminacaoCreateView(CreateView):
    model = Iluminacao
    form_class = IluminacaoForm
    template_name = 'cadastrar/iluminacao.html'

    def get_success_url(self):
        messages.success(self.request, 'Iluminacao cadastrada com suceso!')
        return reverse_lazy('listar_iluminacao')


class EstruturaCreateView(CreateView):
    model = Estrutura
    form_class = EstruturaForm
    template_name = 'cadastrar/estrutura.html'

    def get_success_url(self):
        messages.success(self.request, 'Estrutura cadastrada com suceso!')
        return reverse_lazy('listar_estrutura')


class PisoCreateView(CreateView):
    model = Piso
    form_class = PisoForm
    template_name = 'cadastrar/piso.html'

    def get_success_url(self):
        messages.success(self.request, 'Piso cadastrado com suceso!')
        return reverse_lazy('listar_piso')


# ______________________________________ListView_____________________________________
class VendaListView(ListView):
    model = Venda
    template_name = 'listar/venda.html'
    paginate_by = 3


class EletricosListView(ListView):
    model = Eletricos
    template_name = 'listar/eletricos.html'
    paginate_by = 3


class HidraulicoListView(ListView):
    model = Hidraulico
    template_name = 'listar/hidraulico.html'
    paginate_by = 3


class ClienteListView(ListView):
    model = Cliente
    template_name = 'listar/cliente.html'
    paginate_by = 3


class VidroListView(ListView):
    model = Vidro
    template_name = 'listar/vidro.html'
    paginate_by = 3


class TintaListView(ListView):
    model = Tinta
    template_name = 'listar/tinta.html'
    paginate_by = 3


class EsquadriaListView(ListView):
    model = Esquadria
    template_name = 'listar/esquadria.html'
    paginate_by = 3


class MadeiraListView(ListView):
    model = Madeira
    template_name = 'listar/madeira.html'
    paginate_by = 3


class PedraListView(ListView):
    model = Pedra
    template_name = 'listar/pedra.html'
    paginate_by = 3


class MaquinaListView(ListView):
    model = Maquina
    template_name = 'listar/maquina.html'
    paginate_by = 3


class CeramicaListView(ListView):
    model = Ceramica
    template_name = 'listar/ceramica.html'
    paginate_by = 3


class CobertaListView(ListView):
    model = Coberta
    template_name = 'listar/coberta.html'
    paginate_by = 3


class FerramentaListView(ListView):
    model = Ferramenta
    template_name = 'listar/ferramenta.html'
    paginate_by = 3


class iluminacaoListView(ListView):
    model = Iluminacao
    template_name = 'listar/iluminacao.html'
    paginate_by = 3


class EstruturaListView(ListView):
    model = Estrutura
    template_name = 'listar/estrutura.html'
    paginate_by = 3


class PisoListView(ListView):
    model = Piso
    template_name = 'listar/piso.html'
    paginate_by = 3


# ______________________________________UpdateView_____________________________________
class VendaCorrecaoUpdateView(UpdateView):
    model = Venda
    form_class = VendaForm
    template_name = 'atualizar/venda.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda atualizada com sucesso!')
        return reverse_lazy('listar_venda')


class EletricosUpdateView(UpdateView):
    model = Eletricos
    form_class = EletricosForm
    template_name = 'atualizar/eletricos.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda de eletricos atualizada com sucesso!')
        return reverse_lazy('listar_eletricos')


class HidraulicoUpdateView(UpdateView):
    model = Hidraulico
    form_class = HidraulicoForm
    template_name = 'atualizar/hidraulico.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda de hidraulico atualizada com sucesso!')
        return reverse_lazy('listar_hidraulico')


class VidroUpdateView(UpdateView):
    model = Vidro
    form_class = VidroForm
    template_name = 'atualizar/vidro.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda de vidro atualizada com sucesso!')
        return reverse_lazy('listar_vidro')


class TintaUpdateView(UpdateView):
    model = Tinta
    form_class = TintaForm
    template_name = 'atualizar/tinta.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda de tinta atualizada com sucesso!')
        return reverse_lazy('listar_tinta')


class EsquadriaUpdateView(UpdateView):
    model = Esquadria
    form_class = EsquadriaForm
    template_name = 'atualizar/esquadria.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda de esquadria atualizada com sucesso!')
        return reverse_lazy('listar_esquadria')


class MadeiraUpdateView(UpdateView):
    model = Madeira
    form_class = MadeiraForm
    template_name = 'atualizar/madeira.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda de madeira atualizada com sucesso!')
        return reverse_lazy('listar_madeira')


class PedraUpdateView(UpdateView):
    model = Pedra
    form_class = PedraForm
    template_name = 'atualizar/pedra.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda de pedra atualizada com sucesso!')
        return reverse_lazy('listar_pedra')


class MaquinaUpdateView(UpdateView):
    model = Maquina
    form_class = MaquinaForm
    template_name = 'atualizar/maquina.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda de maquina atualizada com sucesso!')
        return reverse_lazy('listar_maquina')


class CeramicaUpdateView(UpdateView):
    model = Ceramica
    form_class = CeramicaForm
    template_name = 'atualizar/ceramica.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda de ceramica atualizada com sucesso!')
        return reverse_lazy('listar_ceramica')


class FerramentaUpdateView(UpdateView):
    model = Ferramenta
    form_class = FerramentaForm
    template_name = 'atualizar/ferramenta.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda de ferramenta atualizada com sucesso!')
        return reverse_lazy('listar_ferramenta')


class IluminacaoUpdateView(UpdateView):
    model = Iluminacao
    form_class = IluminacaoForm
    template_name = 'atualizar/iluminacao.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda de iluminacao atualizada com sucesso!')
        return reverse_lazy('listar_iluminacao')


class EstruturaUpdateView(UpdateView):
    model = Estrutura
    form_class = EstruturaForm
    template_name = 'atualizar/estrutura.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda de estrutura atualizada com sucesso!')
        return reverse_lazy('listar_estrutura')


class PisoUpdateView(UpdateView):
    model = Piso
    form_class = PisoForm
    template_name = 'atualizar/piso.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda de piso atualizada com sucesso!')
        return reverse_lazy('listar_piso')


class VendaAtualizarObservacaoView(UpdateView):
    model = Venda
    form_class = VendaObservacaoForm
    template_name = 'atualizar/venda_observacao.html'

    def get_success_url(self):
        messages.success(self.request, 'Observação da venda atualizada com sucesso!')
        return reverse_lazy('listar_venda')


class VendaAtualizarClienteView(UpdateView):
    model = Venda
    form_class = VendaClienteForm
    template_name = 'atualizar/venda_cliente.html'

    def get_success_url(self):
        messages.success(self.request, 'Cliente da venda atualizada com sucesso!')
        return reverse_lazy('listar_venda')


# ______________________________________View_____________________________________

class VendaView(View):
    def desabilitarVenda(self, pk: int):
        Venda.objects.filter(id=pk).update(excluido=True)
        return HttpResponseRedirect(reverse_lazy('listar_venda'))

    def habilitarVenda(self, pk: int):
        Venda.objects.filter(id=pk).update(excluido=False)
        return HttpResponseRedirect(reverse_lazy('listar_venda'))


# ______________________________________DetailView_____________________________________
class VendaDetailView(DetailView):
    model = Venda
    template_name = 'detalhes/venda.html'


class EletricosDetailView(DetailView):
    model = Eletricos
    template_name = 'detalhes/eletricos.html'


class HidraulicoDetailView(DetailView):
    model = Hidraulico
    template_name = 'detalhes/hidraulico.html'


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'detalhes/cliente.html'


class VidroDetailView(DetailView):
    model = Vidro
    template_name = 'detalhes/vidro.html'


class TintaDetailView(DetailView):
    model = Tinta
    template_name = 'detalhes/tinta.html'


class EsquadriaDetailView(DetailView):
    model = Esquadria
    template_name = 'detalhes/esquadria.html'


class MadeiraDetailView(DetailView):
    model = Madeira
    template_name = 'detalhes/madeira.html'


class PedraDetailView(DetailView):
    model = Pedra
    template_name = 'detalhes/pedra.html'


class MaquinaDetailView(DetailView):
    model = Maquina
    template_name = 'detalhes/maquina.html'


class CeramicaDetailView(DetailView):
    model = Ceramica
    template_name = 'detalhes/ceramica.html'


class CobertaDetailView(DetailView):
    model = Coberta
    template_name = 'detalhes/coberta.html'


class FerramentaDetailView(DetailView):
    model = Ferramenta
    template_name = 'detalhes/ferramenta.html'


class IluminacaoDetailView(DetailView):
    model = Iluminacao
    template_name = 'detalhes/iluminacao.html'


class EstruturaDetailView(DetailView):
    model = Estrutura
    template_name = 'detalhes/estrutura.html'


class PisoDetailView(DetailView):
    model = Piso
    template_name = 'detalhes/piso.html'


# ______________________________________PDFDetailView_____________________________________
class VendaPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Venda
    template_name = 'detalhes/pdf_venda.html'


class EletricosPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Eletricos
    template_name = 'detalhes/pdf_eletricos.html'


class HidraulicoPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Hidraulico
    template_name = 'detalhes/pdf_hidraulico.html'


class ClientePDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Cliente
    template_name = 'detalhes/pdf_cliente.html'


class VidroPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Vidro
    template_name = 'detalhes/pdf_vidro.html'


class TintaPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Vidro
    template_name = 'detalhes/pdf_vidro.html'


class EsquadriaPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Esquadria
    template_name = 'detalhes/pdf_esquadria.html'


class MadeiraPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Madeira
    template_name = 'detalhes/pdf_madeira.html'


class PedraPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Pedra
    template_name = 'detalhes/pdf_pedra.html'


class MaquinaPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Maquina
    template_name = 'detalhes/pdf_maquina.html'


class CeramicaPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Ceramica
    template_name = 'detalhes/pdf_ceramica.html'


class FerramentaPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Ferramenta
    template_name = 'detalhes/pdf_ferramenta.html'


class IluminacaoPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Iluminacao
    template_name = 'detalhes/pdf_iluminacao.html'


class PisoPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Piso
    template_name = 'detalhes/pdf_piso.html'
