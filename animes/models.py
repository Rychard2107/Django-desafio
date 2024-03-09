from django.contrib.auth.models import User
from django.db import models


class Genero(models.Model):
    genero = models.CharField(max_length=20)

    def __str__(self):
        return (self.genero)


class anime(models.Model):
    nome_anime = models.CharField(max_length=65)
    slug = models.SlugField()
    resumo = models.TextField()
    resumo_is_html = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=False)
    img_anime = models.ImageField(upload_to='animes/covers/%Y/%m/%d/')
    genero = models.ForeignKey(
        Genero, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    episodios = models.IntegerField()

    def __str__(self):
        return (self.nome_anime)
