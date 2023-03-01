from django.db import models

# Create your models here.

# class Category(models.Model):
#     slug = models.SlugField()
#     title = models.CharField(max_length=255)


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return self.title
