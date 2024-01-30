from django.contrib import admin
from django.utils.safestring import mark_safe

from cars.models import Auto, Brand, User, ModelCar


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('model_car', 'is_free')


@admin.register(ModelCar)
class ModelCarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'count_autos')

    def count_autos(self, instance):
        count = Auto.objects.filter(model_car=instance).count()
        return count


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('preview', 'name')

    def preview(self, instance: Brand):
        if instance.logo:
            return mark_safe(f'<img style="max-width: 30px" src="{instance.logo.url}" alt="">')
        return mark_safe('Without logo')
