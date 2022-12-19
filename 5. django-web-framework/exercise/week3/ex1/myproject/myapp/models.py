from django.db import models

# Create your models here.

    
    
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)


class Menuitems(models.Model):
    itemname = models.CharField(max_length=200)
    category = models.CharField(max_length=300)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT,default=None, related_name="category_name")