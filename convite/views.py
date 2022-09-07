from django.shortcuts import render

def index(request):
    return render(request, 'convite/index.html')

def nossahistoria(request):
    return render(request, 'convite/nossahistoria.html')

def listadepresente(request):
    return render(request, 'convite/listadepresente.html')

def trajes(request):
    return render(request, 'convite/trajes.html')