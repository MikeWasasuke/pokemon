# Generated by Django 3.1.6 on 2021-02-06 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IDENTITY', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonspecie',
            name='pokemon_type',
            field=models.ForeignKey(max_length=2, on_delete=django.db.models.deletion.CASCADE, to='IDENTITY.pokemontype'),
        ),
    ]
