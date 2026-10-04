from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, KeywordViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("keywords", KeywordViewSet)

urlpatterns = [
    path("", include(router.urls)),
]