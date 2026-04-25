from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from django.contrib.auth.models import User as UserModel
from drf_spectacular.utils import extend_schema, OpenApiExample
from users.serializers import UserSerializer
from users.permissions import IsSelfOrAdmin

_USER_EXAMPLE = OpenApiExample(
    "Example user",
    value={"username": "john_doe", "email": "john@example.com", "password": "secret123"},
    request_only=True,
)


@extend_schema(examples=[_USER_EXAMPLE])
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # Anyone can register
        if self.action == "create":
            return [AllowAny()]
        # Only admins can see the full user list
        if self.action == "list":
            return [IsAdminUser()]
        # retrieve / update / partial_update / destroy — owner or admin
        return [IsAuthenticated(), IsSelfOrAdmin()]
