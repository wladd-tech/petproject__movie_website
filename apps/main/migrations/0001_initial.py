# Generated by Django 4.2.14 on 2024-08-24 14:07

import django.core.validators
from django.db import migrations, models
import main.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2124)])),
                ('poster_url', models.ImageField(blank=True, null=True, upload_to=main.models.directory_path)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('age_rating', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(18)])),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Кинофильм',
                'verbose_name_plural': 'Кинофильмы',
                'db_table': 'main_movie',
                'ordering': ('id',),
            },
        ),
    ]
