from django.db import models

from news.constants import NewsStatus


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images', null=True, blank=True, default=None)

    status = models.IntegerField(choices=NewsStatus.choices, default=NewsStatus.DRAFT)
    is_published = models.BooleanField(default=False)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
