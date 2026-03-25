from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet

APP_NAME = "authors"

router = DefaultRouter()
router.register(r"authors", AuthorViewSet, basename="authors")

urlpatterns = router.urls
