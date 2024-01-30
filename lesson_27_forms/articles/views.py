from django.shortcuts import render
from django.views import View

from articles.models import Article
from articles.forms import ArticleCreateForm


class ArticleView(View):
    def get(self, request):
        articles = Article.objects.values()
        form = ArticleCreateForm()
        return render(request, 'index.html', {'articles': articles, 'article_form': form})

    def post(self, request):
        form = ArticleCreateForm(request.POST)
        if form.is_valid():
            form.save()

        articles = Article.objects.values()
        return render(request, 'index.html', {'articles': articles, 'article_form': form})
