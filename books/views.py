
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from books.models import BookModel
from books.serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.prefetch_related("authors").all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
