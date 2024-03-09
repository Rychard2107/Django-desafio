from animes.models import Genero, Anime
from django.contrib import admin


class GeneroAdmin(admin.ModelAdmin):
    ...


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Genero, GeneroAdmin)
