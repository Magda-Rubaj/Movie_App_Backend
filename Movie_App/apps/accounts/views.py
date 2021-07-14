
from rest_framework import viewsets
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer


class UserView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSerializer
    queryset = User.objects.all()
