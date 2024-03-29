from django.contrib import admin
from .models import CategoryProduct, Products


admin.site.register(Products)
admin.site.register(CategoryProduct)