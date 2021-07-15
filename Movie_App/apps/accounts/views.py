
from rest_framework import viewsets
from .permissions import IsPostOrAuth
from .models import User
from .serializers import UserSerializer


class UserView(viewsets.ModelViewSet):
    permission_classes = (IsPostOrAuth, )
    serializer_class = UserSerializer
    queryset = User.objects.all()
