from django.db import models

# Create your models here.

class PokemonSpecie(models.Model):
    pokemon_name = models.CharField(max_length=250)
    pokemon_type = models.ManyToManyField('PokemonType', null=True)
    evolution_level = models.IntegerField()
    next_evolution = models.CharField(max_length=250)

    def __str__(self):
        return self.pokemon_name



class PokemonType(models.Model):
    pokemon_type = models.CharField(max_length=250)

    def __str__(self):
        return self.pokemon_type

class Pokemon(models.Model):
    nickname = models.CharField(max_length=250)
    species = models.CharField(max_length=250)
    level = models.IntegerField()
    trainer = models.CharField(max_length=250)

    def __str__(self):
        return self.name