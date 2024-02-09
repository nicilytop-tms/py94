from django.views import View
from django.shortcuts import redirect

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from news.models import News
from news.constants import NewsStatus


class MainView(View):
    def get(self, request):
        all_news = News.objects.filter(is_published=True)
        return render(request, 'index.html', {'all_news': all_news})


class EditNewsView(View):
    def get(self, request, pk):
        news = News.objects.get(pk=pk)
        return render(request, 'edit_news.html', {'news': news})

    def post(self, request, pk):
        news = News.objects.get(pk=pk, user=request.user)

        news.title = request.POST["title"]
        news.content = request.POST["content"]

        image_news = request.FILES.get('image')
        if image_news:
            fs = FileSystemStorage()
            url = fs.save(image_news.name, image_news)
            news.image = url
        news.save()
        return redirect('profile')


class RemoveNewsView(View):
    def get(self, request, pk):
        News.objects.filter(pk=pk, user=request.user).delete()
        return redirect('profile')


class SendCheckNewsView(View):
    def get(self, request, pk):
        news = News.objects.get(pk=pk, user=request.user, status=NewsStatus.DRAFT)
        news.status = NewsStatus.VERIFICATION_SENT
        news.save()
        return redirect('profile')


class PublishNewsView(View):
    def get(self, request, pk):
        news = News.objects.get(pk=pk, user=request.user, status=NewsStatus.VERIFICATION_SUCCESS)
        news.is_published = True
        news.save()
        return redirect('profile')


class ReadNewsView(View):
    def get(self, request, pk):
        news = News.objects.get(pk=pk, is_published=True)
        return render(request, 'read_news.html', {'news': news})
