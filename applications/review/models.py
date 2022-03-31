from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from applications.account.models import User
from applications.movies.models import Movie


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='review')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review')
    review = models.TextField()
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    frame = models.ImageField(upload_to='review_frames', blank=True, null=True)

    def __str__(self):
        return self.movie.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='like')
    like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.like}'

