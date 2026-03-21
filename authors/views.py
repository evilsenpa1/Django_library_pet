from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import AuthorModel
from .serializers import AuthorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]
