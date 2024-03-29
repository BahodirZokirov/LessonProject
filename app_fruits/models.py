from django.db import models


class CategoryProduct(models.Model):
    name = models.CharField(max_length=50, verbose_name="Product category")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"
        db_table = "Categories"


class Products(models.Model):
    product_name = models.CharField(max_length=50, verbose_name="Product name")
    product_description = models.TextField(verbose_name="Product description")
    product_category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name="Product category")
    product_image = models.ImageField(upload_to='products', verbose_name="Product image")
    product_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Product price")

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"
        db_table = "Products"
