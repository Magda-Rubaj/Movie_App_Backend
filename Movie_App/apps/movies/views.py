from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from .models import Movie, Actor, Director
from .serializers import MovieSerializer, ActorSerializer, DirectorSerializer
from .mixins import SwitchSerializerMixin, ExternalCallMixin
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


class ExternalApiView(ExternalCallMixin, ListAPIView):
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        url = ('https://api.themoviedb.org/3/movie/popular'
               '?api_key=5a554cb0938200fedb337e0b6a2ca58b')
        return self.call_api(request, url, *args, **kwargs)

