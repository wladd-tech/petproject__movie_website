from pyclbr import Class
import uuid
from django.db import models


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    year = models.PositiveIntegerField(blank=True)
    poster_url = models.ImageField(upload_to="movies/%Y", blank=True)
