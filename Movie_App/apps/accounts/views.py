
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .permissions import IsPostAdminOrSelf
from .models import User
from .serializers import UserSerializer


class UserView(viewsets.ModelViewSet):
    permission_classes = (IsPostAdminOrSelf, )
    serializer_class = UserSerializer
    queryset = User.objects.all()
