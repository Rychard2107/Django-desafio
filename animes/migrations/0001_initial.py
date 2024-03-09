# Generated by Django 5.0.2 on 2024-03-09 04:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_anime', models.CharField(max_length=65)),
                ('slug', models.SlugField()),
                ('resumo', models.TextField()),
                ('resumo_is_html', models.BooleanField(default=False)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('publicado', models.BooleanField(default=False)),
                ('img_anime', models.ImageField(upload_to='animes/covers/%Y/%m/%d/')),
                ('episodios', models.IntegerField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('genero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='animes.genero')),
            ],
        ),
    ]
