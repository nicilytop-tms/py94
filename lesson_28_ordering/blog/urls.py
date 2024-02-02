from django.contrib import admin
from django.urls import path

from someapp.views import NewsView, SortingNewsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', NewsView.as_view()),
    path('sorting-news/', SortingNewsView.as_view()),
]
