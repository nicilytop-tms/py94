from django.db import models


class Auto(models.Model):
    vin_code = models.CharField(max_length=255)
    is_free = models.BooleanField(default=False)
    model_car = models.ForeignKey('ModelCar', on_delete=models.CASCADE)
