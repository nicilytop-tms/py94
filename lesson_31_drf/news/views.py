from rest_framework.viewsets import ModelViewSet

from news.models import News
from news.serializers import NewsSerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
