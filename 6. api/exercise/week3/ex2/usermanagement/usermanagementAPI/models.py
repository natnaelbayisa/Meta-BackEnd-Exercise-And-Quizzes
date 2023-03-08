from django.db import models

# Create your models here.

class Category(models.Model):
    slug = models.SlugField()
    username = models.CharField(max_length=255)

    def __str__(self)-> str:
        return self.username


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    def __str__(self)-> str:
        return self.username


