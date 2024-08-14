import uuid
from django.db import models


def directory_path(instance, filename):
    ext = filename.split('.')
    return 'movies/{0}.{1}'.format(instance.id, ext[-1])


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    year = models.PositiveIntegerField(blank=True)
    poster_url = models.ImageField(upload_to=directory_path, blank=True)

    
    class Meta:
        db_table = "main_movie"
        verbose_name = "Кинофильм"
        verbose_name_plural= "Кинофильмы"
