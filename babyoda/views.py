from django.shortcuts import render
from .forms import Mensagensform, ListaForm
from .models import Mensagens, Galeria, Lista
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'babyoda/home.html')

def lista(request):
    return render(request, 'babyoda/lista.html', {
        'lista': Lista.objects.all()
    })

def carrinho(request):
    if request.method == 'POST':
        form = ListaForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)

    return render(request, 'babyoda/carrinho.html')

def evento(request):
    return render(request, 'babyoda/evento.html')


def galeria(request):

    return render(request, 'babyoda/galeria.html', {
        'galeria': Galeria.objects.all()
    })

def mensagens(request):
    
    if request.method == 'POST':
        form = Mensagensform(request.POST)        
        
        if form.is_valid():
            Mensagens.objects.create(**form.cleaned_data)
            return render(request, 'babyoda/mensagens.html', {'messages': 'Sua mensagem foi enviada'})
    
    return render(request, 'babyoda/mensagens.html')