# Generated by Django 3.1.6 on 2021-02-06 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IDENTITY', '0002_auto_20210206_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemonspecie',
            name='pokemon_type',
        ),
        migrations.AddField(
            model_name='pokemonspecie',
            name='pokemon_type',
            field=models.ManyToManyField(null=True, to='IDENTITY.PokemonType'),
        ),
    ]
