from books.views import BookViewSet
from rest_framework.routers import DefaultRouter

app_name = "books"

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = router.urls
