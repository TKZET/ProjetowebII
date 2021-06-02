from django import forms
from .models import *


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'valor', 'numero_venda', 'observacao', 'comprovante_venda',
                  'venda_concluida', 'Produtosesq', 'Produtosmad', 'Produtosmaq', 'Produtosped',
                  'Produtoscer', 'Produtos1', 'Produtos2', 'Produtovid', 'Produtotin']


# ______________________________________Form_____________________________________
class EletricosForm(forms.ModelForm):
    class Meta:
        model = Eletricos
        fields = '__all__'


class HidraulicoForm(forms.ModelForm):
    class Meta:
        model = Hidraulico
        fields = '__all__'


class VidroForm(forms.ModelForm):
    class Meta:
        model = Vidro
        fields = '__all__'


class TintaForm(forms.ModelForm):
    class Meta:
        model = Tinta
        fields = '__all__'


class EsquadriaForm(forms.ModelForm):
    class Meta:
        model = Esquadria
        fields = '__all__'


class MadeiraForm(forms.ModelForm):
    class Meta:
        model = Madeira
        fields = '__all__'


class PedraForm(forms.ModelForm):
    class Meta:
        model = Pedra
        fields = '__all__'


class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = '__all__'


class CeramicaForm(forms.ModelForm):
    class Meta:
        model = Ceramica
        fields = '__all__'


class CobertaForm(forms.ModelForm):
    class Meta:
        model = Coberta
        fields = '__all__'


class FerramentaForm(forms.ModelForm):
    class Meta:
        model = Ferramenta
        fields = '__all__'


class IluminacaoForm(forms.ModelForm):
    class Meta:
        model = Iluminacao
        fields = '__all__'


class EstruturaForm(forms.ModelForm):
    class Meta:
        model = Coberta
        fields = '__all__'


class PisoForm(forms.ModelForm):
    class Meta:
        model = Piso
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


# ______________________________________Form_____________________________________


class VendaObservacaoForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['observacao']


class VendaClienteForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente']
