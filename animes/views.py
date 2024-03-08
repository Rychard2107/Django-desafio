from django.shortcuts import render
from utils.animes.factory import make_fake_anime


def home(request):
    return render(request, 'animes/pages/home.html', context={
        'animes': [make_fake_anime() for _ in range(12)]
    })


def anime(request, id):
    return render(request, 'animes/pages/anime-view.html', context={
        'anime': make_fake_anime(),
        'is_resume_page': True,
    })
