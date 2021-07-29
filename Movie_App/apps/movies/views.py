from rest_framework import viewsets
from .models import Movie, Actor, Director
from .serializers import MovieSerializer, ActorSerializer, DirectorSerializer
from .mixins import SwitchSerializerMixin
from .permissions import IsAdminOrOwner


class MovieView(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrOwner, )
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    

class ActorView(SwitchSerializerMixin, viewsets.ModelViewSet):
    permission_classes = (IsAdminOrOwner, )
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()


class DirectorView(SwitchSerializerMixin, viewsets.ModelViewSet):
    permission_classes = (IsAdminOrOwner, )
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()

