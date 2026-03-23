from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from django.contrib.auth.models import User as UserModel
from users.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
