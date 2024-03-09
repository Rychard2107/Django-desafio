from django.shortcuts import render, redirect
from .models import Anime
from django.forms import modelform_factory
from django.utils.text import slugify
from django.utils import timezone


def home(request):
    animes = Anime.objects.all().order_by('-id')
    return render(request, 'animes/pages/home.html', context={
        'animes': animes
    })


def genero(request, genero_id):
    animes = Anime.objects.filter(
        genero__id=genero_id
    ).order_by('-id')
    return render(request, 'animes/pages/home.html', context={
        'animes': animes,
    })


def detail(request, id):
    animes = Anime.objects.filter(
       __id=id
    )
    return render(request, 'animes/pages/anime-view.html', context={
        'animes': animes,
        'is_resume_page': True,
    })


def create_anime(request):
    AnimeForm = modelform_factory(Anime, exclude=('slug', 'data_criacao'))

    if request.method == 'POST':
        form = AnimeForm(request.POST, request.FILES)
        if form.is_valid():
            anime = form.save(commit=False)
            anime.slug = slugify(anime.nome_anime)
            anime.data_criacao = timezone.now()
            anime.save()

            return redirect('animes:home')
    else:
        form = AnimeForm()

    return render(request, 'animes/pages/create.html', context={
        'form': form,
    })
