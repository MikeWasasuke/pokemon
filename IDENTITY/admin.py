from django.contrib import admin
from .models import PokemonType, PokemonSpecie, Pokemon

admin.site.register(PokemonType)
admin.site.register(PokemonSpecie)
admin.site.register(Pokemon)
