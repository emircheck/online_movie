from django.db import models
from applications.genre.utils import slug_generator


class Genre(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, primary_key=True, unique=True,
                            blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE,
                               related_name='children', blank=True,
                               null=True)

    def save(self, *args, **kwargs):
        self.slug = slug_generator(self.title)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
