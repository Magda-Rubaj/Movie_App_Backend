from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
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


class ExternalApiView(ExternalCallMixin, ListCreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def get_model_fields(self, request, url, *args, **kwargs):
        data = self.call_api(request, url, *args, **kwargs)
        return [{
            "title": entry["title"], 
            "production_year": entry.get("release_date")[:4], 
            "description": entry["overview"],
            "added_by": 1
        } for entry in data if entry.get("release_date") is not None]

    def get(self, request, *args, **kwargs):
        url = ('https://api.themoviedb.org/3/movie/popular'
               '?api_key=5a554cb0938200fedb337e0b6a2ca58b')
        data = self.get_model_fields(request, url, *args, **kwargs)
        for entry in data:
            serializer = self.get_serializer(data=entry)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        return Response(data=data)


