from django.shortcuts import render


def home(request):
    return render(request, 'animes/pages/home.html')


def anime(request, id):
    return render(request, 'animes/pages/anime-view.html')
