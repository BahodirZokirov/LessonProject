from django.contrib import admin

# Register your models here.
from .models import Cars, CarCategory


admin.site.register(Cars)
admin.site.register(CarCategory)
