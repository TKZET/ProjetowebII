from django import forms
from .models import *


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'valor', 'numero_venda', 'observacao', 'comprovante_venda',
                  'venda_concluida', 'Produtosesq', 'Produtosmad', 'Produtosmaq', 'Produtosped',
                  'Produtoscer', 'Produtos1', 'Produtos2', 'Produtovid', 'Produtotin']


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


class VendaObservacaoForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['observacao']


class VendaClienteForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'
