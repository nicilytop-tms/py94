from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    auto = models.ForeignKey('Auto', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    phone = models.CharField(max_length=255)
