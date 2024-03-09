from django.shortcuts import render
from utils.animes.factory import make_fake_anime
from .models import anime


def home(request):
    animes = anime.objects.all().order_by('-id')
    return render(request, 'animes/pages/home.html', context={
        'animes': animes
    })


def detail(request, id):
    return render(request, 'animes/pages/anime-view.html', context={
        'anime': make_fake_anime(),
        'is_resume_page': True,
    })
