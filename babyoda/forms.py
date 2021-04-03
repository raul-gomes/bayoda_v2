from django import forms

class Mensagensform(forms.Form):
    nome = forms.CharField(max_length=255)
    mensagem = forms.CharField(max_length=1000)

class ListaForm(forms.Form):
    item = forms.CharField(max_length=255)
    valor = forms.CharField(max_length=10)
    quantidade = forms.CharField(max_length=2)