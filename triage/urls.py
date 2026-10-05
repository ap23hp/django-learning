from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, KeywordViewSet, TriageView

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("keywords", KeywordViewSet)

urlpatterns = [
    path("triage/", TriageView.as_view()),
    path("", include(router.urls)),
]