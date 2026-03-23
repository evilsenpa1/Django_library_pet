from rest_framework.routers import DefaultRouter

from .views import UserViewSet

APP_NAME = "users"

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = router.urls
