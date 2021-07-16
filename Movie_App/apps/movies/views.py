from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Movie, Actor, Director
from .serializers import MovieSerializer, ActorSerializer, DirectorSerializer

class MovieView(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class ActorView(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()

class DirectorView(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()