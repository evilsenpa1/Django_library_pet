from books.views import BookViewSet
from rest_framework.routers import DefaultRouter

APP_NAME = "books"

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = router.urls
