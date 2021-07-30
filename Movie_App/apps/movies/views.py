from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Movie, Actor, Director
from .serializers import MovieSerializer, ActorSerializer, DirectorSerializer, MoviePartSerializer
from .permissions import IsAdminOrOwner


class MovieView(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrOwner, )
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    

class ActorView(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrOwner, )
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()

    def dispatch(self, request, *args, **kwargs):
        mapping = {
            "get": MoviePartSerializer
        }
        serializer = mapping.get(request.method.lower(), MovieSerializer)
        return super().dispatch(request, *args, **kwargs)


class DirectorView(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrOwner, )
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()

    def dispatch(self, request, *args, **kwargs):
        mapping = {
            "get": MoviePartSerializer
        }
        serializer = mapping.get(request.method.lower(), MovieSerializer)
        return super().dispatch(request, *args, **kwargs)
