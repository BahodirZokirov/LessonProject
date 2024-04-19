from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "users"
