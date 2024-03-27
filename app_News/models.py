from django.db import models

# Create your models here.


class Categories (models.Model):
    name = models.CharField(max_length=255, verbose_name="Category name")
    description = models.TextField(verbose_name="Category's description")
    at_date = models.DateTimeField(auto_now_add=True, verbose_name="Added time")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "Categories"
        unique_together = ["name"]
        ordering = ["pk"]


class News(models.Model):
    news_title = models.CharField(max_length=255, verbose_name="News title")
    news_body = models.TextField(verbose_name="Text body")
    news_image = models.ImageField(upload_to='media')
    news_category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    at_date = models.DateTimeField(auto_now_add=True, verbose_name="Added_time")
    views_count = models.PositiveIntegerField(verbose_name="Views Count", default=0)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        unique_together = ["news_title", "news_category"]
        db_table = "News"
        ordering = ['pk']
