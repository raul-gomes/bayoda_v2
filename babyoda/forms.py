from django import forms

class GaleriaForm(forms.Form):
    pass

class Mensagensform(forms.Form):
    nome = forms.CharField(max_length=255)
    mensagem = forms.CharField(max_length=1000)

class ListaForm(forms.Form):
    pass