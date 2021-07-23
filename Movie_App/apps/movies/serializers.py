from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Movie, Actor, Director


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'production_year', 'image',
                  'description', 'added_by', 'rating', 'rating_count', 'users_voted')


class MoviePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title')


class ActorSerializer(WritableNestedModelSerializer):
    roles = MoviePartSerializer(many=True)
    class Meta:
        model = Actor
        fields = ('id', 'name', 'birth_date', 'image','rating', 
                  'roles', 'added_by', 'rating_count', 'users_voted')

class DirectorSerializer(serializers.ModelSerializer):
    directed = MoviePartSerializer(many=True)
    class Meta:
        model = Director
        fields = ('id', 'name', 'birth_date',  'image', 'rating', 
                  'directed', 'added_by', 'rating_count', 'users_voted')