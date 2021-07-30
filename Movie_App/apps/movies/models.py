from django.db import models
from django.contrib.auth import get_user_model


class Movie(models.Model):
    title = models.CharField(max_length=100)
    production_year = models.IntegerField()
    image = models.ImageField(default='defaults\movie.jpg', upload_to='posted_movies',)
    description = models.TextField()
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    rating_count = models.IntegerField(default=0)
    users_voted = models.ManyToManyField(
        get_user_model(), 
        related_name='movie_votes', 
        blank=True
    )

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    image = models.ImageField(default='defaults\person.jpg', upload_to='posted_actors',)
    rating = models.FloatField(default=0)
    roles = models.ManyToManyField(Movie, related_name='actors', blank=True)
    rating_count = models.IntegerField(default=0)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    users_voted = models.ManyToManyField(
        get_user_model(), 
        related_name='actor_votes', 
        blank=True
    )

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    image = models.ImageField(default='defaults\person.jpg', upload_to='posted_directors',)
    rating = models.FloatField(default=0)
    rating_count = models.IntegerField(default=0)
    directed = models.ManyToManyField(Movie, related_name='directors', blank=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    users_voted = models.ManyToManyField(
        get_user_model(), 
        related_name='director_votes', 
        blank=True
    )

    def __str__(self):
        return self.name
