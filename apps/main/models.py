import uuid, datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


def directory_path(instance, filename):
    ext = filename.split(".")
    return "movies/{0}.{1}".format(instance.id, ext[-1])


class Country(models.Model):
    code = models.CharField(max_length=3, unique=True, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "main_countries"
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
        ordering = ['name']

    def __str__(self):
        return self.name


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    year = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.date.today().year + 100),
        ],
    )
    poster_url = models.ImageField(upload_to=directory_path, null=True, blank=True)
    countries = models.ManyToManyField(Country, related_name='movies')
    age_rating = models.PositiveIntegerField(
        null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(18)]
    )
    description = models.TextField(null=True, blank=True)

    related_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "main_movies"
        verbose_name = "Кинофильм"
        verbose_name_plural = "Кинофильмы"
        ordering = ("id",)

    def __str__(self):
        return self.title_ru
