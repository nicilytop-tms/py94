from django.urls import path, include

from news.views import NewsViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
