from django.db import models

# Create your models here.


class Category(models.Model):
    name                = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category            = models.ForeignKey(Category, on_delete=models.CASCADE)
    description         = models.CharField(max_length=2000)
    images              = models.TextField(max_length=5000)
    name                = models.CharField(max_length=250)
    price               = models.DecimalField(max_digits=13, decimal_places=2)
    quantity            = models.SmallIntegerField()

    def __str__(self):
        return self.name