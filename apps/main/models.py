import uuid, datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


def directory_path(instance, filename):
    ext = filename.split(".")
    return "movies/{0}.{1}".format(instance.id, ext[-1])


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
    country = models.CharField(max_length=255, null=True, blank=True)
    age_rating = models.PositiveIntegerField(
        null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(18)]
    )
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "main_movie"
        verbose_name = "Кинофильм"
        verbose_name_plural = "Кинофильмы"
        ordering = ("id",)
