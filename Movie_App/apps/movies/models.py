from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=50)
    production_year= models.IntegerField()
    image = models.ImageField(default='defaults\movie.jpg', upload_to='posted_movies',)
    description = models.TextField()

