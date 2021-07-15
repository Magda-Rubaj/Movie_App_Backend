from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Movie
from .serializers import MovieSerializer

class MovieView(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
