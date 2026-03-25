
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from books.models import BookModel
from books.serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
