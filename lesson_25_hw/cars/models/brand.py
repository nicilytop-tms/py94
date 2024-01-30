from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(null=True, blank=True, default=None, upload_to='logos')

    def __str__(self):
        return self.name
