from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category_name = models.ForeignKey(Category,
                                      on_delete=models.CASCADE,
                                      to_field='category_name')
    product_name = models.CharField(max_length=50, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchased = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


