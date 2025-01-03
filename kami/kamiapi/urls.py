from rest_framework.routers import DefaultRouter
from .views import AirplaneViewSet

router = DefaultRouter()
router.register(r'v1/airplanes', AirplaneViewSet, basename='airplane')

urlpatterns = router.urls
