
from rest_framework import generics, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from django.contrib.auth.models import User
from .serializers import EmailTokenSerializer, UserSerializer


class EmailTokenView(TokenObtainPairView):
    serializer_class = EmailTokenSerializer

class UserView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSerializer
    queryset = User.objects.all()
