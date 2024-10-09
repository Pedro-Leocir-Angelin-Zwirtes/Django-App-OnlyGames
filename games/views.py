from django.shortcuts import render
from . models import *
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'games/index.html')

def lista(request):
    pesquisa = request.GET.get('pesquisa')
    if pesquisa:
        jogos = Jogo.objects.filter(nome__icontains=pesquisa)
    else:
        jogos = Jogo.objects.all()
    context = {
        'jogos': jogos
    }
    return render(request, 'games/lista.html', context=context)

def detalhe(request, id):
    jogo = get_object_or_404(Jogo, pk=id)
    context = {
        'jogo':jogo
    }
    return render(request, 'games/detalhe.html', context=context)