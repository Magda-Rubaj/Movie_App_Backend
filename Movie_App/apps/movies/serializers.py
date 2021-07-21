from rest_framework import serializers
from .models import Movie, Actor, Director


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'production_year', 'image',
                 'description', 'added_by', 'rating')

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'birth_date', 'image','rating', 'roles', 'added_by')

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name', 'birth_date',  'image', 'rating', 'directed', 'added_by')