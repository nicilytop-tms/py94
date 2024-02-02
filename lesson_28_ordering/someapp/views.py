from django.shortcuts import render

from django.views import View

from someapp.models import News


class NewsView(View):
    def get(self, request):
        news = News.objects.values()
        return render(
            request,
            'index.html',
            context={
                'news': news,
            }
        )


class SortingNewsView(View):
    def get(self, request):
        sorting_param = request.GET["name_sorting"]
        priority_sorting = request.GET["priority_sorting"]
        news = News.objects.order_by(f'{priority_sorting}{sorting_param}')
        return render(
            request,
            'index.html',
            context={
                'news': news,
            }
        )
