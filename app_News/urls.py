from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (categories, category_business,
                    category_sport, category_politic,
                    category_sport_detail, category_politic_detail,
                    category_business_detail, categories_all,
                    news_add, news_edit, news_delete, category_all_detail,
                    news_add_form)

urlpatterns = [
    path("", categories, name="HomePage"),
    path("categories_all/", categories_all, name="categories_all"),
    path("business/", category_business, name="category_business"),
    path("sport/", category_sport, name="category_sport"),
    path("politic/", category_politic, name="category_politic"),

        #-----Detail-----
    path("all/media/detail/<int:pk>", category_all_detail, name="category_all_detail"),
    path("sport/detail/<int:pk>/", category_sport_detail, name="category_sport_detail"),
    path("politic/detail/<int:pk>/", category_politic_detail, name="category_politic_detail"),
    path("business/detail/<int:pk>/", category_business_detail, name="category_business_detail"),

        #-----CRUD-----
    path("media-add", news_add, name="news_add"),
    path("media/<int:pk>/edit", news_edit, name="news_edit"),
    path("media/<int:pk>/delete", news_delete, name='news_delete'),


          #-----forms-----
    path("add-form-news", news_add_form, name='news_add_form'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


