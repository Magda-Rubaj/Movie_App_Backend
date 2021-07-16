from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Movie, Actor
from .serializers import MovieSerializer, ActorSerializer

class MovieView(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class ActorView(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()
