from django.shortcuts import render
from .forms import Mensagensform
from .models import Mensagens, Galeria
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'babyoda/home.html')

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