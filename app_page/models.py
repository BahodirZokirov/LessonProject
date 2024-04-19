from django.contrib.auth import get_user_model
from django.db import models


class CarCategory(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "Category"


class Cars (models.Model):
    car_name = models.CharField(max_length=50, verbose_name="Name")
    car_make = models.CharField(max_length=50, verbose_name="Make")
    car_image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name="Image")
    car_price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Price")
    car_year = models.PositiveIntegerField(verbose_name="Year")
    car_category = models.ForeignKey(CarCategory, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Category")
    car_added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Author", null=True, blank=True)
    car_view_count = models.PositiveSmallIntegerField(verbose_name="Views count", default=0, blank=True, null=True)
    car_added_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    car_update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.car_name

    class Meta:
        verbose_name = "Cars"
        verbose_name_plural = "Cars"
        db_table = "Cars"
