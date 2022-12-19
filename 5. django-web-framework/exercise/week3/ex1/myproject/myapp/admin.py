from django.contrib import admin
from .models import Menuitems
from .models import MenuCategory

# Register your models here.
admin.site.register(Menuitems)
admin.site.register(MenuCategory)