from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    count_views = models.PositiveIntegerField()
    email = models.EmailField(unique=True, null=True, blank=True, default=None)
