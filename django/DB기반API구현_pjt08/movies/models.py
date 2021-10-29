from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField

# Create your models here.
class Actor(models.Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    actors = models.ManyToManyField(Actor, related_name='movies')
    title = CharField(max_length=100)
    overview = TextField()
    release_date = DateTimeField()
    poster_path = TextField()

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    content = models.TextField()
    RANKS = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]
    rank = models.IntegerField(choices=RANKS, default=5)

    def __str__(self):
        return self.title