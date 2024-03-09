from animes.models import Genero, anime
from django.contrib import admin


class GeneroAdmin(admin.ModelAdmin):
    ...


@admin.register(anime)
class AnimeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Genero, GeneroAdmin)