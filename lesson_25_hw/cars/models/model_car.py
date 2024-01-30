from django.db import models


class ModelCar(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
