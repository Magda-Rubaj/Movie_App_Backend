from django.db import models
from django.contrib.auth import get_user_model


class Movie(models.Model):
    title = models.CharField(max_length=50)
    production_year= models.IntegerField()
    image = models.ImageField(default='defaults\movie.jpg', upload_to='posted_movies',)
    description = models.TextField()
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    rating = models.IntegerField(default=5)


