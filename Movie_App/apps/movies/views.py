from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from django.conf import settings
from .models import Movie, Actor, Director
from .serializers import MovieSerializer, ActorSerializer, DirectorSerializer
from .mixins import SwitchSerializerMixin
from .permissions import IsAdminOrOwner
from .tasks import call_api


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


class ExternalApiView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def get_limit(self, request, *args, **kwargs):
        limit_param = 'limit'
        limit_value = request.query_params.get(limit_param, 1)
        return limit_value

    def get(self, request, *args, **kwargs):
        url = ('https://api.themoviedb.org/3/movie/popular'
               '?api_key={0}'.format(settings.MOVIEDB_API_KEY))
        limit = int(self.get_limit(request, *args, **kwargs))
        call_api.delay(url, limit, request.user.pk)
        return super().get(self, request, *args, **kwargs)


