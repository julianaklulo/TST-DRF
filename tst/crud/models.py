from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"Category {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"Product {self.name}"
