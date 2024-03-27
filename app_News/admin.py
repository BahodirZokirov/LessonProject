from django.contrib import admin
from .models import Categories, News
# Register your models here.


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["pk", 'name']


class NewsAdmin(admin.ModelAdmin):
    list_display = ["pk", "news_title", "news_category"]
    search_fields = ["news_title"]
    list_filter = ["news_category"]


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(News, NewsAdmin)
