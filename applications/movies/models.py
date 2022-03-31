from django.db import models
from applications.genre.models import Genre


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL, related_name='movie')
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class MovieImage(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='movie_posters')

    def __str__(self):
        return self.movie.title
